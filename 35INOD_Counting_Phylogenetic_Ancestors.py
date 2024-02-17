# Given a positive integer n (3 <= n <= 1000)
# Return the number of internal nodes of any unrooted binary tree having n leaves

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, 'r')
    leaves = int(f.readline().strip())
    print(leaves)
    internal_nodes = 0
    while leaves > 2:
        if (leaves % 2) != 0:
            internal_nodes = internal_nodes + (leaves - 1) / 2
            leaves = (leaves - 1) / 2 + 1
        else:
            internal_nodes = internal_nodes + leaves / 2
            leaves = leaves / 2
    print(int(internal_nodes))
