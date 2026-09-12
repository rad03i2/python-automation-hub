#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path


def report(path: Path) -> None:
    with path.open(newline='', encoding='utf-8') as file:
        rows = list(csv.DictReader(file))
    print(f'CSV report for {path.name}')
    print(f'Rows: {len(rows)}')
    print(f'Columns: {", ".join(rows[0].keys()) if rows else "none"}')


if __name__ == '__main__':
    report(Path(sys.argv[1]))
