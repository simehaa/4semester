from project7 import water_drops
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    """
    Part 1: a closer look on the time intervals
    between each drop for four different psi values
    """

    psis = [0.00073,0.00065,0.00063,0.00060]
    plt.figure()
    plt.title('Distribution of frequencies between water drops')
    for i in range(4):
        psi = psis[i]
        oppgave8 = water_drops(psi=psi)
        oppgave8.solve()
        diff = np.diff(oppgave8.droptimes)


        if i == 0:
            ax1 = plt.subplot(414)
            plt.xlabel('frequency [Hz]')
        else:
            ax2 = plt.subplot(414 - i, sharex = ax1)
            plt.setp(ax2.get_xticklabels(),visible=False)
            if i == 2:
                plt.ylabel('relative occurance')
        freqdrops = 1./diff

        n = 501
        freqs = np.linspace(5,12,n) # frequency array between 5 - 12 Hz
        y = np.zeros(n) # relative occurance of frequency
        for k in range(len(freqdrops)):
            f = freqdrops[k]
            for j in range(n - 1):
                if freqs[j] < f < freqs[j + 1]:
                    y[j] += 1

        y *= 1/np.max(y)
        plt.plot(freqs,y,label='psi=%f' % psi)
        plt.legend()
        plt.grid()
    plt.show()

    """
    Part 2: Comparing 100 different psi values in a
    single plot, to see the chaotic development of the
    number of attractors
    """

    n_p = 100
    psis = np.linspace(0.00055,0.00075,n_p)
    for j in range(n_p):
        psi = psis[j]
        oppgave8 = water_drops(psi=psi)
        oppgave8.solve()
        for s in range(50):
            diff = np.diff(oppgave8.droptimes[-51:])
            plt.plot(50*[psi*1000],diff,'k.')

    plt.title('drop intervals with different $\psi$')
    plt.xlabel('$\psi \cdot 10^3$ [kg/s]')
    plt.ylabel('time between each of the 50 last drops [s]')
    plt.grid()
    plt.show()

"""
[Command: python -u /home/simen/github/university/4semester/fys2130/project8.py]
[Finished in 250.15s]
"""
