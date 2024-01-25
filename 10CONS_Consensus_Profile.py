# Given a collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format
# Return a consensus string and profile matrix for the collection (if several possible consensus exist,
# then you may return any one of them)

def calc_profile(seqs):

    mydic = {
        "A" : 0, "C" : 1, "G" : 2, "T" : 3
    }
    matrix = []
    for i in range(len(seqs[0])):
        matrix.append([0, 0, 0, 0])
    for seq in seqs:
        for i in range(len(seq)):
            matrix[i][mydic[seq[i]]] = matrix[i][mydic[seq[i]]] + 1

    return matrix


def calc_cons(profile):

    dict2 = {
        0 : "A", 1: "C", 2 : "G", 3 : "T"
    }

    consensus = ''
    for item in profile:
        consensus = consensus + dict2[item.index(max(item))]

    return consensus



if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = myfile + '.txt'
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

    profile = calc_profile(seqs)
    consensus = calc_cons(profile)
    print(consensus)

    dict2 = {
        0: "A", 1: "C", 2: "G", 3: "T"
    }
    for i in range(0, 4):
        print(dict2[i], ": ", end=' ')
        for j in range(len(consensus)):
            print(profile[j][i], end=' ')
        print('')
