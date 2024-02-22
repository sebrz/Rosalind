# Given a DNA string s (of length at most 100 kbp) in FASTA format
# Return the failure array of s

def compute_failure_array(seq, position, previous_value):
    failure_val = 0
    for i in range(1, previous_value + 1):
        if seq[0:i] == seq[position + 1 - i:position + 1]:
            failure_val = len(seq[0:i])
    return(failure_val)


if __name__ == '__main__':


    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    seq = ''
    for x in f:
        if x[0] == '>':
            continue
        seq = seq + x.strip()
    p = [0]
    for i in range(1, len(seq)):
        if seq[i] == seq[p[i - 1]]:
            p.append(p[i - 1] + 1)
        elif p[i - 1] != 0:
            p.append(compute_failure_array(seq, i, p[i-1]))
        else:
            p.append(0)
    print(*p)