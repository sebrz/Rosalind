# Given a DNA string s of length at most 1000 bp
# Return the reverse complement of s

if __name__ == '__main__':


    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    seq = f.readline()
    translation_dict = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    translated_seq = ''
    for x in seq:
        translated_seq = translated_seq + translation_dict[x]
    translated_seq = translated_seq[::-1]
    print(translated_seq)