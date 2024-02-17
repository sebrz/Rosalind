# Given an RNA string s having the same number of occurrences of 'A' as 'U' and the same number of
# occurrences of 'C' as 'G'. The length of the string is at most 300bp
# Return the total number of non-crossing perfect matchings of basepair edges in the bonding graph
# of s, modulo 1,000,000
if __name__ == '__main__':

    #myfile = input('Enter file name: ')
    #myfile = 'Data_files/' + myfile + '.txt'
    #f = open(myfile, "r")

    cat_numbers = [1, 1]
    cat_index = int(input('Enter catalan index: '))

    for i in range(len(cat_numbers), cat_index):
        calc_cat = 0
        for k in range(1, i + 1):
            calc_cat = calc_cat + cat_numbers[k-1] * cat_numbers[i-k]
        cat_numbers.append(calc_cat)
    print(cat_numbers)
