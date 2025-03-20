# Given a list L containing 2n + 3 positive real numbers n <= 100. The first number is the parent mass of peptide P,
# and all other numbers represent the masses of some b-ions and y-ions of P (unordered). You may assume that if the mass
# of a b-ion is present, then so is that of its complementary y-ion, and viceversa.
# Return a protein string t of length n whose t-prefix and t-suffix weights correspond to the non-parent mass values of L
import time

if __name__ == '__main__':

    # Load mass table
    g = open("Data_files/Monoisotopic_Mass_Table.txt", 'r')
    aac = []
    mass = []
    for line in g:
        div_line = line.split()
        aac.append(div_line[0])
        mass.append(float(div_line[1]))
    min_val = min(mass)

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    mass_values = []
    for line in f:
        mass_values.append(float(line.strip()))
    #mass_values.sort()
    sol = ''
    curr_index = 1
    prot_length = (len(mass_values) - 3) // 2
    while len(sol) < prot_length:
        print(len(sol), sol, prot_length)
        for i in range(curr_index + 1, len(mass_values)):
            print(curr_index, i, mass_values[curr_index], mass_values[i])
            if i <= curr_index or mass_values[i] == 0:
                continue
            if abs(mass_values[i] - mass_values[curr_index]) < (min_val - 0.1):
                print('skip', min_val, abs(mass_values[i] - mass_values[curr_index]), mass_values[i], mass_values[curr_index])
                #time.sleep(1)
                continue
            diff = mass_values[i] - mass_values[curr_index]
            for j in range(len(mass)):
                if abs(diff - mass[j]) <= 0.1:
                    print(aac[j], mass_values[curr_index], mass_values[i])
                    sol = sol + aac[j]
                    corresponding_index = len(mass_values) - curr_index
                    if corresponding_index < 130:
                        time.sleep(2)
                    print("zeroing ", curr_index, corresponding_index, mass_values[curr_index], mass_values[corresponding_index])
                    mass_values[curr_index] = 0
                    mass_values[corresponding_index] = 0
                    print(mass_values)
                    curr_index = i
                    print(sol)
                    break
    print(sol[:(len(mass_values) - 3) // 2])