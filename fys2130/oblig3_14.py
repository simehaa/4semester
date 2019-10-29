import numpy as np
import matplotlib.pyplot as plt

def fourier(frequency,N,square=False):
    dt = 1./N
    t = np.linspace(0,1,N)
    y = np.sin(2*np.pi*frequency*t)
    if square == True:
        y[y >= 0] = 1
        y[y < 0] = -1

    yf = np.fft.fft(y)*2./N
    xf = np.fft.fftfreq(int(N),dt)

    plt.figure()
    plt.subplot(311)
    plt.title("opprinnelig signal, frekvens = %2.1f Hz" % frequency)
    plt.plot(t,y)
    plt.xlabel("t [s]")
    plt.ylabel("Amplitude")

    plt.subplot(312)
    plt.title("fast fourier transformasjon")
    plt.plot(xf,np.real(yf),label="real part")
    plt.plot(xf,np.imag(yf),label="imaginary part")
    plt.xlabel("frekvenser [Hz]")
    plt.ylabel("Amplitude")
    plt.legend()

    plt.subplot(313)
    plt.title("fast fourier transformasjon")
    plt.plot(xf,np.real(yf),label="real part")
    plt.plot(xf,np.imag(yf),label="imaginary part")
    plt.xlabel("frekvenser [Hz]")
    plt.ylabel("Amplitude")
    plt.axis([-400,400,-1.5,1.5])
    plt.legend()
    plt.show()

# fourier(13.0,512) # oppgave 14
# fourier(13.2,512) # oppgave 15
fourier(16,2**14,square=True) # oppgave 16
