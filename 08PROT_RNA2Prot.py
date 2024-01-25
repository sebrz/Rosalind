# Given an RNA string s corresponding to a strand of mRNA (of length at most 10kbp)
# Return the protein string encoded by s

def decode_prot(aac_dict, seq):

    Protein = ''
    for i in range(len(seq)-1):
        if i % 3 != 0:
            continue
        else:
            if aac_dict[seq[i:i+3]] == "Stop":
                return Protein
            else:
                Protein = Protein + aac_dict[seq[i:i+3]]
    return Protein


if __name__ == '__main__':

    RNA2AAC = {
        "UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V", "UUC" : "F", "CUC" : "L",
        "AUC" : "I", "GUC" : "V", "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
        "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V", "UCU" : "S", "CCU" : "P",
        "ACU" : "T", "GCU" : "A", "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
        "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A", "UCG" : "S", "CCG" : "P",
        "ACG" : "T", "GCG" : "A", "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
        "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D", "UAA" : "Stop", "CAA" : "Q",
        "AAA" : "K", "GAA" : "E", "UAG" : "Stop", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
        "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G", "UGC" : "C", "CGC" : "R",
        "AGC" : "S", "GGC" : "G", "UGA" : "Stop", "CGA" : "R", "AGA" : "R", "GGA" : "G",
        "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"
    }

    myfile = input('Enter file name: ')
    myfile = myfile + '.txt'
    f = open(myfile, "r")
    seq = f.readline()
    print(decode_prot(RNA2AAC, seq))