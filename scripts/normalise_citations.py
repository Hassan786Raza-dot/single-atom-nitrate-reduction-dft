#!/usr/bin/python3
from __future__ import annotations
import re
from pathlib import Path

path=Path(__file__).resolve().parents[1]/'manuscript/manuscript.md'
text=path.read_text(encoding='utf-8')
head, refs = text.split('## References',1)

def expand(match: re.Match[str]) -> str:
    body=match.group(1).strip()
    tokens=re.split(r'[,; ]+',body)
    nums=[]
    for token in tokens:
        if not token: continue
        m=re.fullmatch(r'(\d+)[–-](\d+)',token)
        if m: nums.extend(range(int(m.group(1)),int(m.group(2))+1))
        elif token.isdigit(): nums.append(int(token))
        else: return match.group(0)
    return ' '.join(f'[{n}]' for n in nums)

head=re.sub(r'\[([^\[\]]*\d[^\[\]]*)\]',expand,head)
path.write_text(head+'## References'+refs,encoding='utf-8')
print('normalised_main_text_citations')
