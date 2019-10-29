from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def autocorrelation(Fs,N):
    T = N/Fs
    t = np.linspace(0, T*(N-1)/N, N)
    f = np.linspace(0, Fs*(N-1)/N, N)
    fsenter = 5000
    fsigma = 3000

    A = np.random.rand(N)
    gauss = A*np.exp(-((f-fsenter)/fsigma)**2)
    faser = 2*np.pi*np.random.rand(N)
    y_freq = gauss*(np.cos(faser) + 1j*np.sin(faser))

    for k in range(1,int(N/2) - 1):
        y_freq[N-k] = np.conj(y_freq[k])

    y_freq[int(N/2)] = np.real(y_freq[int(N/2)])
    y_freq[0] = 0

    y_time = np.real(np.fft.ifft(y_freq))*200

    l = t[-1]
    t1 = np.linspace(-l,l,N)
    cor = np.correlate(y_time,y_time,'same')/np.sum(y_time**2)

    i1 = int(N/2)
    plt.figure()
    plt.subplot(211)
    plt.title('entire time')
    plt.plot(t1[i1:],np.absolute(cor[i1:]))
    plt.ylabel('auto correlation, rel. unit')
    plt.grid()
    plt.subplot(212)
    plt.title('segment along the time axis')
    plt.plot(t1[i1:i1+25],np.absolute(cor[i1:i1+25]))
    plt.xlabel('time [s]')
    plt.ylabel('auto correlation, rel. unit')
    plt.grid()
    plt.show()
    return(t,y_time,f,y_freq)


def wavelet(t,y_time,f,N,K=32,fmin=100,fmax=12000):
    N_wa = 1500
    w = f
    wa = np.linspace(fmin,fmax,N_wa) # frequency limits
    Q = np.exp(-K**2) # efficiency in calulations
    freq_fft = np.fft.fft(y_time,N)
    M = np.zeros((N_wa,N))

    def morlet_fft(K,w,wa):
        return 2*(np.exp(-(K*(w-wa)/wa)**2) - Q*np.exp(-(K*w/wa**2)))

    for i in range(N_wa):
        M[i,:] = np.sqrt(np.abs(np.fft.ifft( morlet_fft(K,w,wa[i]) * freq_fft )))

    plt.pcolormesh(t,wa,M,cmap='jet')
    plt.colorbar()
    plt.title('K=%i' % K)
    plt.ylabel('frequency [Hz]')
    plt.xlabel('time [s]')
    plt.show()


def fourier(t,y_time,f,N):
    y_freq = np.fft.fft(y_time)
    plt.figure()
    plt.title('Fourier analysis')

    plt.subplot(211)
    plt.plot(t,y_time)
    plt.xlabel('time [Hz]')
    plt.ylabel('amplitude')
    plt.grid()

    plt.subplot(212)
    plt.plot(f[:int(N/2)],np.real(y_freq[:int(N/2)])) # first half due to aliasing
    plt.xlabel('frequency [Hz]')
    plt.ylabel('amplitude')
    plt.grid()
    plt.show()

Fs = 44100
N  = 2**13

t,y_time,f,y_freq = autocorrelation(Fs,N)
fourier(t,y_time,   f,N)
fourier(t,y_time**2,f,N)
wavelet(t,y_time,f,N)
wavelet(t,y_time**2,f,N,K=32,fmax=22000)

"""
[Command: python -u /home/simen/github/university/4semester/fys2130/oblig6.py]
[Finished in 120.16s]
"""
