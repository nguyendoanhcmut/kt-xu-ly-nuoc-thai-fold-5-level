import os
import json
import subprocess
import sys

BASE_DIR = r"C:\antgravity workplace\hcmut-263\kt xu ly nuoc thai"
AUDIT_DIR = os.path.join(BASE_DIR, "audit_exercise_map_v1")
OUT_DIR = os.path.join(BASE_DIR, "fold_5_level_v1")
EXTRACT_SCRIPT = r"C:\Users\Admin\.gemini\config\skills\branches\scripts\extract_figures.py"

with open(os.path.join(AUDIT_DIR, "raw_inputs_manifest.json"), "r", encoding="utf-8") as f:
    raw_manifest = json.load(f)

for item in raw_manifest["pdfs"]:
    slug = item["slug"]
    pdf_path = item["pdf_path"]
    ch_reader_dir = os.path.join(OUT_DIR, "readers", slug)
    assets_dir = os.path.join(ch_reader_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)
    manifest_out = os.path.join(ch_reader_dir, "figures_manifest.json")
    cmd = [
        sys.executable,
        EXTRACT_SCRIPT,
        pdf_path,
        assets_dir,
        "--manifest",
        manifest_out,
        "--min-size",
        "5120",
        "--min-dim",
        "120",
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    fig_count = 0
    if os.path.exists(manifest_out):
        with open(manifest_out, "r", encoding="utf-8") as mf:
            mdata = json.load(mf)
            fig_count = len(mdata.get("figures", mdata) if isinstance(mdata, dict) else mdata)
    print(f"{slug}: extracted {fig_count} figures (exit={res.returncode})")
