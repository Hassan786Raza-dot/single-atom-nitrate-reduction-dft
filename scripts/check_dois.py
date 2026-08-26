#!/usr/bin/python3
from __future__ import annotations
import csv
import json
import time
from pathlib import Path
import requests

src = Path('literature_review/literature_review.csv')
out = Path('literature_review/doi_audit.csv')
rows = []
with src.open(encoding='utf-8', newline='') as handle:
    records = list(csv.DictReader(handle))
for rec in records:
    doi = rec['DOI'].strip()
    url = 'https://api.crossref.org/works/' + doi
    item = {'DOI': doi, 'csv_title': rec['Title'], 'status': 'ERROR', 'crossref_title': '', 'year': '', 'journal': '', 'type': ''}
    try:
        response = requests.get(url, timeout=20, headers={'User-Agent': 'research-audit/1.0 mailto:research@example.org'})
        item['status'] = str(response.status_code)
        if response.ok:
            msg = response.json()['message']
            item['crossref_title'] = ' '.join(msg.get('title', ['']))
            item['year'] = str((msg.get('published-print') or msg.get('published-online') or msg.get('issued', {})).get('date-parts', [['']])[0][0])
            item['journal'] = ' '.join(msg.get('container-title', ['']))
            item['type'] = msg.get('type', '')
    except Exception as exc:
        item['status'] = f'ERROR:{type(exc).__name__}'
    rows.append(item)
    time.sleep(0.2)
with out.open('w', encoding='utf-8', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=rows[0])
    writer.writeheader(); writer.writerows(rows)
print(json.dumps(rows, indent=2))
