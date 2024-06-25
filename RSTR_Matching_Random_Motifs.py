# Given a positive integer N <= 100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp
# Return the probability that if N random DNA strings having the same length as s are constructed with GC-content
# x, then at least one of the strings equals s. We allow for the same random string to be created more than once.

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    myline = f.readline().split()
    N = int(myline[0])
    GC = float(myline[1])
    S = f.readline().strip()
    P = 1
    for x in S:
        if x == 'A' or x == 'T':
            P = P * (1 - GC) / 2
        else:
            P = P * GC / 2
    sol = 1 - ((1 - P) ** N)
    print(sol)