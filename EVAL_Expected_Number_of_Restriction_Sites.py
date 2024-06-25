# Given a positive integer n < = 1,000,000, a DNA string s of even length at most 10, and an array A
# of length at most 20, containing numbers between 0 and 1
# Return An array B having the same length as A in which B[i] represents the expected number of times that s will
# appear as a substring of a random DNA string t of length n, where t is formed with GC-content A[i]

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    N = int(f.readline())
    S = f.readline().strip()
    A = [float(i) for i in f.readline().split()]
    sol = []
    for x in A:
        P = 1
        for y in S:
            if y == 'A' or y =='T':
                P = P * (1 - x) / 2
            else:
                P = P * x / 2
        P = P * (N - (len(S) - 1))
        sol.append(P)
    print(*sol)