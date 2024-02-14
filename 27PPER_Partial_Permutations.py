# Given positive integers n and k such that 100 >= n and 10 >= k > 0
# Return the total number of partial permutations P(n,k) modulo 1,000,000

import math

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    n, k = [int(i) for i in f.readline().split()]
    print(int((math.factorial(n) / math.factorial(n-k)) % 1000000))
