# Given a positive integer n <= 10000 followed by a permutation PI of length n
# Return a longest increasing subsequence of PI, followed by a longest decreasing subsequence

def longest_increasing_subsequence(permutation_seq):
    n = len(permutation_seq)
    subseq_lengths = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if permutation_seq[i] > permutation_seq[j] and subseq_lengths[i] < subseq_lengths[j] + 1:
                subseq_lengths[i] = subseq_lengths[j] + 1

    # Find the maximum value in the LIS array
    max_length = max(subseq_lengths)

    # Reconstruct the longest increasing subsequence
    result = []
    max_index = subseq_lengths.index(max_length)
    result.append(permutation_seq[max_index])

    for i in range(max_index - 1, -1, -1):
        if permutation_seq[i] < permutation_seq[max_index] and subseq_lengths[i] == subseq_lengths[max_index] - 1:
            result.append(permutation_seq[i])
            max_index = i

    result.reverse()
    return result


if __name__ == '__main__':


    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    f.readline()
    permutation = [int(i) for i in f.readline().split()]
    rev_perm = permutation[::-1]
    LIS = longest_increasing_subsequence(permutation)
    LDS = longest_increasing_subsequence(rev_perm)[::-1]
    print(*LIS)
    print(*LDS)