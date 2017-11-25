import os
import sys
from read_answers import *
from parser import *
from id_labler import get_id
from perp_org_labeler import *
from target_labler import *
from victim_labler import *

answer_dictionary = get_answer_dictionary("developset/answers/")
weapons = answer_dictionary['WEAPON']#,'MACHINE-GUN', 'DYNAMITE', 'GRENADES', 'BULLET', 'BOMB', 'BOMBS', 'MACHINEGUNS', 'ROCKET', 'ARTILLERY']

attack = set(["ATTACKED", "ATTACK", "MURDER", "MURDERED", "SHOOTOUT", "SHOTS", "ESPIONAGE", "ASSASSINATION", "ASSASSINATIONS"])
kidnapping = set(["KIDNAPPING", "KIDNAPPED", "KIDNAP", "KIDNAPPERS", "HOSTAGES", "HOSTAGE"])
bombing = set(["DYNAMITE", "BOMBING", "BOMBED", "BLAST", "BOMBS", "EXPLOSIVE", "EXPLOSIVES", "EXPLOSIONS"])
arson = set(["ARSON", "ON FIRE", "BURNING"])
robbery = set(["ROBBED", "ROBBING", "ROBBERY"])

def get_id(document):

    # print text_data_array
    document_array = document.split()
    result = document_array[0]

    return result

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
            if word.lower() in weapons:
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
    pos_documents_array = getPosDocuments(articles)
    parse_documents_array = getParseDocuments(articles)
    articles.pop(0)
    for i in range(len(articles)):
        # pdb.set_trace()
        results += 'ID:\t\t' + str(get_id(articles[i])) + '\n'
        results += 'INCIDENT:\t' + '-\n'#getIncident(article) + '\n'
        results += 'WEAPON:\t\t' + '-\n'#'\n'.join(getWeapon(article)) + '\n'
        results += 'PERP INDIV:\t' +'-\n'# getPerp(article) + '\n'
        results += 'PERP ORG:\t' + '-\n'#get_perp_org(article) + '\n'
        results += 'TARGET:\t\t' + '-\n'#get_target(article) + '\n'
        results += 'VICTIM:\t\t' + get_victim(articles[i],
                                            pos_documents_array[i],
                                            parse_documents_array[i]) + '\n\n'

    f = open(file_name + '.templates', 'w')
    f.write(results)  # python will convert \n to os.linesep
    f.close()

def getPosDocuments(articles):
    articles_text = '\n\n'.join(articles)
    pos_documents_array = posInput(articles_text)
    pos_article = []
    result_document_array = []
    pos_article.append(pos_documents_array[0])
    for i in range(1, len(pos_documents_array)):
        if pos_documents_array[i][0].startswith('DEV-') or pos_documents_array[i][0].startswith('TST1-') or pos_documents_array[i][0].startswith('TST2-'):
            result_document_array.append(pos_article)
            pos_article = []
            pos_article.append(pos_documents_array[i])
        else:
            pos_article.append(pos_documents_array[i])

    result_document_array.append(pos_article)
    return result_document_array

def getParseDocuments(articles):
    articles_text = '\n\n'.join(articles)
    parse_documents_array = parseInput(articles_text)
    parse_article = []
    result_document_array = []
    parse_article.append(parse_documents_array)
    for i in range(1, len(parse_documents_array)):
        if parse_documents_array[i][0].startswith('DEV-') or parse_documents_array[i][0].startswith('TST1-') or parse_documents_array[i][0].startswith('TST2-'):
            result_document_array.append(parse_article)
            parse_article = []
            parse_article.append(parse_documents_array[i])
        else:
            parse_article.append(parse_documents_array[i])
    result_document_array.append(parse_article)
    return result_document_array


if __name__ == '__main__':
    main()
