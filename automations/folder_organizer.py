#!/usr/bin/env python3
from __future__ import annotations

import shutil
import sys
from pathlib import Path

GROUPS = {
    'images': {'.png', '.jpg', '.jpeg', '.gif', '.webp'},
    'documents': {'.pdf', '.docx', '.txt', '.xlsx', '.pptx'},
    'code': {'.py', '.js', '.html', '.css', '.cs', '.cpp', '.java'},
    'archives': {'.zip', '.rar', '.7z'}
}


def group_for(path: Path) -> str:
    ext = path.suffix.lower()
    for group, extensions in GROUPS.items():
        if ext in extensions:
            return group
    return 'others'


def organize(folder: Path, apply: bool = False) -> None:
    for file in sorted(p for p in folder.iterdir() if p.is_file()):
        target = folder / group_for(file) / file.name
        print(f'{file.name} -> {target.relative_to(folder)}')
        if apply:
            target.parent.mkdir(exist_ok=True)
            shutil.move(str(file), str(target))


if __name__ == '__main__':
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    organize(folder, '--apply' in sys.argv)
