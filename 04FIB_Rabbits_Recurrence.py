# Given positive integers n <= 40 and k <= 5
# Return

if __name__ == '__main__':


    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    seq = f.readline()
    n, k = seq.split()
    n = int(n)
    k = int(k)
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, k * a + b
    print(b)