#! /usr/bin/python3

#
# CARA PENGGUNAAN
# Di terminal ketikkan
# ./process.py pnk-indo indo-sambas > output.txt

import sys
import os
import math

if (len(sys.argv) < 3):
    print("Error.")
    exit(1)

filename_1 = sys.argv[1]
filename_2 = sys.argv[2]

def generate_dict_table(filename, is_first = True):
    phrase_table = {}
    pair_table = {}

    with open(filename) as file_1:
        for row in file_1:
            splitted_row = row.split("|||")
            
            if (len(splitted_row) < 4):
                continue

            if (is_first):
                phrase = splitted_row[1].strip()
                pair_table[splitted_row[1].strip()] = splitted_row[0].strip() 
            else:
                phrase = splitted_row[0].strip()
                pair_table[splitted_row[0].strip()] = splitted_row[1].strip() 

            probabilities = splitted_row[2].strip().split(' ')

            probability_1 = probabilities[1]
            probability_2 = probabilities[3]
        
            phrase_table[phrase] = max([float(probability_1), float(probability_2)])
    return phrase_table, pair_table

phrase_table_1, pair_table_1 = generate_dict_table(filename_1)
phrase_table_2, pair_table_2 = generate_dict_table(filename_2)

for phrase in phrase_table_1:
    if (phrase in phrase_table_2):
        print("{}\t{}\t{}".format(
            pair_table_1[phrase],
            pair_table_2[phrase],
            phrase_table_1[phrase] * phrase_table_2[phrase]
        ))
