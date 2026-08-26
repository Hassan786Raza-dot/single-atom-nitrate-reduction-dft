#!/usr/bin/python3
from __future__ import annotations
import re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
md=(root/'manuscript/manuscript.md').read_text(encoding='utf-8')
main=md.split('## References',1)[0]
abstract=main.split('## 1. Introduction',1)[0]
# Parse numeric citations only from the main text; expand ranges such as [1–5].
all_cites=[]
for group in re.findall(r'\[([^\]]+)\]',main):
    for token in re.split(r'[,; ]+', group.strip()):
        token=token.strip()
        if not token: continue
        m=re.fullmatch(r'(\d+)[–-](\d+)',token)
        if m: all_cites.extend(range(int(m.group(1)),int(m.group(2))+1))
        elif token.isdigit(): all_cites.append(int(token))
refs={int(n) for n in re.findall(r'^\[(\d+)\] ',md,re.M)}
used=set(all_cites)
uncited=sorted(refs-used)
missing=sorted(used-refs)
abstract_cites=sorted({int(n) for group in re.findall(r'\[([^\]]+)\]',abstract) for n in re.findall(r'\d+',group)})
# The manuscript uses a single data figure and numbered display equations.
figure_mentions=len(re.findall(r'\b[Ff]igure 1\b',main))
table_mentions=len(re.findall(r'\b[Tt]able [1-9][0-9]*\b',main))
equation_mentions=len(re.findall(r'\b[Ee]quation[s]?\b',main))
si_mentions=len(re.findall(r'\bSupporting Information\b',main))
print('abstract_citations=',abstract_cites)
print('references=',len(refs),'used=',len(used),'uncited=',uncited,'missing=',missing)
print('figure_mentions=',figure_mentions,'table_mentions=',table_mentions,'equation_mentions=',equation_mentions,'supporting_information_mentions=',si_mentions)
print('used_reference_numbers=',sorted(used))
assert not abstract_cites, abstract_cites
assert len(refs) >= 20 and len(refs) <= 30, len(refs)
assert not uncited, uncited
assert not missing, missing
assert refs == set(range(1,len(refs)+1)), sorted(refs)
assert figure_mentions >= 1
assert table_mentions >= 5
for label in ['Table 1','Table 2','Table 3','Table 4','Table 5']:
    assert label in main, label
assert equation_mentions >= 1
assert si_mentions >= 1
print('CITATION_CROSSREF_AUDIT_PASS')
