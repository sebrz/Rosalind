# Given a positive integer n <= 20,000 and two subsets A and B of {1,2,...,n}
# Return six sets: Union, Intersection, A-B, B-A, A complement and B complement

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    n = int(f.readline().strip())
    A = set([int(i) for i in f.readline().strip()[1:-1].split(', ')])
    B = set([int(i) for i in f.readline().strip()[1:-1].split(', ')])
    C = set([i for i in range(1, n + 1)])
    print(A | B)
    print(A & B)
    print(A - B)
    print(B - A)
    print(C - A)
    print(C - B)

