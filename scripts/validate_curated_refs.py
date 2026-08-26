#!/usr/bin/python3
from __future__ import annotations
import csv
import time
from pathlib import Path
import requests

src=Path('literature_review/curated_references_draft.csv')
out=Path('literature_review/curated_references_validated.csv')
rows=[]
with src.open(encoding='utf-8',newline='') as h:
    for rec in csv.DictReader(h):
        doi=rec['DOI']
        item={'DOI':doi,'topic':rec['topic'],'status':'ERROR','title':'','journal':'','year':'','authors':''}
        try:
            r=requests.get('https://api.crossref.org/works/'+doi,headers={'User-Agent':'research-audit/1.0 mailto:research@example.org'},timeout=30)
            item['status']=str(r.status_code)
            if r.ok:
                m=r.json()['message']
                item['title']=' '.join(m.get('title',[''])).replace('\n',' ')
                item['journal']=' '.join(m.get('container-title',['']))
                item['year']=str((m.get('published',{}).get('date-parts') or [['']])[0][0])
                item['authors']='; '.join(' '.join(filter(None,[a.get('family',''),a.get('given','')])) for a in m.get('author',[])[:4])
        except Exception as e:
            item['status']='ERROR:'+type(e).__name__
        rows.append(item); time.sleep(.2)
with out.open('w',encoding='utf-8',newline='') as h:
    w=csv.DictWriter(h,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
print('validated',len(rows),'references')
for r in rows: print(r['status'],r['DOI'],r['year'],r['journal'],r['title'])
