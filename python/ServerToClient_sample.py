import os
import json
import pyld
import rdflib
import requests

g = rdflib.Graph()

def reqJsonld():
    expanded = pyld.jsonld.expand(
        'https://werewolf.world/village/example/0.3/server2client/myMessageOnChat.jsonld')
    jsonData = json.dumps(expanded, indent=2, ensure_ascii=False)
#    print(jsonData)
    jsonld = json.loads(jsonData)[0]
    normalized = pyld.jsonld.normalize(
        jsonld, {'algorithm': 'URDNA2015', 'format': 'application/nquads'})
    g.parse(data=normalized, format='n3')

# Character Info Function
def getCharacters():
    sparql = """
        prefix ns1: <https://werewolf.world/resource/0.3/>
        prefix ns2: <https://licos.online/state/0.3/village#3/>
        SELECT * WHERE {
            ns2:systemMessage ns1:character ?o.
        }
    """
    result = g.query(sparql).serialize(format='csv').decode('utf-8')
    characterList = result.split('\r\n')
    characterList.remove('o')
    characterList.remove('')

    return characterList

def getCharacterIsMine(characterList):
    sparql = """
        prefix ns1: <https://werewolf.world/resource/0.3/>
        select ?isMine where { 
            ?class ns1:characterIsMine ?isMine
        }
    """
    for element in characterList:
        result = g.query(sparql, initBindings={'class': rdflib.URIRef(element)}).serialize(format='csv').decode('utf-8')
        isMainList = result.split('\r\n')
        isMainList.remove('isMine')
        isMainList.remove('')
        if(isMainList[0] == 'true'):
            break;
            
    return element

def getCharacterName(element):
    sparql = """
        prefix ns1: <https://werewolf.world/resource/0.3/>
        prefix ns2: <https://licos.online/state/0.3/village#3/>    
        select ?name where { 
            ?class ns1:characterName ?name
        }"""

    q = g.query(sparql, initBindings={'class': rdflib.URIRef(element)}).serialize(format='csv').decode('utf-8')
    name = q.split('\r\n');
    name.remove('name')
    name.remove('')
    name = {
        "en":name[0],
        "ja":name[1]
    }
    
    return name

# Role Info Function
def getRoles():
    sparql = """
        prefix ns1: <https://werewolf.world/resource/0.3/>
        prefix ns2: <https://licos.online/state/0.3/village#3/>
        SELECT * WHERE {
            ns2:systemMessage ns1:role ?o.
        }
    """
    result = g.query(sparql).serialize(format='csv').decode('utf-8')
    roleList = result.split('\r\n')
    roleList.remove('o')
    roleList.remove('')

    return roleList    
    
def getRoleIsMine(roleList):
    sparql = """
        prefix ns1: <https://werewolf.world/resource/0.3/>
        select ?isMine where { 
            ?class ns1:roleIsMine ?isMine
        }
    """
    for element in roleList:
        result = g.query(sparql, initBindings={'class': rdflib.URIRef(element)}).serialize(format='csv').decode('utf-8')
        isMainList = result.split('\r\n')
        isMainList.remove('isMine')
        isMainList.remove('')
        if(isMainList[0] == 'true'):
            break;
            
    return element

def getRoleName(element):
    sparql = """
        prefix ns1: <https://werewolf.world/resource/0.3/>
        prefix ns2: <https://licos.online/state/0.3/village#3/>    
        select ?name where { 
            ?class ns1:roleName ?name
        }"""

    q = g.query(sparql, initBindings={'class': rdflib.URIRef(element)}).serialize(format='csv').decode('utf-8')
    name = q.split('\r\n');
    name.remove('name')
    name.remove('')
    name = {
        "en":name[1],
        "ja":name[0]
    }
    
    return name

def getRoleBoard(element):
    sparql = """
        prefix ns1: <https://werewolf.world/resource/0.3/>
        prefix ns2: <https://licos.online/state/0.3/village#3/>    
        select ?character where { 
            ?class ns1:board ?character
        }"""

    q = g.query(sparql, initBindings={'class': rdflib.URIRef(element)}).serialize(format='csv').decode('utf-8')
    elements = q.split('\r\n');
    elements.remove('character')
    elements.remove('')

    sparql = """
        prefix ns1: <https://werewolf.world/resource/0.3/>
        prefix ns2: <https://licos.online/state/0.3/village#3/>    
        select ?character where { 
            ?class ns1:character ?character
        }"""

    characters = []
    for element in elements:
        result = g.query(sparql, initBindings={'class': rdflib.URIRef(element)}).serialize(format='csv').decode('utf-8')
        character = result.split('\r\n')
        character.remove('character')
        character.remove('')
        characters.append(character[0])

    return characters

def getRoleNumberOfPlayers(element):
    sparql = """
        prefix ns1: <https://werewolf.world/resource/0.3/>
        prefix ns2: <https://licos.online/state/0.3/village#3/>    
        select ?num where { 
            ?class ns1:numberOfPlayersWhoPlayTheRole ?num
        }"""

    q = g.query(sparql, initBindings={'class': rdflib.URIRef(element)}).serialize(format='csv').decode('utf-8')
    num = q.split('\r\n');
    num.remove('num')
    num.remove('')
    
    return num

# ChatMessage Info Function
def getChatIsMine():
    sparql = """
        prefix ns1: <https://werewolf.world/resource/0.3/>
        prefix ns2: <https://licos.online/state/0.3/village#3/>
        SELECT * WHERE {
            ns2:chatMessage ns1:chatIsMine ?o.
        }
    """
    result = g.query(sparql).serialize(format='csv').decode('utf-8')
    isMine = result.split('\r\n')
    isMine.remove('o')
    isMine.remove('')

    return isMine

def getChatText():
    sparql = """
        prefix ns1: <https://werewolf.world/resource/0.3/>
        prefix ns2: <https://licos.online/state/0.3/village#3/>
        SELECT * WHERE {
            ns2:chatMessage ns1:chatText ?o.
        }
    """
    result = g.query(sparql).serialize(format='csv').decode('utf-8')
    text = result.split('\r\n')
    text.remove('o')
    text.remove('')

    return text


# main
def main():
###
#    reqJsonld()
#    characters = getCharacters()
#    print(getCharacterName(getCharacterIsMine(characters)))
#    print(getRoleName(getRoleIsMine(getRoles())))
#    for element in getRoleBoard(getRoleIsMine(getRoles())):
#        print(getCharacterName(element))
#    print(getRoleNumberOfPlayers(getRoleIsMine(getRoles())))
###  
    reqJsonld()
    print(getChatIsMine())
    print(getChatText())

if __name__ == "__main__":
    main()
