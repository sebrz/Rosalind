# Given a protein string of length at most 1000 aa
# Return the total number of different RNA strings from which the protein could have been
# translated, modulo 1,000,000 (Don't forget the stop codon)

if __name__ == '__main__':

    # Dictionary containing the number of possible codons for each aminoacid
    Possible_Codons = {
        "F" : 2, "S" : 6, "Y" : 2, "Stop" : 3, "C" : 2, "W" : 1, "L" : 6,
        "P" : 4, "H" : 2, "Q" : 2, "R" : 6, "I" : 3, "M" : 1, "T" : 4,
        "N" : 2, "K" : 2, "V" : 4, "A" : 4, "D" : 2, "E" : 2, "G" :4
    }

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    protein_seq = f.readline().strip()


    possible_strings = 1
    for i in protein_seq:
        possible_strings = possible_strings * Possible_Codons[i]
    possible_strings = possible_strings * Possible_Codons['Stop']
    print(possible_strings)
    print(possible_strings % 1000000)