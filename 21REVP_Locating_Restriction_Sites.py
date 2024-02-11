# Given a DNA string of length at most 1kbp in FASTA format
# Return the position and length of every reverse palindrome in the string of length 4-12

def reverse_complement (seq):
    translation_dict = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    rev_compl_seq = ''
    for x in seq:
        rev_compl_seq = rev_compl_seq + translation_dict[x]
    rev_compl_seq = rev_compl_seq[::-1]
    return rev_compl_seq

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    seq = ''
    for line in f:
        if line[0] == '>':
            continue
        seq = seq + line.strip()
    rev_seq = reverse_complement(seq)
    palindromes = []
    start_index = []
    palindrome_length = []
    for i in range(len(seq)):
        for j in range(len(seq)):
            if seq[i:i + 4] == rev_seq[j:j + 4]:
                k = 0
                palindrome = ''
                while k + 3 <= 11 and seq[i:i + k + 4] == rev_seq[j:j + k + 4]:
                    palindrome = seq[i:i + k + 4]
                    if i == len(seq) - j - 4 - k:
                        print(palindrome)
                        palindromes.append(palindrome)
                        start_index.append(i + 1)
                        palindrome_length.append(len(palindrome))
                    k = k + 1
    #print(*palindromes)
    for i in range(len(start_index)):
        print(str(start_index[i]) + ' ' + str(palindrome_length[i]))


