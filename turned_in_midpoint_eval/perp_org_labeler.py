from read_answers import get_answer_dictionary
from parser import *
import pdb

def get_perp_org(document):

    train_dictionary = get_answer_dictionary("developset/answers/")
    perp_org = train_dictionary['PERP ORG']
    # pdb.set_trace()
    # print perp_org
    search_organizations = ['claimed responsibility']#, 'participated']
    # print text_data_array
    # pdb.set_trace()
    result = ""
    org = ""
    for item in search_organizations:
        if item.lower() in document.lower():
            document_array = document.split()
            start_index = get_item_location(document_array, item.split()[0])
            org = get_prev_nns(document_array, start_index)
            if org:
                result = org
                # pdb.set_trace()
                break
    if not org:
        result = '-'

    return result



def get_item_location(array, word):
    for item in array:
        if word in item.lower():
            # pdb.set_trace()
            return array.index(item)

def get_prev_nns(array, index):
    while index > 0:
        index -= 1
        result = posInput(array[index])
        # print result
        if result[0][1].startswith('N'):
            # if result[0][0] == 'SUSPECTS':
            #     pdb.set_trace()
            return result[0][0]

    return None



# find_perp_org('sample-textfile.txt')
