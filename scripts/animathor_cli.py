#!/usr/bin/env python3
"""
Animathor Studio Automation CLI
Facilitates project scaffolding, fast draft renders, single-frame previews, and ffmpeg stitching.
"""

import os
import sys
import argparse
import subprocess
import shutil
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = ROOT_DIR / ".agents" / "skills" / "animathor" / "templates"


if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


import datetime


def scaffold_project(project_name: str, vertical: bool = False, title: str | None = None, modular: bool = False):
    """Scaffold a new Animathor animation project using the directory template."""
    target_dir = ROOT_DIR / project_name
    if target_dir.exists():
        print(f"[!] Error: Directory '{project_name}' already exists.")
        return 1

    project_title = title or project_name.replace("_", " ").replace("-", " ").title()
    fmt_name = "vertical" if vertical else "horizontal"
    aspect_ratio = "9:16" if vertical else "16:9"
    width = 1080 if vertical else 1920
    height = 1920 if vertical else 1080
    date_str = datetime.date.today().isoformat()

    print(f"[*] Scaffolding Animathor project: {project_name}")
    print(f"    Title: {project_title}")
    print(f"    Format: {fmt_name} ({aspect_ratio}, {width}x{height})")

    # 1. Create directory structure
    for sub in ["assets/audio", "assets/images", "assets/svgs", "output"]:
        (target_dir / sub).mkdir(parents=True, exist_ok=True)
        gitkeep = target_dir / sub / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.write_text(f"# {sub}\n", encoding="utf-8")
        print(f"  [+] Directory: {project_name}/{sub}")

    # 2. animathor.json metadata
    metadata_tpl = (TEMPLATES_DIR / "project_template" / "animathor.json").read_text(encoding="utf-8")
    metadata_content = (
        metadata_tpl.replace("{{PROJECT_NAME}}", project_name)
        .replace("{{PROJECT_TITLE}}", project_title)
        .replace("{{FORMAT}}", fmt_name)
        .replace("{{ASPECT_RATIO}}", aspect_ratio)
        .replace("{{WIDTH}}", str(width))
        .replace("{{HEIGHT}}", str(height))
        .replace("{{DATE}}", date_str)
    )
    (target_dir / "animathor.json").write_text(metadata_content, encoding="utf-8")
    print(f"  [+] Created: {project_name}/animathor.json")

    # 3. manim.cfg
    cfg_src = "manim_vertical.cfg" if vertical else "manim_horizontal.cfg"
    cfg_content = (TEMPLATES_DIR / "project_template" / cfg_src).read_text(encoding="utf-8")
    (target_dir / "manim.cfg").write_text(cfg_content, encoding="utf-8")
    print(f"  [+] Created: {project_name}/manim.cfg (from {cfg_src})")

    # 4. storyboard.md
    sb_tpl = (TEMPLATES_DIR / "storyboard_template.md").read_text(encoding="utf-8")
    sb_content = sb_tpl.replace("[Judul Video / Video Title]", project_title)
    (target_dir / "storyboard.md").write_text(sb_content, encoding="utf-8")
    print(f"  [+] Created: {project_name}/storyboard.md")

    # 5. script.py
    script_src = "vertical_shorts_ce.py" if vertical else "horizontal_explainer_ce.py"
    script_content = (TEMPLATES_DIR / script_src).read_text(encoding="utf-8")
    (target_dir / "script.py").write_text(script_content, encoding="utf-8")
    print(f"  [+] Created: {project_name}/script.py (from {script_src})")

    # 6. README.md
    readme_tpl = (TEMPLATES_DIR / "project_template" / "README.md").read_text(encoding="utf-8")
    readme_content = readme_tpl.replace("{{PROJECT_TITLE}}", project_title).replace("{{PROJECT_NAME}}", project_name)
    (target_dir / "README.md").write_text(readme_content, encoding="utf-8")
    print(f"  [+] Created: {project_name}/README.md")

    # 7. Optional modular scenes
    if modular:
        scenes_dir = target_dir / "scenes"
        scenes_dir.mkdir(exist_ok=True)
        (scenes_dir / "__init__.py").write_text("# Modular scenes package\n", encoding="utf-8")
        print(f"  [+] Created: {project_name}/scenes/ modular directory")

    print(f"\n[+] Project '{project_name}' successfully scaffolded with standard directory template!")
    print(f"    Next steps:")
    print(f"    1. Open {project_name}/storyboard.md and refine your AV scene beats.")
    print(f"    2. Audit: python scripts/animathor_cli.py lint {project_name}/storyboard.md")
    print(f"    3. Code: Edit {project_name}/script.py")
    print(f"    4. Draft: python scripts/animathor_cli.py draft {project_name}/script.py")
    return 0


def run_manim(cmd_args: list[str]):
    """Execute manim command."""
    print(f"[*] Executing: {' '.join(cmd_args)}")
    try:
        proc = subprocess.run(cmd_args)
        return proc.returncode
    except FileNotFoundError:
        print("[!] Error: 'manim' CLI command not found. Ensure Manim is installed (pip install manim).")
        return 1


def draft_render(script_path: str, scenes: list[str]):
    """Fast render at 480p15 (-ql)."""
    cmd = ["manim", "-ql", script_path] + scenes
    return run_manim(cmd)


def preview_frame(script_path: str, scene: str):
    """Preview a single freeze frame as PNG (-s -ql)."""
    cmd = ["manim", "-s", "-ql", script_path, scene]
    return run_manim(cmd)


def production_render(script_path: str, scenes: list[str]):
    """Production render at 1080p60 (-qh)."""
    cmd = ["manim", "-qh", script_path] + scenes
    return run_manim(cmd)


def stitch_scenes(script_path: str, quality_folder: str = "1080p60"):
    """Auto-detect exported scene videos and stitch them using ffmpeg."""
    script_p = Path(script_path).resolve()
    script_stem = script_p.stem

    media_dir = script_p.parent / "media" / "videos" / script_stem / quality_folder
    if not media_dir.exists():
        # Fallback search
        candidate_dirs = list((script_p.parent / "media" / "videos" / script_stem).glob("*"))
        if candidate_dirs:
            media_dir = candidate_dirs[0]
        else:
            print(f"[!] Error: No rendered videos found in {script_p.parent / 'media' / 'videos' / script_stem}")
            return 1

    mp4_files = sorted(list(media_dir.glob("*.mp4")))
    if not mp4_files:
        print(f"[!] Error: No .mp4 files found in {media_dir}")
        return 1

    print(f"[*] Found {len(mp4_files)} scenes to stitch in {media_dir}:")
    concat_file = script_p.parent / "concat.txt"
    with open(concat_file, "w", encoding="utf-8") as f:
        for mp4 in mp4_files:
            print(f"  - {mp4.name}")
            f.write(f"file '{mp4.as_posix()}'\n")

    out_dir = script_p.parent / "output"
    final_output = out_dir / "final.mp4" if out_dir.exists() else script_p.parent / "final.mp4"
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(concat_file),
        "-c", "copy",
        str(final_output)
    ]

    print(f"[*] Running ffmpeg concatenation...")
    try:
        proc = subprocess.run(ffmpeg_cmd)
        if proc.returncode == 0:
            print(f"\n[+] Successfully stitched video: {final_output}")
            return 0
        return proc.returncode
    except FileNotFoundError:
        print("[!] Error: ffmpeg is not installed or not in PATH.")
        return 1


def main():
    parser = argparse.ArgumentParser(description="Animathor Studio Automation CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # new
    new_parser = subparsers.add_parser("new", help="Scaffold a new animation project with standard directory template")
    new_parser.add_argument("name", help="Project directory name")
    new_parser.add_argument("--vertical", action="store_true", help="Scaffold a 9:16 vertical short project (default: horizontal)")
    new_parser.add_argument("--horizontal", action="store_true", help="Scaffold a 16:9 widescreen project")
    new_parser.add_argument("--title", help="Human-readable project title")
    new_parser.add_argument("--modular", action="store_true", help="Create modular scenes/ directory")

    # draft
    draft_parser = subparsers.add_parser("draft", help="Fast draft render (-ql 480p15)")
    draft_parser.add_argument("script", help="Path to Python scene script")
    draft_parser.add_argument("scenes", nargs="*", help="Specific scene class names (optional)")

    # preview
    preview_parser = subparsers.add_parser("preview", help="Render single freeze frame as PNG (-s)")
    preview_parser.add_argument("script", help="Path to Python scene script")
    preview_parser.add_argument("scene", help="Scene class name to preview")

    # render
    render_parser = subparsers.add_parser("render", help="Production high-res render (-qh 1080p60)")
    render_parser.add_argument("script", help="Path to Python scene script")
    render_parser.add_argument("scenes", nargs="*", help="Specific scene class names (optional)")

    # stitch
    stitch_parser = subparsers.add_parser("stitch", help="Concatenate rendered scene videos with ffmpeg")
    stitch_parser.add_argument("script", help="Path to Python scene script")
    stitch_parser.add_argument("--quality", default="1080p60", help="Quality folder name (e.g. 1080p60, 480p15)")

    # lint (Anti-Slop & Accuracy Quality Audit)
    lint_parser = subparsers.add_parser("lint", help="Audit storyboard or script against Anti-Slop & Accuracy standards")
    lint_parser.add_argument("file", help="Path to storyboard markdown or python script")
    lint_parser.add_argument("--json", action="store_true", help="Output findings in structured JSON format")

    args = parser.parse_args()

    if args.command == "new":
        sys.exit(scaffold_project(args.name, vertical=args.vertical, title=args.title, modular=args.modular))
    elif args.command == "draft":
        sys.exit(draft_render(args.script, args.scenes))
    elif args.command == "preview":
        sys.exit(preview_frame(args.script, args.scene))
    elif args.command == "render":
        sys.exit(production_render(args.script, args.scenes))
    elif args.command == "stitch":
        sys.exit(stitch_scenes(args.script, args.quality))
    elif args.command == "lint":
        from validate_script import ScriptValidator
        validator = ScriptValidator(args.file, json_mode=args.json)
        sys.exit(0 if validator.audit() else 1)


if __name__ == "__main__":
    main()
