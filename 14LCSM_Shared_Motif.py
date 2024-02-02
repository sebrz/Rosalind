# Given a collection of k(k <=100) DNA strings of length at most 1kbp each in FASTA format
# Return a longest common substring of the collection (if multiple solutions exist, you may
# return any single solution)

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

def find_shared_motif(seqs):
    motif = ''
    if len(seqs) > 1 and len(seqs[0]) > 0:
        for i in range(len(seqs[0])):
            for j in range(len(seqs[0]) - i + 1):
                if j > len(motif) and all(seqs[0][i:i + j] in x for x in seqs):
                    motif = seqs[0][i:i + j]
    return motif

if __name__ == '__main__':


    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    seq_names, my_seqs = read_seqs(myfile)
    print(find_shared_motif(my_seqs))