x = []
y = []
z = []
t = []
def f():
    with open('data.txt','r') as infile:
        for line in infile:
            a = line.split()
            x.append(float(a[0]))
            y.append(float(a[1]))
        infile.close()

    with open('data.txt','r') as infile:
        for line in infile:
            a = line.split()
            if len(a) == 3:
                t.append(float(a[0]))
                z.append(float(a[2]))
        infile.close()

    from matplotlib.pyplot import plot, show
    plot(x,y,'r-')
    plot(t,z,'bo')
    show()

def dump_data(filename,x,y,z):
    with open(filename,'w') as outfile:
        for i in range(len(x)):
            outfile.write('%9.6g %9.2g' % (x[i],y[i]))
            if z[i] != None:
                outfile.write('%9.4f')
            outfile.write('\n')
    outfile.close()

" Monte Carlo "
import numpy as np

N = 100000
m = 0
for i in range(N):
    g = np.random.random_integers(0,1,20)
    if sum(g) >= 15:
        m += 400
    m -= 10

print m/float(N), 'profit per game'
if m/float(N) < 0:
    print 'not profitable in the long run'
else:
    print 'profitable in the long run'
