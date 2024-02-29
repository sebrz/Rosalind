# Given a collection of n (n <= 10) DNA strings s1,...,sn of equal length (at most 1 kbp) in FASTA format
# Return the matrix D corresponding the p-distance dp on the given strings

def read_seqs(myfile):
    # This function will take in a file, and place the sequence names in a list, and
    # the sequences themselves in another list
    names = []
    seqs = []
    f = open(myfile, "r")
    curr_seq = ''
    i = 0
    for line in f:
        if line[0] == '>':
            names.append(line[1:].replace("\n", ""))
            if i == 0:
                continue
            curr_seq = curr_seq.replace("\n", "")
            seqs.append(curr_seq)
            curr_seq = ''
        else:
            curr_seq = curr_seq + line
        i = i + 1

    curr_seq = curr_seq.replace("\n", "")
    seqs.append(curr_seq)
    return names, seqs

def calc_hamm(seq1, seq2):

    hamm = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            continue
        else:
            hamm = hamm + 1
    return hamm

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    seq_names, seqs = read_seqs(myfile)
    p_matrix = []
    for x in seqs:
        p_array = []
        for y in seqs:
            p_array.append(calc_hamm(x, y) / len(x))
        p_matrix.append(p_array)
    for x in p_matrix:
        print(*x)