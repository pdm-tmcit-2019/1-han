import numpy as np
import json
import pyld
import rdflib
import random
import jsonldParser as jp 

def mydata():
	 jp.loadJsonld('firstMorning.jsonld')
	 charaData = jp.getCharacterData()
	 for x in charaData:
	 	if jp.isMineCharacter(x):
	 		myData = x
	 		break
	 myid = jp.getCharacterId(myData)
	 myid = ''.join(myid)
	 return myid

def writeName(charId, charName_en, charName_ja):

	json_file = open("temp/noonVote_temp.jsonld", 'r', encoding='utf-8')
	json_object = json.load(json_file)

	json_object["character"]["id"] = charId
	json_object["character"]["name"]["en"] = charName_en
	json_object["character"]["name"]["ja"] = charName_ja

	new_json_file = open('jsonld_return/noonVote_return.jsonld', 'w')
	json.dump(json_object, new_json_file, indent=2, ensure_ascii=False)

def main():

	myid = mydata()

	while(1):
		random_id  = str(random.randrange(16))
		if(random_id != myid):
			break


	charId = 'https://licos.online/state/0.3/village#3/character#' + str(random_id)

	charName = jp.getCharacterName(charId)
	charName_en = charName[0]
	charName_ja = charName[1]

	writeName(random_id, charName_en, charName_ja)

	print(charId)
	print(charName_en)
	print(charName_ja)



if __name__ == '__main__':
	main()