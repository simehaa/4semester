import numpy as np
import matplotlib.pyplot as plt
# import sys
# degree = sys.argv[1]

infile = open('lab3_dat1.txt','r')
x,y = [],[]
for line in infile:
    a = line.split()
    x.append(eval(a[0]))
    y.append(eval(a[1])) #(sum([eval(i) for i in a[1:]])/(len(a[1:])))
infile.close()
x = np.array(x)
y = np.array(y)


b = np.polyfit(x,y,1)
t = np.linspace(np.min(x),np.max(x),100)
plt.plot(t,np.polyval(b,t))
plt.plot(x,y,'ko')
# plt.xlabel('B')
# plt.ylabel('V')
plt.grid()
plt.show()
