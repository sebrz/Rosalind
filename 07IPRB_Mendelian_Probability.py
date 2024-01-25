# Given 3 positive integers k, m, n, representing a population containing k+m+n organisms:
#   k individuals are homozygous dominant for a factor
#   m are heterozygous
#   n are homozygous recessive
# Return the probability that two randomly selected mating organisms will produce an individual possessing
# a dominant allele (and thus displaying the dominant phenotype). Assume that any 2 organisms can mate


def calc_prob(k, m, n):

    T = k + m + n
    Pk = k/T
    Pm = m/T * (k/(T-1) + (m-1)/(T-1)*0.75 + n/(T-1)*0.5)
    Pn = n/T * (k/(T-1) + m/(T-1)*0.5)
    P = Pk + Pm + Pn
    return P


if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = myfile + '.txt'
    f = open(myfile, "r")
    k, m, n = (map(int, f.readline().split()))
    print(calc_prob(k, m, n))