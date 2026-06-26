import shutil
import argparse
from pathlib import Path

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".wmv", ".webm", ".mpeg", ".3gp"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Documents": [".pdf", ".doc", ".docx", ".odt", ".rtf", ".txt", ".md", ".tex"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"],
    "Archives": [".zip", ".tar", ".gz", ".xz", ".7z", ".rar", ".iso"],
    "Code": [
        ".py",
        ".js",
        ".ts",
        ".html",
        ".css",
        ".java",
        ".c",
        ".cpp",
        ".rs",
        ".go",
        ".rb",
        ".php",
        ".sh",
        ".bat",
        ".json",
        ".xml",
        ".toml",
        ".sql",
    ],
    "Executables": [".exe", ".msi", ".apk", ".deb", ".rpm"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Torrents": [".torrent"],
}

EXT_MAP = {ext: cat for cat, exts in CATEGORIES.items() for ext in exts}


def organize(downloads: Path):
    if not downloads.is_dir():
        print(f"Error: '{downloads}' is not a valid directory.")
        return

    files = [f for f in downloads.iterdir() if f.is_file()]
    print(f"Scanning: {downloads}")
    print(f"Found {len(files)} file(s)\n")

    moved = 0
    for src in files:
        category = EXT_MAP.get(src.suffix.lower(), "Others")
        dest_dir = downloads / category
        dest = dest_dir / src.name

        if dest.exists():
            continue

        dest_dir.mkdir(exist_ok=True)
        shutil.move(str(src), str(dest))
        moved += 1
        print(f"Moved: {src.name} -> {category}/")

    print(f"\nDone. Moved {moved} file(s).")


def main():
    parser = argparse.ArgumentParser(description="Organise Downloads folder.")
    parser.add_argument(
        "path",
        nargs="?",
        default=str(Path.home() / "Downloads"),
        help="Folder to organise",
    )
    args = parser.parse_args()
    organize(Path(args.path))


if __name__ == "__main__":
    main()
