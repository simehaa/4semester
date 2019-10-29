print '---Fahrenheit-to-Celsius---'
F = 0
while F <= 100:
    C = (F - 32)*5./9
    print '%3.0f %3.1f' % (F, C)
    F += 10
print '---------------------------'

v0 = 5.0
g = 9.81

n = 5

t_stop = 2*v0/g
dt = t_stop/n

for i in range(0,n + 1):
    t = i*dt
    y = v0*t-0.5*g*t**2
    print '%5.2f - %3.1f' % (t, y)

print '---------------------------'

t = 0
while t <= t_stop:
    y = v0*t-0.5*g*t**2
    print '%5.2f - %3.1f' % (t, y)
    t += dt

print '---------------------------'
