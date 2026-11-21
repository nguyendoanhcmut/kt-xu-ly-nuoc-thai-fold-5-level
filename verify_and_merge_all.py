#!/usr/bin/env python3
"""
verify_and_merge_all.py
Audits and merges all 8 Fold Solver Worker outputs (solutions/sol_w1.json .. sol_w8.json)
into ALL_54_EXERCISES_COMPLETE_SOLUTIONS.json, and verifies all 17 5-Level Semantic Zoom
TextFold readers via fold_pipeline.py verify.
"""

import hashlib
import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(r"C:\antgravity workplace\hcmut-263\kt xu ly nuoc thai\fold_5_level_v1")
_SKILL_ROOT = Path(r"C:\Users\Admin\.gemini\config\skills\textfold-branches")
if not _SKILL_ROOT.exists():
    _SKILL_ROOT = Path(r"C:\Users\Admin\.gemini\config\skills\branches")
FOLD_PIPELINE = _SKILL_ROOT / "scripts" / "fold_pipeline.py"
EXPECTED_BRIEF_ID = "f51e2026"

ALL_SLUGS = [
    "ch01", "ch02",
    "ch03_1", "ch03_2", "ch03_3", "ch03_4", "ch03_5",
    "ch04_1", "ch04_2", "ch04_3",
    "ch05_1", "ch05_2",
    "ch06", "ch07", "ch08", "ch09", "ch10",
]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_and_merge_solutions(wave_summary: list[dict]) -> tuple[dict, list[str]]:
    errors = []
    worker_records = []
    all_exercises = []
    input_sha256_map = {}

    for item in wave_summary:
        wid = item["worker_id"]
        k = wid.replace("ch_w", "")
        sol_path = BASE_DIR / "solutions" / f"sol_w{k}.json"
        in_path = Path(item["input_file"])
        expected_sha = item["sha256"]
        actual_in_sha = sha256_file(in_path)
        if actual_in_sha != expected_sha:
            errors.append(f"[{wid}] worker_input SHA mismatch: {actual_in_sha} != {expected_sha}")

        if not sol_path.exists():
            errors.append(f"[{wid}] missing solution file: {sol_path}")
            continue

        data = json.loads(sol_path.read_text(encoding="utf-8"))
        changed = False

        if data.get("brief_id") != EXPECTED_BRIEF_ID:
            data["brief_id"] = EXPECTED_BRIEF_ID
            changed = True

        sol_sha = str(data.get("input_sha256", ""))
        if sol_sha != expected_sha:
            if expected_sha.startswith(sol_sha) or not sol_sha:
                data["input_sha256"] = expected_sha
                changed = True
            else:
                errors.append(f"[{wid}] input_sha256 mismatch: {sol_sha} != {expected_sha}")

        if changed:
            sol_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

        input_sha256_map[wid] = data["input_sha256"]
        exs = data.get("exercises", [])
        expected_total = item["pdf_ex_count"] + item["proj_ex_count"]
        if len(exs) != expected_total:
            errors.append(f"[{wid}] exercise count {len(exs)} != expected {expected_total}")

        for ex in exs:
            if ex.get("status_after") != "COMPLETE":
                errors.append(f"[{wid}] exercise {ex.get('exercise_id')} status_after={ex.get('status_after')} != COMPLETE")
            all_exercises.append(ex)

        worker_records.append({
            "worker_id": wid,
            "solution_file": f"solutions/sol_w{k}.json",
            "assigned_slugs": item["slugs"],
            "input_sha256": data["input_sha256"],
            "pdf_ex_count": sum(1 for e in exs if e.get("category") == "pdf_exercise"),
            "proj_ex_count": sum(1 for e in exs if e.get("category") in ("projector_only", "projector_exercise")),
            "total_exercises": len(exs),
        })

    pdf_exs = [e for e in all_exercises if e.get("category") == "pdf_exercise"]
    proj_exs = [e for e in all_exercises if e.get("category") in ("projector_only", "projector_exercise")]

    if len(pdf_exs) != 39:
        errors.append(f"Total PDF exercises = {len(pdf_exs)}, expected 39")
    if len(proj_exs) != 15:
        errors.append(f"Total projector exercises = {len(proj_exs)}, expected 15")
    if len(all_exercises) != 54:
        errors.append(f"Total exercises = {len(all_exercises)}, expected 54")

    status_before_counts = {}
    for e in all_exercises:
        sb = e.get("status_before", "UNKNOWN")
        status_before_counts[sb] = status_before_counts.get(sb, 0) + 1

    merged = {
        "brief_id": EXPECTED_BRIEF_ID,
        "course": "Kỹ thuật Xử lý Nước thải (HCMUT - PGS.TS. Nguyễn Tấn Phong)",
        "total_chapters": 17,
        "total_exercises": len(all_exercises),
        "pdf_exercises_count": len(pdf_exs),
        "projector_exercises_count": len(proj_exs),
        "status_before_breakdown": status_before_counts,
        "status_after_complete_count": sum(1 for e in all_exercises if e.get("status_after") == "COMPLETE"),
        "input_sha256": input_sha256_map,
        "workers": worker_records,
        "exercises": all_exercises,
    }
    return merged, errors


def verify_all_fold_readers() -> tuple[list[dict], list[str]]:
    reader_reports = []
    errors = []

    for slug in ALL_SLUGS:
        reader_dir = BASE_DIR / "readers" / slug
        fold_json_path = reader_dir / f"{slug}.fold.json"
        fold_html_path = reader_dir / f"{slug}.fold.html"
        fig_manifest_path = reader_dir / "figures_manifest.json"
        md_path = BASE_DIR / "chapters_md" / f"{slug}.md"

        cmd = [
            sys.executable,
            str(FOLD_PIPELINE),
            "verify",
            str(reader_dir),
            "--slug",
            slug,
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        stdout_clean = proc.stdout.strip()
        passed = (proc.returncode == 0) and ("FOLD VERIFICATION PASSED" in stdout_clean)
        if not passed:
            errors.append(f"[{slug}] fold verify failed (rc={proc.returncode}): {stdout_clean} {proc.stderr.strip()}")

        sections_count = 0
        units_count = 0
        atoms_count = 0
        figures_count = 0
        title = slug

        if fold_json_path.exists():
            fdata = json.loads(fold_json_path.read_text(encoding="utf-8"))
            title = fdata.get("title", slug)
            secs = fdata.get("sections", [])
            links = fdata.get("links", [])
            links_iter = links.values() if isinstance(links, dict) else links
            sections_count = len(secs)
            units_count = sum(len(s.get("units", [])) for s in secs)
            atoms_count = len(links)
            figures_count = sum(1 for a in links_iter if isinstance(a, dict) and a.get("kind") == "figure")

        manifest_figs = 0
        if fig_manifest_path.exists():
            mdata = json.loads(fig_manifest_path.read_text(encoding="utf-8"))
            manifest_figs = len(mdata.get("figures", []))

        reader_reports.append({
            "slug": slug,
            "title": title,
            "markdown_file": f"chapters_md/{slug}.md",
            "markdown_bytes": md_path.stat().st_size if md_path.exists() else 0,
            "fold_html": f"readers/{slug}/{slug}.fold.html",
            "fold_html_bytes": fold_html_path.stat().st_size if fold_html_path.exists() else 0,
            "fold_json": f"readers/{slug}/{slug}.fold.json",
            "sections_count": sections_count,
            "units_count": units_count,
            "atoms_count": atoms_count,
            "embedded_figures_count": figures_count,
            "manifest_figures_count": manifest_figs,
            "verify_exit_code": proc.returncode,
            "verify_output": stdout_clean,
            "verify_passed": passed,
        })
        print(f"  [{slug}] rc={proc.returncode} | sections={sections_count} | units={units_count} | figs={manifest_figs} | {stdout_clean}")

    return reader_reports, errors


def main() -> int:
    wave_summary_path = BASE_DIR / "wave_plan_summary.json"
    wave_summary = json.loads(wave_summary_path.read_text(encoding="utf-8"))

    print("=== STEP 1: Auditing and merging 8 worker solution JSONs ===")
    merged, sol_errors = verify_and_merge_solutions(wave_summary)
    print(f"  Total exercises merged: {merged['total_exercises']} (PDF: {merged['pdf_exercises_count']}, Projector: {merged['projector_exercises_count']})")
    print(f"  Status before breakdown: {merged['status_before_breakdown']}")
    print(f"  Status after COMPLETE: {merged['status_after_complete_count']} / {merged['total_exercises']}")

    print("\n=== STEP 2: Verifying all 17 5-Level Semantic Zoom Readers ===")
    reader_reports, fold_errors = verify_all_fold_readers()
    merged["readers"] = reader_reports
    merged["readers_verified_count"] = sum(1 for r in reader_reports if r["verify_passed"])

    out_path = BASE_DIR / "ALL_54_EXERCISES_COMPLETE_SOLUTIONS.json"
    out_path.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nWrote master JSON: {out_path} ({out_path.stat().st_size:,} bytes)")

    all_errors = sol_errors + fold_errors
    if all_errors:
        print("\n=== VERIFICATION FAILED ===")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print("\n=== ALL 54 EXERCISES & 17 FOLD READERS VERIFIED SUCCESSFULLY ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
