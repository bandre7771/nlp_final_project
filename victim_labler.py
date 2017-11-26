from parser import *
import pdb
from read_answers import get_answer_dictionary

# While stepping backwards check for phrases that talk about the victim_right
# If there is a comma and there is not
# Result can not include "PERSON"

victim_right = ['ATTACK AGAINST', 'ATTACK ON', 'MURDER OF',
                'KIDNAPPING OF', 'ASSASSINATION OF',
                'GUARDED BY', 'BURIAL OF', 'WAS IDENTIFIED', 'KILLING OF',
                'THAT MURDERED']
victim_left = ['HAVE BEEN KILLED', 'WAS KILLED', 'WERE KILLED',
                'WAS HEADING', 'WERE BROUGHT BEFORE', 'WAS MURDERED',
                'WERE MURDERED', 'DIED', 'KILLED IN', 'WHO LIVES IN',
                'WERE ABDUCTED', 'WAS ABDUCTED', 'WAS GUNNED']
people_not_covered = ['LUIS', 'OSCAR']


def get_victim(document, pos_document_array, parse_document_array):
    result = ""
    name = ''
    # pos_documents_array = posInput(document)
    # parse_documentss_array = parseInput(document)
    prev_location = False
    prev_person = False

    document_array = document.split()

    for phrase in victim_right:
        index = document.find(phrase)
        if index != -1:
            # if document_array[0] == 'DEV-MUC3-0062':
            #     pdb.set_trace()
            phrase_array = phrase.split()
            endIndex = getLocation(phrase_array, pos_document_array) + 1
            result += '\n' + getRightResult(pos_document_array, endIndex)
    #
    # if document_array[0] == 'DEV-MUC3-0383':
    #     pdb.set_trace()

    for phrase in victim_left:
        index = document.find(phrase)
        if index != -1:

            phrase_array = phrase.split()
            endIndex = getLocation(phrase_array, pos_document_array)
            result += '\n' + getLeftResult(pos_document_array, endIndex)



    result = result.strip()
    if result == "" or result == None:
        return '-'
    # if document_array[0] == 'DEV-MUC3-0062':
    #     pdb.set_trace()
    result = cleanResult(result, parse_document_array)
    return result

def getLeftResult(pos_document_array, endIndex):
    result = ""
    startIndex = ""
    for k in range(0, 6):
        if pos_document_array[endIndex - k][1].startswith('NN') and not pos_document_array[endIndex - k][0] == '[' and not pos_document_array[endIndex - k][0] == ']':# == 'NNP':
            # result = str(endIndex - k) + ' '
            while True:
                if pos_document_array[endIndex - k][1] == 'CC':
                    # pdb.set_strace()
                    startIndex = str(endIndex - k + 1)
                    endIndex = endIndex - k - 1
                    result = startIndex + ' ' + result + '\n'
                    # result += '\n'
                    # pdb.set_trace()
                    for o in range(0, 6):
                        if pos_document_array[endIndex - o][1].startswith('NN') and not pos_document_array[endIndex - o][0] == '[' and not pos_document_array[endIndex - o][0] == ']':# == 'NNP':
                            # result += str(endIndex - o) + ' '
                            while True:
                                if not pos_document_array[endIndex - o][1].startswith('NN') and not pos_document_array[endIndex - o][1].startswith('JJ') and not pos_document_array[endIndex - o][0] == '[' and not pos_document_array[endIndex - o][0] == ']': #!= 'NNP':
                                    startIndex = str(endIndex - o + 1)
                                    result = startIndex + ' ' + result
                                    break
                                result = pos_document_array[endIndex - o][0] + ' ' + result
                                o += 1
                            break
                    break
                elif not pos_document_array[endIndex - k][1].startswith('NN') and not pos_document_array[endIndex - k][1].startswith('JJ') and not pos_document_array[endIndex - k][0] == '[' and not pos_document_array[endIndex - k][0] == ']': # != 'NNP':
                    startIndex = str(endIndex - k + 1)
                    result = startIndex + ' ' + result
                    break
                result = pos_document_array[endIndex - k][0] + ' ' + result
                k += 1
            break
        elif pos_document_array[endIndex - k][1] == ',':
            result = getVictimAfterComma(endIndex - k, pos_document_array)
            break

    return result.strip()

def getVictimAfterComma(index, pos_document_array):
    result = ""
    for j in range(1, index - 1):
        if pos_document_array[index - j][0] == ',':
            index = index - j
            for z in range(index - 1):
                if pos_document_array[index - z][1].startswith('NNP'): #== 'NNP':
                    while True:
                        if not pos_document_array[index - z][1].startswith('NNP') and not pos_document_array[index - z][1].startswith('JJ'):# != 'NNP':
                            # pdb.set_trace()
                            startIndex = str(index - z + 1)
                            result = str(index) + ' ' + result
                            break
                        result = pos_document_array[index - z][0] + ' ' + result
                        z += 1
                    break
            break
        if pos_document_array[index -j][0] == '.' or pos_document_array[index - j][0] == '!' or pos_document_array[index -j][0] == '?':
            break

    return result


def getRightResult(pos_document_array, endIndex):
    result = ""
    for k in range(0, 6):
        if pos_document_array[k + endIndex][1].startswith('NN') and not pos_document_array[endIndex + k][0] == '[' and not pos_document_array[endIndex + k][0] == ']':# == 'NNP':
            result = str(k + endIndex)
            while True:
                if pos_document_array[k + endIndex][1] == 'CC':
                    # pdb.set_strace()
                    endIndex = endIndex + k + 1
                    result += '\n'
                    # pdb.set_trace()
                    for o in range(0, 6):
                        if pos_document_array[o + endIndex][1].startswith('NN') and not pos_document_array[endIndex + o][0] == '[' and not pos_document_array[endIndex + o][0] == ']':# == 'NNP':
                            result += str(o + endIndex)
                            while True:
                                if not pos_document_array[o + endIndex][1].startswith('NN') and not pos_document_array[endIndex + o][1].startswith('JJ'):# != 'NNP':
                                    break
                                result += ' ' + pos_document_array[o + endIndex][0]
                                o += 1
                            break
                    break
                if not pos_document_array[k + endIndex][1].startswith('NN') and not pos_document_array[endIndex + k][1].startswith('JJ'):# != 'NNP':
                    break
                result += ' ' + pos_document_array[k + endIndex][0]
                k += 1
            break
    return result.strip()

def cleanResult(result, parse_document_array):
    result_array = result.split('\n')
    is_person = False
    new_result = ""
    result_array = ridDuplicates(result_array)
    for r in result_array:
        is_person = False
        if r == "":
            continue
        result_a = r.split()
        index = int(result_a[0])
        # result_a = ridDuplicates(result_a)
        for i in range(1, len(result_a)):
            if parse_document_array[index][1] == 'PERSON' or parse_document_array[index][0] in people_not_covered:
                # pdb.set_trace()
                is_person = True
                new_result += ' ' + result_a[i]
            if parse_document_array[index][1] == 'LOCATION':
                is_person = True
                new_result += ' '
                break
            index += 1
        if not is_person:
            num_index = r.find(' ')
            new_result += r[num_index:]
        new_result += '\n'

    # pdb.set_trace()
    return new_result.strip()

def ridDuplicates(result_array):
    new_results = []
    if len(result_array) == 1:
        return result_array
    while len(result_array) != 0:
        item = result_array.pop(0).strip()
        if not contains(item, result_array):
            new_results.append(item)

    return new_results

def contains(item, result_array):
    index = item.find(' ')
    item = item[index:].strip()
    for j in range(len(result_array)):
        if item.strip() in result_array[j].strip():
            return True


def getLocation(phrase_array, pos_document_array):
    indices=[]
    for z in range(len(pos_document_array)):
        if pos_document_array[z][0] == phrase_array[0]:
            indices.append(z)
    # indices = [i for i,x in enumerate(pos_documents_array) if x == phrase_array[0]]
    for index in indices:
        if len(phrase_array) == 2 and phrase_array[1] == pos_document_array[index + 1][0]:
            return index
        elif len(phrase_array) == 3 and phrase_array[1] == pos_document_array[index + 1][0]:
            return index
        elif len(phrase_array) == 1:
            return index

    return -1

    # word_index = document_array.index(phrase_array[0])
    # for word in document_array:
    #     # pdb.set_trace()
    #     bio_label = word[1]
    #     if word[0] == 'ELENA':
    #         prev_person = False
    #         prev_location = True
    #     if bio_label == 'PERSON' and not prev_location:
    #         # pdb.set_trace()
    #         if prev_person:
    #             name += ' ' + word[0]
    #         else:
    #             name = word[0]
    #             prev_person = True
    #     elif bio_label == 'LOCATION':
    #         # pdb.set_trace()
    #         prev_location = True
    #     elif prev_person:
    #         result = name
    #         prev_person = False
    #         break
    #     else:
    #         prev_location = False
    #         prev_person = False
    # if not name:
    #     result = ('-')



# find_target("sample-textfile.txt")
