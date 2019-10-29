import numpy as np
import matplotlib.pyplot as plt
import glob, os

for filename in glob.glob('wvpt_*.png'):  # removal of old files
    os.remove(filename)

def f(x,t):
    return (np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t)))

plt.ion()                   # interactive mode on
x = np.linspace(-6,6,1001)  # x array
y = np.zeros(1001)          # y array
time = np.linspace(-1,1,61) # time array for the gif
lines = plt.plot(x,y)

counter = 0
for t in time:  # matplotlib.pyplot setup for movie making in a for loop
    y = f(x,t)
    lines[0].set_ydata(y)
    plt.title('wavepacket')
    plt.xlabel('time')
    plt.ylabel('position')
    plt.axis([-6,6,-1.6,1.6])
    plt.draw()
    # plt.savefig('wvpt_%04d.png' % counter)
    counter += 1

cmd = 'convert -delay 8 wvpt_*.png wavepacketmovie.gif'  # the gif is saved, and is viewable, the gif looks 'correct' as one wave moving along the axis
os.system(cmd)

"""
simen@simen-VirtualBox:~/python/uke7$ python plot_wavepacket_movie.py

"""
