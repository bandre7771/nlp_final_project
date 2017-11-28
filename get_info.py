import os
import sys
from read_answers import *
from parser import *
from id_labler import get_id
from perp_org_labeler import *
from target_labler import *
from victim_labler import *

answer_dictionary = get_answer_dictionary("developset/answers/")
# answer_dictionary2 = get_answer_dictionary('developset/testset1/answerkeys/')
# answer_dictionary3 = answer_dictionary.copy().update(answer_dictionary2)#,'MACHINE-GUN', 'DYNAMITE', 'GRENADES', 'BULLET', 'BOMB', 'BOMBS', 'MACHINEGUNS', 'ROCKET', 'ARTILLERY']
weapons = answer_dictionary2['WEAPON']
# weapons2 = answer_dictionary['WEAPON']

definitely_attack = set(['CROSSFIRE','VIOLENT ATTACK', 'VIOLENT\nATTACK', 'MACHINEGUNNED',
                        'ATTACKS ON', 'CLASHES', 'DOWND', 'KILLING OF', 'DEMOBILIZATION', 'MURDER PERPETRATED'])
definitely_kidnapping = set([])
definitely_bombing = set(['DYNAMITE', 'BOMB EXPLOSION', 'BOMB\nEXPLOSION',
                            'DETONATED', 'SET OFF BOMBS', 'SET\nOFF BOMBS', 'SET OFF\nBOMBS',
                            'THE BLAST', 'THE\nBLAST', 'OF BOMBING', 'OF\nBOMBING',
                            'EXPLODED', 'A BOMB', 'A\nBOMB', 'WITH GRENADES', 'WITH\nGRENADES',
                            'BOMB WAS PLACED', 'BOMB ATTACK', 'CAR BOMB', 'CAR\nBOMB',
                            'BLOWING-UP'])
definitely_arson = set(['A FIRE', 'A\nFIRE', 'SET FIRE', 'SET\nFIRE', 'PLACES BURNED'])
definitely_robbery = set([])

higher_weapons = set(['DYNAMITE CHARGE','CHARGE OF DYNAMITE', 'ROCKET', 'HELICOPTER GUNSHIPS','C-47 AIRCRAFT', 'ARTILLERY'])
weapons = set(['DYNAMITE', 'GRENADES', 'BOMB', 'BOMB', 'EXPLOSIVE DEVICES','BULLET', 'EXPLOSIVE CHARGES',])

attack = set(["ATTACKED","ATTACK", "MURDER", "MURDERED", "SHOOTOUT", "SHOTS", "ESPIONAGE", "ASSASSINATION", "ASSASSINATIONS"])
kidnapping = set(["KIDNAPPING", "KIDNAPPED", "KIDNAP", "KIDNAPPERS", "HOSTAGES", "HOSTAGE", 'BLINDFOLDED'])
bombing = set(["BOMBING", "BOMBED", "BLAST", "BOMBS", "EXPLOSIVE", "EXPLOSIVES", "EXPLOSIONS", 'EXPLOSION', 'GRENADES'])
                #'BY A BOMB', 'BY\nA BOMB', 'BY A\nBOMB'])
arson = set(["ARSON", "ON FIRE","ON\nFIRE", "BURNING"])
robbery = set(["ROBBED", "ROBBING", "ROBBERY"])

pre_perp_org = set(["CLAIMED", "CLAIMED RESPONSIBILITY", "OPERATING"])
post_perp_org = set(["PANAMA FROM", "COMMAND OF", "WING OF ", "KIDNAPPED BY", "GUERILLAS OF", "KINGPINS OF", "ATTACKS BY"])

post_target = set(["DESTROYED", "ATTACKS"])
pre_target = set(["HAVE PARTICIPATED", "ABDUCTED BY", "PERPETRATED BY"])


def get_id(document):

    # print text_data_array
    document_array = document.split()
    result = document_array[0]

    return result

def getIncident(article):

    if any (word in article for word in definitely_kidnapping):
        return "KIDNAPPING"
    if any (word in article for word in definitely_arson):
        return "ARSON"
    if any (word in article for word in definitely_attack):
        return "ATTACK"
    if any (word in article for word in definitely_robbery):
    	return "ROBBERY"
    if any (word in article for word in definitely_bombing):
        return "BOMBING"
    if any (word in article for word in kidnapping):
        return "KIDNAPPING"
    if any (word in article for word in arson):
        return "ARSON"
    if any (word in article for word in attack):
        return "ATTACK"
    if any (word in article for word in robbery):
    	return "ROBBERY"
    if any (word in article for word in bombing):
        return "BOMBING"
    else :
        return "ATTACK"

def getWeapon(article, pos_document_array):
    weaponsList = set()
    # for weapon in weapons1:
    #     if weapon in article:
    #         indices = getLocations(weapon.split(), pos_document_array)

    for word in article.split():
        word = word.strip()
        if len(word) > 0:
            if word in weapons1 or word in weapons2:
                weaponsList.add(word)
    if len(weaponsList) == 0:
        weaponsList.add("-")
    return weaponsList

# def getPerp(article, pos_document_array, parse_document_array):
#     result = ""
#     for phrase in post_perp:
#         index = article.find(phrase)
#         if index != -1:
#                 phrase_array = phrase.split()
#                 endIndex = [x+1 for x in getLocations(phrase_array, pos_document_array)]
#                 result += '\n' + getRightResult(pos_document_array, endIndex)
#     for phrase in pre_perp:
#         index = article.find(phrase)
#         if index != -1:
#             phrase_array = phrase.split()
#             endIndex = getLocations(phrase_array, pos_document_array)
#             result += '\n' + getLeftResult(pos_document_array, endIndex)
#
# 	result = result.strip()
#     if result == "" or result == None:
#         return '-'
#
#     result = cleanResult(result, parse_document_array)
#     return result


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
    # pos_documents_array = getPosDocuments(articles)
    # parse_documents_array = getParseDocuments(articles)
    articles.pop(0)
    for i in range(len(articles)):
        # pdb.set_trace()
        # victim = get_victim(articles[i], pos_documents_array[i], parse_documents_array[i])
        # if not victim:
        #     victim = '-'
        # perp_org = get_perp_org(articles[i], pos_documents_array[i], parse_documents_array[i])
        # if not perp_org:
        #     perp_org = '-'
        results += 'ID:\t\t' + str(get_id(articles[i])) + '\n'
        results += 'INCIDENT:\t-\n'# + getIncident(articles[i]) + '\n'
        results += 'WEAPON:\t\t' + '\n'.join(getWeapon(articles[i])) + '\n'
        results += 'PERP INDIV:\t-\n'# + getPerp(articles[i], pos_documents_array[i], parse_documents_array[i]) + '\n'
        results += 'PERP ORG:\t-\n'# + perp_org + '\n'
        results += 'TARGET:\t\t-\n'# + get_target(articles[i]) + '\n'
        results += 'VICTIM:\t\t-\n\n'# + victim + '\n\n'


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
