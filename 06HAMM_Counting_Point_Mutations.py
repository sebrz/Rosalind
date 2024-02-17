# Given 2 DNA strings s and t of equal length (not exceeding 1 kbp)
# Return the Hamming distance

def calc_hamm(seq1, seq2):

    hamm = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            continue
        else:
            hamm = hamm + 1
    return hamm

if __name__ == '__main__':


    myfile = input('Enter file name: ')
    myfile = myfile + '.txt'
    names = []
    seqs = []
    GC_cont = []
    f = open(myfile, "r")
    seq1 = f.readline()
    seq2 = f.readline()
    print(calc_hamm(seq1, seq2))
