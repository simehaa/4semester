import numpy as np
import matplotlib.pyplot as plt

N = 500
x_short = np.linspace(0.001,0.1,N) # x array for short wavelengths
x_long = np.linspace(1,2000,N)     # x array for longer wavelengths
y_short = np.zeros(N)              # two empty y arrays
y_long = np.zeros(N)

def f(wavelength):  # the function
    g = 9.81    # [m/s**2]  - gravitational acceleration
    s = 7.9e-2  # [N/m]     - air-water surface tension
    p = 1000    # [kg/m**3] - water density
    h = 50      # [m]       - water depth
    return (np.sqrt((g*wavelength)/(2*np.pi)* \
           (1 + s*(4*np.pi**2)/(p*g*wavelength**2))\
           *np.tanh((2*np.pi*h)/(wavelength))))

for i in range(N):  # giving the two y arrays values from the function
    y_short[i] = f(x_short[i])
    y_long[i] = f(x_long[i])

plt.plot(x_short,y_short, label='short wavelengths') # plot for short wavelengths
plt.xlabel('wavelength (m)')                         # name on axis
plt.ylabel('water wave velocity (m/s)')
plt.axis([0,0.101,0.2,0.8])
plt.title('wave speed of water surface')             # title for the plot
plt.legend(loc='best') # legend box, allows the plot label, located at the best location
plt.show()

plt.plot(x_long,y_long, label='long wavelengths') # plot for longer wavelengths
plt.xlabel('wavelength (m)')
plt.ylabel('water wave velocity (m/s)')
plt.title('wave speed of water surface')
plt.legend(loc='best')
plt.show()
