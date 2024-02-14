# Given an RNA string s of length at most 80 bp having the same number of occurrences of 'A'
# as 'U' and the same number of occurrences of 'C' as 'G'
# Return the total possible number of perfect matchings of basepair edges in the bonding
# graph of S

import math

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    seq = ''
    for line in f:
        if line[0] == '>':
            continue
        seq = seq + line.strip()
    print(math.factorial(seq.count('A')) * math.factorial(seq.count('C')))