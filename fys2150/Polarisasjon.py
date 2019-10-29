import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

Radian=np.pi/180

###Oppgave1 data

Vinkler_1	= np.array((0, 15, 30, 45, 60, 75, 90))
Lux_1		= np.array((446, 448, 454, 463, 472, 478, 480))


###Oppgave2 data

Vinkler_2 	= np.array((0, 10, 20, 30, 40, 50, 60, 70, 80, 90))
Lux_2		= np.array((156, 153, 141, 121, 97, 70, 45, 23, 8, 3))


###Oppgave3 data

Vinkler_3	= Vinkler_2
Lux_3		= np.array((2, 4, 8, 14, 17, 17, 13, 8, 3, 2))


####Usikkerheter for alle maalinger###
#0.5grad for alle (for lite?)
d_vinkler_1	= np.ones(7)*0.5 
d_vinkler_2	= np.ones(10)*0.5
d_vinkler_3	= np.ones(10)*0.5


#5 prosent plus 2 digits fra brukermanualen (in range 0-1,999 lux)
d_lux_1		= np.sqrt((Lux_1*0.05)**2 + 2**2)
d_lux_2		= np.sqrt((Lux_2*0.05)**2 + 2**2)
d_lux_3		= np.sqrt((Lux_3*0.05)**2 + 2**2)


plt.errorbar(Vinkler_1,Lux_1,  yerr=d_lux_1, xerr=d_vinkler_1, fmt="ro")
plt.grid()
plt.axis([-3,93,0,510])
plt.title("Ett polarisasjonsfilter")
plt.xlabel("Vinkel til polarisasjonsfilteret [$^o$]")
plt.ylabel("Illuminans [lx]")
plt.figure()

x =np.linspace(0,90, 200)
#cos2=156*np.cos(x_*Radian)**2
#def f(x,a,b,c):
#    return (a*np.cos(x*b))**2 + c
def f(x,a,c):
    return a*(np.cos(x*np.pi/180))**2 + c
popt, pcov = curve_fit(f,Vinkler_2,Lux_2,bounds=([150,0],[160,3]))
plt.plot(x, f(x, *popt),'k-',label=r'Kurvetilpasning: $a \cdot cos^2(\theta_1) + c$')
plt.errorbar(Vinkler_2, Lux_2, yerr=d_lux_2, xerr=d_vinkler_2, fmt="r.", label="Målepunkter")
#plt.plot(x_, cos2, "k-", label="$\\cos^2$")
plt.legend()
plt.xlabel(r"Vinkel mellom polarisasjonsfiltrene, $\theta_1$ [$^o$]")
plt.ylabel("Illuminans [lx]")
plt.title("To polarisasjonsfiltre")
plt.grid()
plt.figure()

def f(x,a,c):
    return a*(np.sin(x*np.pi/180)*np.cos(x*np.pi/180))**2 + c
popt, pcov = curve_fit(f,Vinkler_3,Lux_3,bounds=([60,0],[80,3]))
plt.plot(x, f(x, *popt),'k-',label=r'Kurvetilpasning: $a \cdot cos^2(\theta_2)sin^2(\theta_2) + c$')
plt.xlabel(r"Vinkel til det midterste polarisasjonsfilteret, $\theta_2$ [$^o$]")
plt.ylabel("Illuminans [lx]")
plt.title(r"Tre polarisasjonsfiltre, med $\theta_1 = 0^\circ$ og $\theta_3 = 90^\circ$")
plt.grid()

plt.errorbar( Vinkler_3,Lux_3, yerr=d_lux_3, xerr=d_vinkler_3, fmt="ro",label="Målepunkter")
plt.legend()
plt.show()



