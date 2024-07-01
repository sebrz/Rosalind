# Given an array A for which A[k] represents the proportion of homozygous recessive individuals for the k-th
# Mendelian factor in a diploid population. Assume that the population is in genetic equilibrium for all factors
# Return an array B having the same length as A in which B[k] represents the probability that a randomly selected
# individual carries at least one copy of the recessive allele for the k-th factor.

import math

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    A = [float(x) for x in f.readline().split()]
    B = []
    for x in A:
        p = 1 - math.sqrt(x)
        B.append(1 - p ** 2)
    print(*B)