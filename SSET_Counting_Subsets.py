# Given a positive integer n <= 10000
# Return the total number of subsets modulo 1,000,000

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    n = int(f.readline().strip())
    sol = 2 ** n
    print(sol % 1000000)