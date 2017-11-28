from read_answers import get_answer_dictionary
from parser import *
import pdb

perp_org_right = ['MEMBER OF', 'GROUP OF', 'PANAMA FROM', 'COMMAND OF', 'WING OF',
                    'KIDNAPPED BY', 'GUERILLAS OF', 'KINGPINS OF', 'ATTACKS BY']
perp_org_left = ['CLAIMING RESPONSIBILITY', 'ATTRIBUTED TO',
                'CLAIMED RESPONSIBILITY', 'CLAIMS IT', 'CLAIMED CREDIT',
                'CLAIMED', 'OPERATING']
people_not_covered = ['LUIS', 'OSCAR', 'DINO', 'ROSSY']

def get_perp_org(document, pos_document_array, parse_document_array):

    result = ""
    name = ''
    prev_location = False
    prev_person = False

    num_in = 0

    document_array = document.split()
    # if document_array[0] == 'DEV-MUC3-0023':
    #     pdb.set_trace()
    for phrase in perp_org_right:
        index = document.find(phrase)
        if index != -1:
            num_in += 1
            # if document_array[0] == 'TST2-MUC4-0078':
            #     pdb.set_trace()
            phrase_array = phrase.split()
            endIndex = [x+1 for x in getLocations(phrase_array, pos_document_array)]
            result += '\n' + getRightResult(parse_document_array, pos_document_array, endIndex)

    for phrase in perp_org_left:
        index = document.find(phrase)

        if index != -1:
            num_in += 1
            # if document_array[0] == 'DEV-MUC3-0075':# and phrase == 'WERE\nKIDNAPPED':
            #     pdb.set_trace()
            phrase_array = phrase.split()
            endIndex = getLocations(phrase_array, pos_document_array)
            result += '\n' + getLeftResult(parse_document_array, pos_document_array, endIndex)
    #
    #
    #
    # result = result.strip()
    # if result == "" or result == None:
    #     for word in parse_document_array:
    #         if word[1] == 'ORGANIZATION':
    #             result += word[0] + '\n'
    #     if result == "" or result == None:
    #         return '-'
    #     else:
    #         return result
    # # if document_array[0] == 'DEV-MUC3-0062':
    # #     pdb.set_trace()
    if result == "" or result == None:
            return '-'
    result = cleanResult(result, parse_document_array)
    # print "Number of phrases: ", num_in
    return result

def getLeftResult(parse_document_array, pos_document_array, endIndices):
    result = ""
    startIndex = ""
    is_org = False
    had_comma = False
    o = 0
    # pdb.set_trace()
    for endIndex in endIndices:
        is_org = False
        had_comma = False
        for k in range(0, 9):
            parse_item = parse_document_array[endIndex - k + o]
            if parse_item[0] == ',':
                endIndex = getOrgIndexAfterComma(endIndex - k + o, pos_document_array)
                o = k + 1
                had_comma = True
            elif parse_item[1] == 'ORGANIZATION':
                result += str(endIndex - k + o) + ' ' + parse_item[0]
                is_org = True
                return result
            elif pos_document_array[endIndex - k + o] and had_comma:
                result += str(endIndex - k + o) + ' ' + parse_item[0]
                return result
        # for k in range(0, 9):
        #     pos_item = pos_document_array[endIndex - k]
        #     if pos_item[1].startswith('NN') and not pos_item[0] == '[' and not pos_item[0] == ']':# == 'NNP':
        #         # result = str(endIndex - k) + ' '
        #         while True:
        #             pos_item = pos_document_array[endIndex - k]
        #             if pos_item[1] == 'CC':
        #                 # if pos_document_array[0][0] == 'DEV-MUC3-0537':
        #                 #     pdb.set_strace()
        #                 startIndex = str(endIndex - k + 1)
        #                 endIndex = endIndex - k - 1
        #                 result = startIndex + ' ' + result + '\n'
        #                 # result += '\n'
        #                 # pdb.set_trace()
        #                 for o in range(0, 6):
        #                     pos_item = pos_document_array[endIndex - o]
        #                     if pos_item[1].startswith('NN'): #and not pos_item[0] == '[' and not pos_item[0] == ']':# == 'NNP':
        #                         # result += str(endIndex - o) + ' '
        #                         while True:
        #                             pos_item = pos_document_array[endIndex - o]
        #                             if not pos_item[1].startswith('NN') and not pos_item[1].startswith('JJ'): #or pos_item[0] == '[' or pos_item[0] == ']': #!= 'NNP':
        #                                 startIndex = str(endIndex - o + 1)
        #                                 result = startIndex + ' ' + result
        #                                 break
        #                             result = pos_item[0] + ' ' + result
        #                             o += 1
        #                         break
        #                 break
        #             elif pos_item[0] == ']':
        #                 while True:
        #                     pos_item = pos_document_array[endIndex - k]
        #                     if pos_item[0] == '[':
        #                         break
        #                     result = pos_item[0] + ' ' + result
        #                     k += 1
        #             elif not pos_item[1].startswith('NN') and not pos_item[1].startswith('JJ'): # or pos_item[0] == '[' or pos_item[0] == ']': # != 'NNP':
        #                 startIndex = str(endIndex - k + 1)
        #                 result = startIndex + ' ' + result
        #                 break
        #             result = pos_item[0] + ' ' + result
        #             k += 1
        #         break
        #     elif pos_item[1] == ',':
        #         result = getOrgAfterComma(endIndex - k, pos_document_array)
        #         break
        #
        # result = '\n' + result
    return result.strip()

def getOrgIndexAfterComma(index, pos_document_array):
    result = ""
    for j in range(1, index - 1):
        if pos_document_array[index - j][0] == ',':
            index = index - j - 1
            return index

    return -1

def getRightResult(parse_document_array, pos_document_array, endIndices):
    # pdb.set_trace()
    # if parse_document_array[0][0] == 'DEV-MUC3-0204':
    #     pdb.set_trace()
    result = ""
    startIndex = ""
    is_org = False
    for endIndex in endIndices:
        is_org = False
        for k in range(0, 9):
            if (endIndex + k) >= len(parse_document_array):
                return result
            parse_item = parse_document_array[endIndex + k]
            if parse_item[1] == 'ORGANIZATION':
                result += str(k + endIndex) + ' '+ parse_item[0]
                is_org = True
                return result


        # for k in range(0, 9):
        #     if k + endIndex >= len(pos_document_array):
        #         break
        #     pos_item = pos_document_array[k + endIndex]
        #     if pos_item[1].startswith('NN') and not pos_item[0] == '[' and not pos_item[0] == ']':# == 'NNP':
        #         result += str(k + endIndex)
        #         while True:
        #             pos_item = pos_document_array[k + endIndex]
        #             if pos_item[1] == 'CC':
        #                 # pdb.set_strace()
        #                 endIndex = endIndex + k + 1
        #                 result += '\n'
        #                 # pdb.set_trace()
        #                 for o in range(0, 6):
        #                     pos_item = pos_document_array[o + endIndex]
        #                     if pos_item[1].startswith('NN'):# and not pos_item[0] == '[' and not pos_item[0] == ']':# == 'NNP':
        #                         result += str(o + endIndex)
        #                         while True:
        #                             pos_item = pos_document_array[o + endIndex]
        #                             if not pos_item[1].startswith('NN') and not pos_item[1].startswith('JJ'): # or pos_item[0] == '[' or pos_item[0] == ']':# != 'NNP':
        #                                 break
        #                             result += ' ' + pos_item[0]
        #                             o += 1
        #                         break
        #                 break
        #             if pos_item[0] == ',':
        #                 while not pos_item[1].startswith('NN'):
        #                     k+=1
        #                     pos_item = pos_document_array[k + endIndex]
        #                 result += '\n' + str(k + endIndex)
        #                 continue
        #             elif not pos_item[1].startswith('NN') and not pos_item[1].startswith('JJ'): # or pos_item[0] == '[' or pos_item[0] == ']':# != 'NNP':
        #                 break
        #             result += ' ' + pos_item[0]
        #             k += 1
        #         break
        # result += '\n'
    return result.strip()

def cleanResult(result, parse_document_array):
    result_array = result.split('\n')
    is_person = False
    new_result = ""
    result_array = ridDuplicates(result_array, True)
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
            if r.strip().isdigit():
                continue
            num_index = r.find(' ')
            new_result += r[num_index:]
        new_result += '\n'
    # new_result_array = new_result.split('\n')
    # new_result = '\n'.join(ridDuplicates(new_result_array, False))
    # pdb.set_trace()
    return new_result.strip()

def ridDuplicates(result_array, is_index):
    new_results = []
    if len(result_array) == 1:
        return result_array
    while len(result_array) != 0:
        item = result_array.pop(0).strip()
        # if 'MARIA ELENA DIAZ' in item:
        #     pdb.set_trace()
        if not contains(item, result_array, is_index) and not contains(item, new_results, is_index):
            new_results.append(item)

    return new_results

def contains(item, result_array, is_index):
    index = item.find(' ')
    if is_index:
        item = item[index:].strip()
    for j in range(len(result_array)):
        if item.strip() in result_array[j].strip():
            return True


def getLocations(phrase_array, pos_document_array):
    indices=[]
    result_indices = []
    for z in range(len(pos_document_array)):
        if pos_document_array[z][0] == phrase_array[0]:
            indices.append(z)
    # indices = [i for i,x in enumerate(pos_documents_array) if x == phrase_array[0]]
    for index in indices:
        if len(phrase_array) == 2 and phrase_array[1] == pos_document_array[index + 1][0]:
            result_indices.append(index)
        elif len(phrase_array) == 3 and phrase_array[1] == pos_document_array[index + 1][0] and phrase_array[2] == pos_document_array[index + 2][0]:
            result_indices.append(index)
        elif len(phrase_array) == 1:
            result_indices.append(index)

    return result_indices



# find_perp_org('sample-textfile.txt')
