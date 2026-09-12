#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


def preview(folder: Path, prefix: str = 'item') -> None:
    files = sorted(p for p in folder.iterdir() if p.is_file())
    for index, path in enumerate(files, start=1):
        new_name = f'{prefix}_{index:03d}{path.suffix.lower()}'
        print(f'{path.name} -> {new_name}')
    print('Preview only. No files were changed.')


if __name__ == '__main__':
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    preview(target, sys.argv[2] if len(sys.argv) > 2 else 'item')
