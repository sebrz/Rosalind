# Given a positive integer n <= 50
# Return an array A of length 2n in which A[k] represents the common logarithm of the probability that two
# diploid siblings share at least k of their 2n chromosomes
import math

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    n = int(f.readline().strip())
    sol = []
    for i in range(2 * n, 0, -1):
        p = 0
        for j in range(0, i):
            p += math.comb(2 * n, j) * 0.5 ** j * 0.5 ** (2 * n - j)
        sol.append(math.log(p, 10))
    print(*sol)