#!/usr/bin/python3
from __future__ import annotations
import requests
from pathlib import Path

queries = [
    'nitrate electroreduction ammonia DFT',
    'single atom catalyst nitrate reduction',
    'computational hydrogen electrode electrocatalysis',
    'implicit solvation electrochemical DFT',
    'single atom catalysts two dimensional materials review',
    'microkinetic modelling electrocatalysis DFT',
    'reproducibility computational chemistry data code',
]
lines=[]
for q in queries:
    data=requests.get('https://api.crossref.org/works',params={'query.bibliographic':q,'rows':10,'select':'DOI,title,author,published,container-title,type'},headers={'User-Agent':'research-audit/1.0 mailto:research@example.org'},timeout=30).json()['message']['items']
    lines.append(f'## {q}')
    for item in data:
        title=' '.join(item.get('title',[''])).replace('\n',' ')
        journal=' '.join(item.get('container-title',['']))
        year=(item.get('published',{}).get('date-parts') or [['']])[0][0]
        doi=item.get('DOI','')
        lines.append(f'{year}\t{doi}\t{journal}\t{title}')
    lines.append('')
Path('literature_review/crossref_candidates.tsv').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('wrote literature_review/crossref_candidates.tsv')
