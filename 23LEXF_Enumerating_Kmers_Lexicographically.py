# Given a collection of at most 10 symbols defining an ordered alphabet, and a positive integer n <= 10
# Return all strings of length n that can be formed from the alphabet, ordered lexicographically

def write_strings(length, mystring, my_alphabet):
    if len(mystring) == length:
        print(mystring)
    elif len(mystring) > length:
        return 0
    else:
        for x in my_alphabet:
            mystring = mystring + x
            write_strings(length, mystring, my_alphabet)
            mystring = mystring[:len(mystring)-1]


if __name__ == '__main__':


    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")

    alphabet = f.readline().strip().replace(' ', '')
    length = int(f.readline())
    seq = ''
    write_strings(length, seq, alphabet)