# Given at most 50 DNA strings of approximately equal length, not exceeding 1kbp in FASTA format
# (which represent reads deriving from the same strand of a single linear chromosome)
# The dataset is guaranteed to satisfy the following condition: there exists a unique way to
# reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap
# by more than half their length
# Return the shortest superstring containing al the given strings (corresponding to a reconstructed
# chromosome)

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

    # Start with the first sequence
    superstring = my_seqs[0]
    my_seqs.pop(0)
    search_index = 0
    while len(my_seqs) > 0:
        for i in range(len(my_seqs[search_index]) - 1, int(len(my_seqs[search_index])/2), -1):
            if my_seqs[search_index][:i] == superstring[-i:]:
                superstring = superstring + my_seqs[search_index][i:]
                my_seqs.pop(search_index)
                search_index = -1
                break
            if my_seqs[search_index][-i:] == superstring[:i]:
                superstring = my_seqs[search_index][:-i] + superstring
                my_seqs.pop(search_index)
                search_index = -1
                break
        search_index = search_index + 1
    print(superstring)
