substance = []
density = []
with open("densities.dat","r") as infile:
    infile.readline()
    infile.readline()
    for line in infile:
        line_list = line.split()
        density.append(line_list[-1])
        substance.append(line_list[:-1])
        if len(substance[-1]) > 1:
            substance[-1] = str(substance[-1][0]) + ' ' + str(substance[-1][1])
        elif len(substance[-1]) < 2:
            substance[-1] = str(substance[-1])

for i in range(len(substance)):
    print substance[i], density[i]
