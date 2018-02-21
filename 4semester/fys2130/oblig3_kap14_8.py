import numpy as np
import matplotlib.pyplot as plt

N = 8192
f1 = 1000.
f2 = 1600.
c1 = 1.
c2 = 1.7
fs = 10000.
dt = 1/fs
t = np.linspace(0,N*dt,N)
f = c1*np.sin(2*np.pi*f1*t) + c2*np.sin(2*np.pi*f2*t)

yf = np.fft.fft(f)*2./N
xf = np.fft.fftfreq(int(N),dt)
"""
plt.figure()
plt.subplot(211)
plt.title("opprinnelig signal, f = %1.1fsin(2pi*%4.0f*t) + %1.1fsin(2pi*%4.0f*t)" % (c1,f1,c2,f2))
plt.plot(t[:N/64],f[:N/64])
plt.xlabel("t [s]")
plt.ylabel("Amplitude")

il = np.abs(xf-900).argmin()
ir = np.abs(xf-1700).argmin()
plt.subplot(212)
plt.title("fast fourier transformasjon")
plt.plot(xf[il:ir],np.real(yf)[il:ir],label="real part")
plt.plot(xf[il:ir],np.imag(yf)[il:ir],label="imaginary part")
plt.xlabel("frekvenser [Hz]")
plt.ylabel("Amplitude")
plt.legend()
# plt.show()f
"""
