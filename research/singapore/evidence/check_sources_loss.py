import json
old=json.load(open('research/singapore/evidence/city.pre-r8.json'))
new=json.load(open('research/singapore/city/city.json'))
new_urls={x['url'] for x in new['sources_consulted']}
dropped={x.get('url') for x in old.get('sources_consulted') or [] if x.get('url') and x.get('url') not in new_urls}
print('dropped',len(dropped))
blob=json.dumps({k:v for k,v in new.items() if k!='sources_consulted'})
cited=[u for u in dropped if u in blob]
print('still cited outside sources ledger:',len(cited))
for u in cited[:10]: print(' ',u)
gap=[g for g in new['declared_gaps'] if g['kind']=='sources-replaced']
print('gap', gap[0]['text'][:200] if gap else None)
print('gaps',len(new['declared_gaps']))
