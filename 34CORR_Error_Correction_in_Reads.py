# Given a collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some
# of these reads were generated with a single-nucleotide error. For each s in the dataset, one
# of the following applies:
# - s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement)
# - s is incorrect, it appears in the dataset exactly once, and its hamming distance 1 with respect to
# exactly one correct read in the dataset (or its reverse complement)
# Return a list of all corrections in the form "[old read]->[new read]". Each correction must be a single
# symbol substitution

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

def calc_hamm(seq1, seq2):

    hamm = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            continue
        else:
            hamm = hamm + 1
    return hamm

def reverse_complement(seq):

    translation_dict = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    translated_seq = ''
    for x in seq:
        translated_seq = translated_seq + translation_dict[x]
    translated_seq = translated_seq[::-1]
    return translated_seq


if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    seq_name, seqs = read_seqs(myfile)
    true_reads = []
    corrected_reads = []

    # Populate true_reads and vacate those items from seqs
    for i in range(len(seqs)):
        if i >= len(seqs):
            continue
        for j in range(len(seqs)):
            if i == j or j >= len(seqs):
                continue
            if seqs[i] == seqs[j] or seqs[i] == reverse_complement(seqs[j]):
                true_reads.append(seqs[i])
                true_reads.append(seqs[j])
                seqs.pop(max(i,j))
                seqs.pop(min(i,j))

    for i in range(len(seqs)):
        for j in range(len(true_reads)):
            if calc_hamm(seqs[i], true_reads[j]) == 1:
                corrected_reads.append(seqs[i] + '->' + true_reads[j])
                break
            if calc_hamm(seqs[i], reverse_complement(true_reads[j])) == 1:
                corrected_reads.append(seqs[i] + '->' + reverse_complement(true_reads[j]))
                break
    for x in corrected_reads:
        print(x)


