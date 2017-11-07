import os
from read_answers import *

answer_dictionary = get_answer_dictionary("developset/answers/")
weapons = answer_dictionary['WEAPON']

attack = set(["ATTACKED", "ATTACK", "MURDER", "MURDERED", "SHOOTOUT", "SHOTS", "ESPIONAGE", "ASSASSINATION", "ASSASSINATIONS"])
kidnapping = set(["KIDNAPPING", "KIDNAPPED", "KIDNAP", "KIDNAPPERS", "HOSTAGES", "HOSTAGE"])
bombing = set(["DYNAMITE", "BOMBING", "BOMBED", "BLAST", "BOMBS", "EXPLOSIVE", "EXPLOSIVES", "EXPLOSIONS"])
arson = set(["ARSON", "ON FIRE", "BURNING"])
robbery = set(["ROBBED", "ROBBING", "ROBBERY"])

def getIncident(article):
    if any (word in article for word in kidnapping):
        return "KIDNAPPING"
    elif any (word in article for word in arson):
        return "ARSON"
    elif any (word in article for word in attack):
        return "ATTACK"
    elif any (word in article for word in bombing):
        return "BOMBING"
    elif any (word in article for word in robbery):
    	return "ROBBERY"
    else :
        return "ATTACK"

def getWeapon(article):
    weaponsList = set()
    for word in article.split():
        word = word.strip()
        if len(word) > 0:
            if word in weapons:
                weaponsList.add(word)
    if len(weaponsList) == 0:
        weaponsList.add("-")
    return weaponsList

def getPerp(article):
	return "-"

directory = "./developset/texts/"
for filename in os.listdir(directory):
	print("\n" + filename + "\n")
	text = ""
	fileName = directory + filename
	input_file = open(fileName, "r")
	for line in input_file:
		text += line
		articles = text.split("DEV-")

	for article in articles:
		if len(article.strip()) > 0:
			print(getIncident(article))
			print(getWeapon(article))