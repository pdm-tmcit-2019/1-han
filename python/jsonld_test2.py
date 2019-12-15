import os
import json
import pyld
import rdflib
import requests

expanded = pyld.jsonld.expand('https://werewolf.world/village/example/0.3/server2client/firstMorning.jsonld')
jsonData = json.dumps(expanded, indent=2, ensure_ascii=False)
jsonld = json.loads(jsonData)[0]
normalized = pyld.jsonld.normalize(jsonld, {'algorithm': 'URDNA2015', 'format': 'application/nquads'})


print(jsonData)
g = rdflib.Graph()
g.parse(data=normalized, format='n3')
sparql = """
    prefix ns1: <https://werewolf.world/resource/0.3/>
    prefix ns2: <https://licos.online/state/0.3/village#3/>
    SELECT * WHERE {
        ns2:systemMessage ns1:character ?o.
    }
"""
text = g.query(sparql).serialize(format='csv').decode('utf-8')
textArray = text.split('\r\n')
textArray.remove('o')
textArray.remove('')

print(textArray)

sparql = """
    prefix ns1: <https://werewolf.world/resource/0.3/>
    prefix ns2: <https://licos.online/state/0.3/village#3/>    
    select ?name where { 
        ?class ns1:characterName ?name
    }"""

for element in textArray:
    print(element)
    q = g.query(sparql, initBindings={'class': rdflib.URIRef(element)})
    test = q.serialize(format='csv')
    print(test.decode('utf-8'))

#print(len(textArray))