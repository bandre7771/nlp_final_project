from read_answers import get_answer_dictionary
from parser import *
import pdb

def find_target(file_name):
    with open(file_name, 'r') as f:
        text_data = f.read().replace('\n', ' ')

    text_data_array = text_data.split('DEV-')
    text_data_array.pop(0)
    # print text_data_array
    results = []
    for document in text_data_array:
        document_array = document.split()
        results.append('DEV-' + document_array[0])

    print results

find_target('sample-textfile.txt')
