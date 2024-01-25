# Given 6 nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number
# of couples in a population possessing each genotype pairing for a given factor. In order, the 6 given
# integers represent the number of couples having the following genotypes:
#   1. AA-AA
#   2. AA-Aa
#   3. AA-aa
#   4. Aa-Aa
#   5. Aa-aa
#   6. aa-aa
# Return the expected number of offspring displaying the dominant phenotype in the next generation, under the
# assumption that every couple has exactly two offspring

def calc_offspring(a, b, c, d, e):

    ans = a * 2 + b * 2 + c * 2 + d * 1.5 + e * 1

    return ans


if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = myfile + '.txt'
    names = []
    seqs = []
    f = open(myfile, "r")
    a, b, c, d, e, f = f.readline().strip().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)

    print(calc_offspring(a, b, c, d, e))
