# Given 2 DNA strings s and t (each of length at most 1 kbp)
# Return all locations of t as a substring of s

def find_motif(seq, motif):

    pos = []
    print(motif)
    for i in range(len(seq)-1):
        if seq[i] == motif[0]:
            print(len(motif))
            print(seq[i:i+len(motif)], motif)
            if seq[i:i+len(motif)] == motif:
                pos.append(i + 1)
                print("yes")
    print(pos)
    return pos


if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = myfile + '.txt'
    f = open(myfile, "r")
    seq = f.readline()
    motif = f.readline().strip()
    pos = find_motif(seq, motif)
    for i in pos:
        print(i, end=' ')