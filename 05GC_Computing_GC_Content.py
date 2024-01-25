# Given at most 10 DNA strings in FASTA format (of length at most 1 kbp each)
# Return the id of the string having the highest GC-content, followed by the GC content of that string.

def calc_gc(seq):

    GC = 0
    for x in seq:
        if x == 'G' or x == 'C':
            GC = GC + 1
        else:
            continue
    GC = GC * 100 / len(seq)
    return GC

if __name__ == '__main__':


    myfile = input('Enter file name: ')
    myfile = myfile + '.txt'
    names = []
    seqs = []
    GC_cont = []
    f = open(myfile, "r")
    curr_seq = ''
    i = 0
    for line in f:
        if line[0] == '>':
            names.append(line[1:])
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
    print(seqs)

    for seq in seqs:
        GC_cont.append(calc_gc(seq))

    print(names[GC_cont.index(max(GC_cont))])
    print(max(GC_cont))
    print (names, GC_cont)
