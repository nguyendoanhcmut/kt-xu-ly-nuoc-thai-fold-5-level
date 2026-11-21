import os
import json
import hashlib

BASE_DIR = r"C:\antgravity workplace\hcmut-263\kt xu ly nuoc thai"
AUDIT_DIR = os.path.join(BASE_DIR, "audit_exercise_map_v1")
OUT_DIR = os.path.join(BASE_DIR, "fold_5_level_v1")

for sub in ["worker_inputs", "solutions", "chapters_md", "readers"]:
    os.makedirs(os.path.join(OUT_DIR, sub), exist_ok=True)

with open(os.path.join(AUDIT_DIR, "merged_audit_v2_with_duynguyen.json"), "r", encoding="utf-8") as f:
    merged_v2 = json.load(f)

with open(os.path.join(AUDIT_DIR, "EXERCISE_SOLUTION_RECONCILIATION_V2.json"), "r", encoding="utf-8") as f:
    recon_v2 = json.load(f)

with open(os.path.join(AUDIT_DIR, "raw_inputs_manifest.json"), "r", encoding="utf-8") as f:
    raw_manifest = json.load(f)

pdf_by_slug = {item["slug"]: item for item in raw_manifest["pdfs"]}
chapters_raw = merged_v2.get("chapters", [])
chapters_audit = {item["slug"]: item for item in chapters_raw} if isinstance(chapters_raw, list) else chapters_raw
photos_all = merged_v2.get("photos", [])

# Index reconciled PDF exercises and projector exercises by chapter slug
pdf_ex_raw = recon_v2.get("pdf_exercise_reconciliation", [])
if isinstance(pdf_ex_raw, dict):
    pdf_ex_list = [{**v, "exercise_id": k} for k, v in pdf_ex_raw.items()]
else:
    pdf_ex_list = pdf_ex_raw
pdf_ex_by_slug = {}
for ex in pdf_ex_list:
    eid = ex.get("exercise_id") or ex.get("id") or ex.get("problem_id")
    ex["exercise_id"] = eid
    slug = ex.get("chapter_slug") or ex.get("slug") or eid.rsplit("_ex", 1)[0]
    pdf_ex_by_slug.setdefault(slug, []).append(ex)

proj_ex_raw = recon_v2.get("projector_only_problems", [])
if isinstance(proj_ex_raw, dict):
    proj_ex_list = [{**v, "exercise_id": k} for k, v in proj_ex_raw.items()]
else:
    proj_ex_list = proj_ex_raw
proj_ex_by_slug = {}
for pex in proj_ex_list:
    eid = pex.get("exercise_id") or pex.get("id") or pex.get("problem_id")
    pex["exercise_id"] = eid
    slug = pex.get("chapter_slug") or pex.get("slug")
    if not slug or slug not in pdf_by_slug:
        if "ch02" in eid:
            slug = "ch02"
        elif "ch03_1" in eid:
            slug = "ch03_1"
        elif "ch03_2" in eid:
            slug = "ch03_2"
        elif "ch03_3" in eid or "api" in eid:
            slug = "ch03_3"
        elif "ch03_4" in eid:
            slug = "ch03_4"
        elif "ch03_5" in eid:
            slug = "ch03_5"
        elif "ch04_1" in eid:
            slug = "ch04_1"
        elif "ch04_2" in eid:
            slug = "ch04_2"
        elif "ch04_3" in eid:
            slug = "ch04_3"
        else:
            slug = "other"
    proj_ex_by_slug.setdefault(slug, []).append(pex)

WORKER_GROUPS = [
    ("ch_w1", ["ch01", "ch02"]),
    ("ch_w2", ["ch03_1", "ch03_2"]),
    ("ch_w3", ["ch03_3", "ch03_4"]),
    ("ch_w4", ["ch03_5", "ch04_1"]),
    ("ch_w5", ["ch04_2", "ch04_3"]),
    ("ch_w6", ["ch05_1", "ch05_2"]),
    ("ch_w7", ["ch06", "ch07"]),
    ("ch_w8", ["ch08", "ch09", "ch10"]),
]

summary = []
for wid, slugs in WORKER_GROUPS:
    payload_chapters = []
    for slug in slugs:
        pmeta = pdf_by_slug[slug]
        with open(pmeta["raw_json"], "r", encoding="utf-8") as rf:
            raw_pages_data = json.load(rf)
        pages_dir = pmeta["pages_dir"]
        png_files = sorted([
            os.path.join(pages_dir, fn)
            for fn in os.listdir(pages_dir)
            if fn.endswith(".png")
        ])
        ch_pdf_exs = pdf_ex_by_slug.get(slug, [])
        ch_proj_exs = proj_ex_by_slug.get(slug, [])

        # Attach full photo transcriptions for all exercises in this chapter
        ex_photo_details = {}
        for ex in ch_pdf_exs + ch_proj_exs:
            eid = ex["exercise_id"]
            matched_indices = set(
                ex.get("photo_indices", [])
                + ex.get("all_photos", [])
                + ex.get("problem_photos", [])
                + ex.get("solution_photos", [])
                + ex.get("problem_photo_indices", [])
                + ex.get("solution_photo_indices", [])
            )
            ex_photos = [
                ph for ph in photos_all
                if ph.get("index") in matched_indices or ph.get("matched_exercise_id") == eid
            ]
            ex_photo_details[eid] = ex_photos

        payload_chapters.append({
            "slug": slug,
            "pdf_filename": pmeta["pdf_filename"],
            "pdf_path": pmeta["pdf_path"],
            "pdf_sha": pmeta["pdf_sha"],
            "page_count": pmeta["page_count"],
            "pages_dir": pages_dir,
            "page_pngs": png_files,
            "raw_pages": raw_pages_data.get("pages", []),
            "audit_chapter_meta": chapters_audit.get(slug, {}),
            "reconciled_pdf_exercises": ch_pdf_exs,
            "reconciled_projector_exercises": ch_proj_exs,
            "exercise_photo_transcriptions": ex_photo_details,
        })

    out_path = os.path.join(OUT_DIR, "worker_inputs", f"{wid}.json")
    raw_bytes = json.dumps({
        "worker_id": wid,
        "brief_id": "f51e2026",
        "assigned_slugs": slugs,
        "chapters": payload_chapters,
    }, ensure_ascii=False, indent=2).encode("utf-8")
    with open(out_path, "wb") as wf:
        wf.write(raw_bytes)
    sha = hashlib.sha256(raw_bytes).hexdigest()
    summary.append({
        "worker_id": wid,
        "slugs": slugs,
        "input_file": out_path,
        "sha256": sha,
        "pdf_ex_count": sum(len(c["reconciled_pdf_exercises"]) for c in payload_chapters),
        "proj_ex_count": sum(len(c["reconciled_projector_exercises"]) for c in payload_chapters),
    })

with open(os.path.join(OUT_DIR, "wave_plan_summary.json"), "w", encoding="utf-8") as sf:
    json.dump(summary, sf, ensure_ascii=False, indent=2)

for row in summary:
    print(f"{row['worker_id']}: slugs={row['slugs']} | pdf_ex={row['pdf_ex_count']} | proj_ex={row['proj_ex_count']} | sha256={row['sha256'][:12]}")
