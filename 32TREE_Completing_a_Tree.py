# Given a positive integer n <= 1000 and an adjacency list corresponding to a graph on n nodes
# that contains no cycles
# Return the minimum number of edges that can be added to the graph to produce a tree

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    n = int(f.readline().strip())

    # We only need to count the edges given
    edges = 0
    for x in f:
        edges = edges + 1
    # The minimum number of edges to add in order to produce a tree is:
    # min_edges = n - 1 - edges
    print(n - 1 - edges)