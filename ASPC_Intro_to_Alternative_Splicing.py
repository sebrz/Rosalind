# Given positive integers m and n with 0<=m<=n<=2000
# Return the sum of combinations C(n,k) for all k satisfying m<=k<=n, modulo 1,000,000
import math

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    line = f.readline().strip().split()
    n, m = int(line[0]), int(line[1])
    sol = 0
    for i in range(m, n + 1):
        sol += math.comb(n, i)
    print(sol % 1000000)