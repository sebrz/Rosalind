# Given 2 DNA strings s1 and s2 of equal length (at most 1 kbp)
# Return the transition/transversion ratio R

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
    purines = ['A', 'G']
    pyrimidines = ['C', 'T']
    seq1 = my_seqs[0]
    seq2 = my_seqs[1]
    transitions = 0
    transversions = 0

    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            continue
        if (seq1[i] in purines and seq2[i] in purines) or (seq1[i] in pyrimidines and seq2[i] in pyrimidines):
            transitions = transitions + 1
        else:
            transversions = transversions + 1

    print(transitions / transversions)