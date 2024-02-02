# In this problem, we begin with Tom, who in the 0th generation has genotype AaBb.
# Tom has two children in the 1st generation, each of whom has two children, and so on.
# Each organism always mates with an organism having genotype AaBb.
# Given 2 positive integers k (k<=7) and N (N<=2^k).
# Return the probability that at least N AaBb organisms will belong to the k-th
# generation of Tom's family tree.
import math

def binomial_prob(k, n):
    # The k inside this function isn't the same k that represents the generation
    # We know from Punnett squares that the probability of offspring having AaBb genotype is 0.25
    # This holds true even for subsequent generations
    binomial_coeff = math.factorial(n)/(math.factorial(k) * math.factorial(n - k))
    return binomial_coeff*(0.25**k) * (1-0.25)**(n - k)

if __name__ == '__main__':

    # Grab k and N from the input file
    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    k, N = map(int, f.readline().split())

    # The probability of having at least N individuals with AaBb genotype is equal to
    # the sum of the probabilities of having N..k^2 individuals. In order to calculate these, we'll use
    # the binomial distribution probability mass function
    P_AaBb = 0.0
    i = N
    while i <= (2 ** k):
        P_AaBb += binomial_prob(i, 2 ** k)
        i = i + 1

    print(P_AaBb)
