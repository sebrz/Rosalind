# Given a positive integer n <= 6
# Return the total number of signed permutations of length n followed by a list

import math
from itertools import product

def perm_sign(curr_permutation):
    perm_signs = list(product([-1, 1], repeat=len(curr_permutation)))
    for x in perm_signs:
        resulting_perm = [a * b for a,b in zip(curr_permutation, x)]
        print(*resulting_perm)
    return

def permute(a, l, r):
    if l == r:
        perm_sign(a)
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    my_int = int(f.readline())
    print(math.perm(my_int) * 2 ** my_int)
    my_string = ''
    int_list = []

    for i in range(1, int(my_int) + 1):
        int_list.append(i)
    n = len(int_list)

    # Function call
    permute(int_list, 0, n)