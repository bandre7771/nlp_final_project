from read_answers import get_answer_dictionary
from parser import *
import pdb

def get_target(document):
    search_targets = ["ATTACKS ON"]
    # print text_data_array
    result = ""
    found_target = ""
    for target in search_targets:
        if target in document:
            document_array = document.split()
            start_index = get_target_location(document_array, target)
            found_target = get_next_nns(document_array, start_index, search_targets)
            if found_target != '-':
                result = found_target
                # pdb.set_trace()
                break

    # pdb.set_trace()
    if not found_target:
        result = '-'

    return result

def get_target_location(document_array, target):
    split_target = target.split()
    star_index = 0
    for item in document_array:
        if split_target[0] in item:
            # pdb.set_trace()
             star_index = document_array.index(item)
             if document_array[star_index + 1] in split_target[1]:
                 return star_index

    return 0


def get_next_nns(document_array, index, search_targets):
    result = ''
    for target in search_targets:
        if document_array[index] in target:
            change_index = len(target.split())
            new_index = index + change_index
            prev_noun = False
            for i in range(new_index, len(document_array)):
                pos = posInput(document_array[i])
                # pdb.set_trace()
                if pos[0][1].startswith('N'):
                    result += pos[0][0] + ' '
                    prev_noun = True
                    # if result[0][0] == 'SUSPECTS':
                    #     pdb.set_trace()
                elif pos[0][1].startswith('CC') and prev_noun:
                    result += '\n'
                    continue
                elif prev_noun:
                    return result.strip()

    return '-'



# find_target("sample-textfile.txt")
