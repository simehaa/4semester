# a)

def readfile(filename):
    t = []
    with open(filename,'r') as infile:    # open file from function argument
        line = infile.readline()
        first_line_list = line.split()    # splitting the first line into a list
        v0 = eval(first_line_list[-1])    # v0 is found as the last object on the first line
        infile.readline()                 # the second line (which I don't need)
        for line in infile:               # reading lines with information
            a = line.split()              # split each object in the line into a list
            for i in range(len(a)):       # reading each object in a line
                t.append(float(a[i]))     # appending each value to the list t
        return v0, t

print readfile("ball.dat")                # print a tuple containing a float and a list

# b)

def test_readfile():
    outfile = open('test.dat','w')        # writing a file
    t_test = [4.1, 1234.4, 590.1]         # some random t values
    v0_test = 5.01                        # a random v0 value

    outfile.write("v0: %.2f\nt:\n" % v0_test)  # the writing in the file which has the same format as ball.dat
    for i in range(len(t_test)):
        outfile.write('%.1f ' % float(t_test[i])) # writing t values on the next lines
    outfile.close()

    v0 = readfile("test.dat")[0]          # obtaining v0 from test.dat using the first function readfile()
    t  = readfile("test.dat")[1]          # obtaining t
    msg_v = "float fail: v0=%.2f v0_test=%.2f" % (v0, v0_test)  # fail message for v0
    success_v = abs(v0 - v0_test) < 1e-14
    assert success_v, msg_v               # assertion test for v0
    for i,j in zip(t, t_test):
        msg_t = "list fail: i = %.1f and j = %.1f" % (float(i), float(j))   # fail message for t
        success_t = abs(i - j) < 1e-14
        assert success_t, msg_t           # assertion test for t

test_readfile()  # calling test function

# c)

def position():
    v0_ = float(readfile("ball.dat")[0])  # getting v0 from function in a)
    g = 9.81
    t_results = readfile("ball.dat")[1]   # t from a)
    t_results.sort()                      # sort t values in increasing order
    outfile = open('ball_results.dat', 'w') # wrtiting the new file
    outfile.write("__time__|_height__\n")   # Headline
    for i in range(len(t_results)):
        t_ = float(t_results[i])
        position = (v0_*t_ - 0.5*g*t_**2)  # calculation of height
        outfile.write("%5.2f s | %6.3f m\n" % (t_, position))  # table for the file
    outfile.close()                        # closing the file, necessary for writing to work

position()                                # calling the function, also necessary for the creation of the new file

# terminal print (checking that the function in "a)" give v0 and a list of t)
"""
simen@simen-VirtualBox:~/python/uke5$ python ball_file_read_write.py
(3.0, [0.15592, 0.28075, 0.36807889, 0.35, 0.57681501876, 0.21342619, 0.0519085, 0.042, 0.27, 0.50620017, 0.528, 0.2094294, 0.1117, 0.53012, 0.372985, 0.39325246, 0.21385894, 0.3464815, 0.57982969, 0.10262264, 0.29584013, 0.17383923])
"""
# ball_results.dat
"""
__time__|_height__
 0.04 s |  0.117 m
 0.05 s |  0.143 m
 0.10 s |  0.256 m
 0.11 s |  0.274 m
 0.16 s |  0.349 m
 0.17 s |  0.373 m
 0.21 s |  0.413 m
 0.21 s |  0.417 m
 0.21 s |  0.417 m
 0.27 s |  0.452 m
 0.28 s |  0.456 m
 0.30 s |  0.458 m
 0.35 s |  0.451 m
 0.35 s |  0.449 m
 0.37 s |  0.440 m
 0.37 s |  0.437 m
 0.39 s |  0.421 m
 0.51 s |  0.262 m
 0.53 s |  0.217 m
 0.53 s |  0.212 m
 0.58 s |  0.098 m
 0.58 s |  0.090 m
"""
