# Given a collection of at most 5 pairs of permutations, all of which have length 10
# Return the reversal distance between each permutation pair
import time
def calc_rev_dist(seq1, seq2):
    rev_dist = 0
    while seq1 != seq2:
        for i in range(len(seq1)):
            if seq2[i] != seq1[i]:
                a, b = i, seq2.index(seq1[i])
                seq2[a:b + 1] = seq2[a:b + 1][::-1]
                rev_dist += 1
                break
    return rev_dist


if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    seqs = []
    for x in f:
        if x == '':
            continue
        if x.strip():
            seqs.append([int(a) for a in x.strip().split()])
    print(seqs)
    for i in range(0, len(seqs), 2):
        a = (calc_rev_dist(seqs[i], seqs[i + 1]))
        print(a)
