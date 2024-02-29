# Given an RNA string s of length at most 100
# Return the total possible number of maximum matchings of basepair edges in the bonding
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

    # For some reason relating to the way Python 3 rounds numbers that I'm still not clear on,
    # this problem requires us to use floor division (//) in order to get the right answer
    print(int(math.factorial(max(seq.count('A'), seq.count('U'))) //
          math.factorial(max(seq.count('A'), seq.count('U')) - min(seq.count('A'), seq.count('U'))) *
          math.factorial(max(seq.count('G'), seq.count('C'))) //
          math.factorial(max(seq.count('G'), seq.count('C')) - min(seq.count('G'), seq.count('C')))))