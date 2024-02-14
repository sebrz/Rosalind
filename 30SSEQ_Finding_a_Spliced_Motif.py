# Given 2 DNA strings s and t (each of length at most 1 kbp) in FASTA format
# Return one collection of indices of s in which the symbols of t appear as a subsequence of s.
# If multiple solutions exist, you may return any one

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


if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    seq_names, my_seqs = read_seqs(myfile)

    result = []

    for i in range(len(my_seqs[0])):
        if my_seqs[0][i] == my_seqs[1][0]:
            result.append(i + 1)
            my_seqs[1] = my_seqs[1][1:]
        if len(my_seqs[1]) == 0:
            break

    print(*result)