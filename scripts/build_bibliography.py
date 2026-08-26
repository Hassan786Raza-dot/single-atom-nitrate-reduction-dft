#!/usr/bin/python3
from __future__ import annotations
import csv
from pathlib import Path

src=Path('literature_review/curated_references_validated.csv')
out=Path('references')
out.mkdir(exist_ok=True)
rows=list(csv.DictReader(src.open(encoding='utf-8')))
rows=[r for r in rows if r['status']=='200' and r['year'].isdigit() and int(r['year']) <= 2025]
with (out/'references.md').open('w',encoding='utf-8') as h:
    for i,r in enumerate(rows,1):
        title=r['title'].replace('<i>','').replace('</i>','').replace('<sub>','').replace('</sub>','').replace('&amp;','&').replace('\n',' ')
        h.write(f'[{i}] {r["authors"]}. {title}. *{r["journal"]}* ({r["year"]}). https://doi.org/{r["DOI"]}\n\n')
print(f'written={len(rows)}')
