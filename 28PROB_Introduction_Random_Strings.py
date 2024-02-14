# Given a DNA string s of length at most 100 bp and an array A containing at most 20
# numbers between 0 and 1
# Return an array B having the same length as A in which B[k] represents the common
# logarithm of the probability that a random string constructed with the GC-content found
# in A[k] will match s exactly

import math

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    seq = f.readline().strip()
    A = [float(i) for i in f.readline().split()]
    B = []

    for i in range(len(A)):
        prob = 1.0
        for j in range(len(seq)):
            if seq[j] == 'A' or seq[j] == 'T':
                prob = prob * (1.0 - A[i]) / 2.0
            if seq[j] == 'G' or seq[j] == 'C':
                prob = prob * A[i] / 2.0
        B.append(prob)

    B = [math.log(i, 10) for i in B]
    print(*B)