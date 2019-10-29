import numpy as np                    # import of numpy and matplotlib.pyplot
import matplotlib.pyplot as plt

N = 2                                 # only need two values because both functions are linear
F = np.linspace(-20,120,N)            # vectorized fahrenheit array
C_simple = np.zeros(N)                # empty celsius arrays
C_exact = np.zeros(N)

for i in range(N):
    C_simple[i] = (F[i] - 30)/2.      # giving the simple array values
    C_exact[i] = (F[i] - 32)*5/9.     # giving the exact array values

plt.plot(F,C_simple, 'g-', label='Simple conversion formula')  # plot with color and label
plt.plot(F,C_exact, 'b-', label='Exact conversion formula')
plt.xlabel('Fahrenheit')              # label on the x axis
plt.ylabel('Celsius')                 # label on the y axis
plt.title('Fahrenheit to Celsius')    # plot headline
plt.legend(loc='best')                # the legend box, which allows me to give the two graphs names in a box, location is set to best
plt.show()
