# Given a collection of DNA strings in FASTA format having a total length at most 10 kbp
# Return the adjacency list corresponding to O3. You may return edges in any order

def create_graph(names, seqs):
    edges = []
    for i in range(len(seqs)):
        for j in range(len(seqs)):
            if i == j:
                continue
            else:
                if seqs[i][-3:] == seqs[j][:3]:
                    edge = names[i].strip() + ' ' + names[j].strip()
                    print(edge)
                    edges.append(edge)
    return edges


if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    names = []
    seqs = []
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

    edges = create_graph(names, seqs)
    print(edges)