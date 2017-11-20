import os
import sys
from read_answers import *
from id_labler import get_id
from perp_org_labeler import *
from target_labler import *
from victim_labler import *

answer_dictionary = get_answer_dictionary("developset/answers/")
weapons = answer_dictionary['WEAPON']

attack = set(["ATTACKED", "ATTACK", "MURDER", "MURDERED", "SHOOTOUT", "SHOTS", "ESPIONAGE", "ASSASSINATION", "ASSASSINATIONS"])
kidnapping = set(["KIDNAPPING", "KIDNAPPED", "KIDNAP", "KIDNAPPERS", "HOSTAGES", "HOSTAGE"])
bombing = set(["DYNAMITE", "BOMBING", "BOMBED", "BLAST", "BOMBS", "EXPLOSIVE", "EXPLOSIVES", "EXPLOSIONS"])
arson = set(["ARSON", "ON FIRE", "BURNING"])
robbery = set(["ROBBED", "ROBBING", "ROBBERY"])

# def get_id(document):
#
#     # print text_data_array
#     document_array = document.split()
#     result = 'DEV-' + document_array[0]
#
#     print result

def getIncident(article):
    if any (word in article for word in kidnapping):
        return "KIDNAPPING"
    elif any (word in article for word in arson):
        return "ARSON"
    elif any (word in article for word in attack):
        return "ATTACK"
    elif any (word in article for word in bombing):
        return "BOMBING"
    # elif any (word in article for word in robbery):
    # 	return "ROBBERY"
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

def main():
    file_name = sys.argv[1]
    results = ""
    print("\n" + file_name + "\n")
    text = ""
    input_file = open(file_name, "r")
    articles = []
    for line in input_file:
        if line.startswith('DEV-') or line.startswith('TST1-') or line.startswith('TST2-'):
            articles.append(text)
            text = ""
        text += line

    articles.append(text)

    for article in articles:
        if len(article.strip()) > 0:
            # pdb.set_trace()
            results += 'ID:\t' + get_id(article) + '\n'
            results += 'INCIDENT:\t' + getIncident(article) + '\n'
            results += 'WEAPON:\t' + '\n'.join(getWeapon(article)) + '\n'
            results += 'PERP INDIV:\t' + getPerp(article) + '\n'
            results += 'PERP ORG:\t' + get_perp_org(article) + '\n'
            results += 'TARGET:\t' + get_target(article) + '\n'
            results += 'VICTIM:\t' + get_victim(article) + '\n\n'

    f = open(file_name + '_templates', 'w')
    f.write(results)  # python will convert \n to os.linesep
    f.close()



if __name__ == '__main__':
    main()
