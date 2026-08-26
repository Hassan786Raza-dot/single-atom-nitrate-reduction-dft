#!/usr/bin/python3
from __future__ import annotations
import csv
import re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
md=(root/'manuscript/manuscript.md').read_text(encoding='utf-8')
words=len(re.findall(r"\b[\w’'-]+\b", md))
refs=re.findall(r'^\[(\d+)\] ',md,re.M)
assert words >= 3500, words
assert len(refs) >= 25 and len(refs) <= 30, len(refs)
assert len(refs)==len(set(refs)), 'duplicate reference numbers'
assert (root/'figures/final/convergence_benchmark.png').exists()
assert 'figures/final/convergence_benchmark.png' in md
conv=list(csv.DictReader((root/'data/convergence/convergence.csv').open(encoding='utf-8')))
assert len(conv)==11, len(conv)
for p, n in [('data/geometry_audit.txt',36),('data/adsorbate_geometry_audit.txt',60)]:
    text=(root/p).read_text(encoding='utf-8')
    assert re.search(r'failures=0', text), p
    assert re.search(rf'checked={n}\b', text), p
validated=list(csv.DictReader((root/'literature_review/curated_references_validated.csv').open(encoding='utf-8')))
valid={r['DOI'] for r in validated if r['status']=='200'}
for doi in re.findall(r'https://doi\.org/([^\s)]+)', md):
    assert doi in valid, doi
print('FINAL_AUDIT_PASS')
print('word_count',words)
print('reference_count',len(refs))
print('convergence_rows',len(conv))
print('validated_doi_links',len(re.findall(r'https://doi\.org/([^\s)]+)', md)))
