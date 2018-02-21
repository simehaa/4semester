import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def fourier(frequency,points,square=False):
    N = points
    dt = 1./N
    t = np.linspace(0,1,N)
    y = np.sin(2*np.pi*frequency*t)
    if square == True:
        y[y >= 0] = 1
        y[y < 0] = -1

    yf = np.fft.fft(y)*2./N
    xf = np.fft.fftfreq(int(N),dt)#np.linspace(0,(N-1)*dt,N/2)

    plt.figure()
    plt.subplot(211)
    plt.title("opprinnelig signal, frekvens = %2.1f Hz" % frequency)
    plt.plot(t,y)
    plt.xlabel("t [s]")
    plt.ylabel("Amplitude")

    plt.subplot(212)
    plt.title("fast fourier transformasjon")
    plt.plot(xf,np.real(yf),label="real part")
    plt.plot(xf,np.imag(yf),label="imaginary part")
    plt.xlabel("frekvenser [Hz]")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.show()

fourier(13.0,512)
fourier(13.2,512)
fourier(16,2**14,square=True)
