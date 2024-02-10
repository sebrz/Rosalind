# Given a positive integer n <= 7
# Return the total number of permutations of length n, followed by a list of all such permutations

import math

def permute(a, l, r):
    if l == r:
        print(*a)
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
    print(math.perm(my_int))
    my_string = ''

    for i in range(1, int(my_int) + 1):
        my_string = my_string + str(i)
    n = len(my_string)
    a = list(my_string)

    # Function call
    permute(a, 0, n)