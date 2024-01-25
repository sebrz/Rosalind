# Given a DNA string s of length at most 1000 nt
# Return 4 integers (separated by spaces) counting the respective number of times that the symbols
# 'A', 'C', 'G', 'T' occur in s

if __name__ == '__main__':


    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    seq = f.readline()
    print(seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T'))