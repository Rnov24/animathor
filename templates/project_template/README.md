# {{PROJECT_TITLE}}

Project standard Animathor directory structure.

## Folder Organization

```
{{PROJECT_NAME}}/
├── animathor.json     # Project metadata and configuration
├── manim.cfg          # Local Manim engine settings (resolution, fps, theme)
├── storyboard.md      # Mathematical pre-flight audit & Two-Column AV Script
├── script.py          # Manim Python animation script
├── assets/            # Project source assets
│   ├── audio/         # Voiceovers (.mp3), sound effects, background music
│   ├── images/        # Bitmaps, reference diagrams (.png, .jpg)
│   └── svgs/          # Vector icons, custom shapes (.svg)
└── output/            # Exported master video files and final renders
```

## Production Workflow

1. **Verify Storyboard**:
   Edit `storyboard.md` to define narrative beats and check accuracy.
   ```powershell
   python ../scripts/animathor_cli.py lint storyboard.md
   ```

2. **Draft Preview**:
   ```powershell
   python ../scripts/animathor_cli.py draft script.py
   ```

3. **Production Render & Stitching**:
   ```powershell
   python ../scripts/animathor_cli.py render script.py
   python ../scripts/animathor_cli.py stitch script.py
   ```
