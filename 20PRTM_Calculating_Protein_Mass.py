# Given
if __name__ == '__main__':

    aac_mass = {'A' : 71.03711, 'C' : 103.00919, 'D' : 115.02694, 'F' : 147.06841,
                'G' : 57.02146, 'H' : 137.05891, 'I' : 113.08406, 'K' : 128.09496,
                'E' : 129.04259, 'L' : 113.08406, 'M' : 131.04049, 'N' : 114.04293,
                'P' : 97.05276, 'Q' : 128.05858, 'R' : 156.10111, 'S' : 87.03203,
                'T' : 101.04768, 'V' : 99.06841, 'W' : 186.07931, 'Y' : 163.06333}

    myfile = input('Enter file name: ')
    myfile = 'Data_files/' + myfile + '.txt'
    f = open(myfile, "r")
    protein = f.readline().strip()
    mass = 0
    for aac in protein:
        mass = mass + float(aac_mass[aac])
    print(mass)