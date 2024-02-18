# Given a DNA string s in FASTA format (having length at most 100 kbp)
# Return the 4-mer composition of s

def generate_lexicographic_list(length, mystring, my_alphabet, kmers):
    if len(mystring) == length:
        kmers.append(mystring)
    elif len(mystring) > length:
        return 0
    else:
        for x in my_alphabet:
            mystring = mystring + x
            generate_lexicographic_list(length, mystring, my_alphabet, kmers)
            mystring = mystring[:len(mystring)-1]


if __name__ == '__main__':


    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    dnaseq = ''
    for x in f:
        if x[0] == '>':
            continue
        dnaseq = dnaseq + x.strip()

    alphabet = ['A', 'C', 'G', 'T']
    length = 4
    seq = ''
    kmers = []
    generate_lexicographic_list(length, seq, alphabet, kmers)
    counts = [0]*len(kmers)

    for i in range(len(dnaseq) - 3):
        counts[kmers.index(dnaseq[i:i + 4])] = counts[kmers.index(dnaseq[i:i + 4])] + 1

    print(*counts)