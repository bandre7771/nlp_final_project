from read_answers import get_answer_dictionary
from parser import *
import pdb

def get_victim(document):
    result = ""
    name = ''
    document_array = parseInput(document)
    prev_location = False
    prev_person = False
    # document_array = document.split()
    for word in document_array:
        # pdb.set_trace()
        bio_label = word[1]
        if word[0] == 'ELENA':
            prev_person = False
            prev_location = True
        if bio_label == 'PERSON' and not prev_location:
            # pdb.set_trace()
            if prev_person:
                name += ' ' + word[0]
            else:
                name = word[0]
                prev_person = True
        elif bio_label == 'LOCATION':
            # pdb.set_trace()
            prev_location = True
        elif prev_person:
            result = name
            prev_person = False
            break
        else:
            prev_location = False
            prev_person = False
    if not name:
        result = ('-')

    return result

# find_target("sample-textfile.txt")
