import matplotlib.pyplot as plt

t = []
v = []
infile = open('running.txt','r')
for line in infile:
    tnext, vnext = line.strip().split(',')
    t.append(float(tnext))
    v.append(float(vnext))
infile.close()

a = []
s = []
distance = 0
for i in range(len(t) - 1):
    dt = (t[i + 1] - t[i])
    dv = (v[i + 1] - v[i])
    a.append(float(dv)/dt)
    distance += dt*(v[i] + dv/2.)
    s.append(distance)

del t[-1]
plt.plot(t, a, label='akselerasjon')
plt.xlabel('tid')
plt.legend()
plt.show()

plt.plot(t, s, label='avstand')
plt.xlabel('tid')
plt.legend()
plt.show()
