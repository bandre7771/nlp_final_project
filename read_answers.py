import os
import pdb


def get_answer_dictionary(directory):
    answer_dictionary = dict()

    for filename in os.listdir(directory):
        with open(directory + filename) as f:
            answer_file = f.readlines()

        current_label = ""
        for line in answer_file:
            # print line
            label_array = line.split(':')

            if len(label_array) == 1:
                if label_array == '\n':
                    continue
                new_item = label_array[0].strip()
                if current_label in answer_dictionary:
                    temp_array = answer_dictionary[current_label]
                    if new_item in temp_array:
                        # pdb.set_trace()
                        continue
                else:
                    temp_array = []
                    # temp_answer = temp_array[len(answer_dictionary[current_label]) - 1]
                    new_item_split = new_item.split('/')
                    for item in new_item_split:
                        temp_array.append(item.strip())
                        if item.strip() in temp_array:
                            # pdb.set_trace()
                            continue

                # temp_array.append(new_item)
                answer_dictionary[current_label] = temp_array
                continue

            new_item = label_array[1].strip()
            # pdb.set_trace()
            current_label = label_array[0].strip()

            # Check if current label is already in the dictionary
            if current_label in answer_dictionary:
                dictionary_list = answer_dictionary[current_label]
                if new_item in dictionary_list:
                    # pdb.set_trace()
                    continue
            else:
                dictionary_list = []

            new_item_split = new_item.split('/')
            for item in new_item_split:
                dictionary_list.append(item.strip())
                if item.strip() in dictionary_list:
                    # pdb.set_trace()
                    continue

            answer_dictionary[current_label] = dictionary_list

    # print "ID:"
    # print answer_dictionary['ID']
    # print "\nINCIDENT:"
    # print answer_dictionary['INCIDENT']
    # print "\nWEAPON:"
    # print answer_dictionary['WEAPON']
    # print "\nPERP INDIV:"
    # print answer_dictionary['PERP INDIV']
    # print "\nPERP ORG:"
    # print answer_dictionary['PERP ORG']
    # print "\nTARGET:"
    # print answer_dictionary['TARGET']
    # print "\nVICTIM:"
    # print answer_dictionary['VICTIM']
    return answer_dictionary

def main():
    answer_dictionary = get_answer_dictionary("developset/answers/")


if __name__ == '__main__':
    main()
