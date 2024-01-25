# Given a DNA string t having a length of at most 1000 nt
# Return the transcribed RNA string of t

if __name__ == '__main__':


    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    seq = f.readline()
    print(seq.replace('T', 'U'))