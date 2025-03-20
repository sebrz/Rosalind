# Given a list L of n <= 100 positive real numbers
# Return a protein string of length n - 1 whose prefix spectrum is equal to L

if __name__ == '__main__':

    # Load mass table
    g = open("Data_files/Monoisotopic_Mass_Table.txt", 'r')
    aac = []
    mass = []
    for line in g:
        div_line = line.split()
        aac.append(div_line[0])
        mass.append(float(div_line[1]))

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    prefix_vals = []
    for line in f:
        prefix_vals.append(float(line.strip()))
    sol = ''
    for i in range(len(prefix_vals) - 1):
        aac_mass = prefix_vals[i + 1] - prefix_vals[i]
        min_diff = 1000
        index = 0
        for j in range(len(mass)):
            if abs(aac_mass - mass[j]) < min_diff:
                min_diff = abs(aac_mass - mass[j])
                index = j
        sol = sol + aac[index]
    print(sol)

