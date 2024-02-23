# Given 2 DNA strings s and t (each having length at most 1 kbp) in FASTA format
# Return a longest common subsequence of s and t

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

def find_lcs(seq1, seq2):
    m, n = len(seq1), len(seq2)
    my_table = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2 [j - 1]:
                my_table[i][j] = my_table[i - 1][j - 1] + 1
            else:
                my_table[i][j] = max(my_table[i - 1][j], my_table[i][j - 1])
    lcs = ''
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs += seq1[i - 1]
            i -= 1
            j -= 1
        elif my_table[i - 1][j] > my_table[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return lcs[::-1]


if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    seq_names, my_seqs = read_seqs(myfile)
    i = 0
    j = 0
    print(find_lcs(my_seqs[0], my_seqs[1]))