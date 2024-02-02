# Given at most 15 UniProt Protein Database access IDs
# Return the access ID for each protein possessing the N-glycosylation motif "N{P}[ST]{P}"
# followed by a list of locations in the protein string where the motif can be found

import urllib.request
import re

def get_protein_sequence(accession_id):
    # This function accesses the protein FASTA file in uniprot and saves the sequence into a single string
    protein_url = 'https://rest.uniprot.org/uniprotkb/' + accession_id + '.fasta'
    protein_page = urllib.request.urlopen(protein_url)
    protein_sequence = ''
    for line in protein_page:
        line = line.decode('ascii')
        if line[0] == '>':
            continue
        protein_sequence = protein_sequence + line.strip()
    return protein_sequence

def find_motif(protein_sequence):
    # This function uses re to search for all instances of motif in a given protein sequence
    motif = '(?=N[^P][ST][^P])'
    my_iter = re.finditer(motif, protein_sequence)
    return list(m.start(0) + 1 for m in my_iter)

if __name__ == '__main__':

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    access_IDs = []
    for x in f:
        access_IDs.append(x.strip())
    for ID in access_IDs:
        # We'll use only the first 6 characters because otherwise Uniprot returns a 404 error
        protein_seq = get_protein_sequence(ID[0:6])
        if len(find_motif(protein_seq)) > 0:
            print(ID)
            print(*find_motif(protein_seq))