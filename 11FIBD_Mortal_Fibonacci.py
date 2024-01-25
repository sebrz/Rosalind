def rabbits(n, k):
    R1 = 1
    R2 = 0
    R3 = 1
    R = []
    for i in range(n):
        R.append(R1 + R2)
        if i > k - 1:
            R[i] = R[i] - R3
            R3 = R[i-k]
        if i > 0:
            R1 = R[i]
            R2 = R[i-1]
    return R


if __name__ == '__main__':

    n = int(input('Enter n: '))
    k = int(input('Enter k: '))
    print(rabbits(n, k))