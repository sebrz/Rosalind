# Given a DNA string s of length at most 1kbp and a collection of substrings of s acting
# as introns (all given in FASTA format)
# Return a protein string resulting from transcribing and translating the exons of s

def read_seqs(myfile):
    # This function will take in a file, and place the sequence names in a list, and
    # the sequences themselves in another list
    names = []
    seqs = []
    f = open(myfile, "r")
    curr_seq = ''
    i = 0
    for line in f:
        if line[0] == '>':
            names.append(line[1:].replace("\n", ""))
            if i == 0:
                continue
            curr_seq = curr_seq.replace("\n", "")
            seqs.append(curr_seq)
            curr_seq = ''
        else:
            curr_seq = curr_seq + line
        i = i + 1

    curr_seq = curr_seq.replace("\n", "")
    seqs.append(curr_seq)
    return names, seqs

def decode_prot(aac_dict, seq):

    protein = ''
    for i in range(len(seq)-1):
        if i % 3 != 0:
            continue
        else:
            if aac_dict[seq[i:i+3]] == "Stop":
                return protein
            else:
                protein = protein + aac_dict[seq[i:i+3]]
    return protein

if __name__ == '__main__':

    RNA2AAC = {
        "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L",
        "AUC": "I", "GUC": "V", "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
        "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V", "UCU": "S", "CCU": "P",
        "ACU": "T", "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
        "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A", "UCG": "S", "CCG": "P",
        "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
        "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "UAA": "Stop", "CAA": "Q",
        "AAA": "K", "GAA": "E", "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
        "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G", "UGC": "C", "CGC": "R",
        "AGC": "S", "GGC": "G", "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
        "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    seq_names, my_seqs = read_seqs(myfile)
    DNA = my_seqs[0]

    for i in range(1, len(my_seqs)):
        DNA = DNA.replace(my_seqs[i], '')
    RNA = DNA.replace('T', 'U')
    print(decode_prot(RNA2AAC, RNA))