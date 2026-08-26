#!/usr/bin/python3
from __future__ import annotations
import csv
import re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
md=(root/'manuscript/manuscript.md').read_text(encoding='utf-8')
dois=re.findall(r'https://doi\.org/([^\s)]+)',md)
meta={r['DOI']:r for r in csv.DictReader((root/'literature_review/curated_references_validated.csv').open(encoding='utf-8'))}
assert len(dois)==25 and len(set(dois))==25
out=root/'references/manuscript_references.md'
with out.open('w',encoding='utf-8') as h:
    for i,doi in enumerate(dois,1):
        r=meta[doi]
        title=r['title'].replace('<i>','').replace('</i>','').replace('<sub>','').replace('</sub>','').replace('&amp;','&').replace('\n',' ')
        h.write(f'[{i}] {r["authors"]}. {title}. *{r["journal"]}* ({r["year"]}). https://doi.org/{doi}\n\n')
print('synchronised',len(dois),'references')
