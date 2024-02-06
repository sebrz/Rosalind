# Given a DNA string s of length at most 1 kbp in FASTA format
# Return every distinct candidate protein string that can be translated from ORFs of s

def reverse_complement (seq):
    translation_dict = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    rev_compl_seq = ''
    for x in seq:
        rev_compl_seq = rev_compl_seq + translation_dict[x]
    rev_compl_seq = rev_compl_seq[::-1]
    return rev_compl_seq

def DNA2RNA (seq):
    translated_seq = seq.replace('T', 'U')
    return translated_seq

def find_proteins (RNA_seq, proteins):
    for i in range(0, 3):
        for j in range(i, len(RNA_seq) - 2, 3):
            if RNA2AAC[RNA_seq[j:j + 3]] == 'M':
                candidate = ''
                for k in range(j, len(RNA_seq) - 2, 3):
                    if RNA2AAC[RNA_seq[k:k + 3]] == 'Stop':
                        if candidate not in proteins:
                            proteins.append(candidate)
                        break
                    candidate = candidate + RNA2AAC[RNA_seq[k:k + 3]]
    return proteins


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
    f = open(myfile, "r")
    seq = ''
    for line in f:
        if line[0] == '>':
            continue
        seq = seq + line.strip()
    RNA_seq = DNA2RNA(seq) # Translating the sequence
    proteins = []
    find_proteins(RNA_seq, proteins)
    # Now do the reverse complement
    RNA_seq2 = DNA2RNA(reverse_complement(seq))
    find_proteins(RNA_seq2, proteins)
    print(*proteins, sep = '\n')

