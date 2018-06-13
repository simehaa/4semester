# a)

def read_split_join():                 # first method, with the split function
    infile = open('densities.dat','r')
    substance = []
    densities = []
    for line in infile:
        words = line.split()
        value = words[-1]
        del words[-1]           # remove the last element: number value
        densities.append(value)
        name = ' '.join(words)  # then I join (if any) words separated by space
        substance.append(name)
    infile.close()
    return substance, densities

# b)

def read_divideline():                 # second method where I divide the entire line
    infile = open('densities.dat','r')
    substance = []
    densities = []
    for line in infile:
        left = line[:11]               # split after the 11th symbol
        right = line[11:]
        name = left.strip()            # stripping of whitespaces
        value = right.strip()
        substance.append(name)
        densities.append(value)
    infile.close()
    return substance, densities

# c) test function


def test_func():    # in this test function I test all values and names
    sub   = read_split_join()[0]
    den   = read_split_join()[1]
    sub_1 = read_divideline()[0]
    den_1 = read_divideline()[1]
    success = True
    for i in range(len(sub)):     # success will become False if any of the tests fail
        if sub[i] != sub_1[i]:    # then a message will be printed, showing which line
            success = False       # the fail were, and what the two readings were
            msg = 'function did not read the same way, line %i in file: <%s>;<%s>' % (i+1,sub[i],sub_1[i])
        elif den[i] != den_1[i]:
            success = False
            msg = 'function did not read the same way, line %i in file: <%s>;<%s>' % (i+1,den[i],den_1[i])
    assert success, msg

test_func()

"""
simen@simen-VirtualBox:~/python/uke8$
"""
