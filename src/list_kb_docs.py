import json

with open('data/enterprise_regulatory_kb.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

docs = data.get('documents', [])
print(f"Total documents: {len(docs)}")
for i, d in enumerate(docs):
    m = d.get('metadata', {})
    vol = m.get('physical_volume', m.get('jurisdiction', ''))
    print(f"{i+1:02d}. [{vol}] {d.get('doc_id')}: {d.get('title')}")
