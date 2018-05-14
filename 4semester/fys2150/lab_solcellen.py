import numpy as np
import matplotlib.pyplot as plt


def uncertainties():
    V  = np.array([-0.48356,-0.48380,-0.48371,-0.48394,-0.48425,-0.48414,-0.48405,-0.48388,-0.48394,-0.48410,-0.48414])
    VL = np.array([5.5603,5.5603,5.5603,5.5604,5.5603,5.5604,5.5603,5.5604,5.5603,5.5604,5.5605])
    I = VL/41.19
    I_err = np.std(I)
    V_err = np.std(V)
    return I_err,V_err
    
    
def oppg1(I_err,V_err):
    # oppgave 1a), med spenningskilde
    V   = np.array([-4.9739,-4.8868,-4.6208,-4.3304,-3.1880,0.35036, \
                    0.49979,0.50238,0.50299,0.50341,-2.3025,0.18429,0.46215, \
                    0.47925,0.4980,0.49425,0.49593,0.49660,0.49692,0.49759,0.49811,0.49291, \
                    0.6725,0.5901,0.5378,0.5209,0.5094,0.5024,0.4998,0.4995,0.4996])
    V_L = np.array([-0.093120,-0.18030,-0.44660,-0.73561,-1.8813,-5.4192, \
                    -5.5777,-5.5808,-5.5818,-5.5824,-2.7621,-5.2563,-5.5459,-5.5641, \
                  -5.5762,-5.5811,-5.5831,-5.5836,-5.5841,-5.5848,-5.5854,-5.5797, \
                  4.333,4.466,4.540,4.562,4.576,4.585,4.588,4.588,4.588])
    R_L = np.array([0.6,1.2,3.,5.,13.,45.,666.,2455.,5734.,9999.9,20,40,80, \
                    120,210,333,422,474,505,587,622,350, \
                    3.,8.,28.,58.,137,446,2446,5365,9999])
    I = V_L/R_L #
    print(len(R_L))
    # Oppgave 1b), uten ekstern spenning
    V1   = np.array([0.020530,0.08777,0.31935,0.4525,0.49567,0.49907,0.50167,0.50247,0.50263,0.50266,0.50263,0.50064,0.50104,0.50203,0.524])
    V_L1 = np.array([0.016042,0.083606,0.31554,0.44985,0.495,0.49864,0.50151,0.50243,0.50267,0.50264,0.50254,0.50046,0.50093,0.50198,0.49998])
    R_L1 = np.array([0.1,0.6,2.5,5.4,25.4,47,147,447,724,924,1000,86,116,274,67])
    I1 = V_L1/R_L1
    a = [[-5,2,-0.4,1.6],[0,0.6,-0.25,0.1]]
    for i in range(2):
        plt.title('IV-karakteristikk')
        plt.plot(V1[1:],-I1[1:],'bx',label='Med ekstern spenningskilde')
        plt.errorbar(V,I,xerr=V_err,yerr=I_err,fmt='o')#'rx',label='Uten ekstern spenningskilde')
        plt.grid()
        plt.plot([-5,2],[0,0],'k-',[0,0],[-0.4,1.6],'k-')
        plt.axis(a[i])
        plt.xlabel('Spenning, V, [V]')
        plt.ylabel('Strom, I, [A]')
        plt.legend(loc='best')
        plt.show()


def oppg2():
    # Samme data som fra 1b), uten ekstern spenning
    V1   = np.array([0.020530,0.08777,0.31935,0.4525,0.49567,0.49907,0.524,0.50167,0.50247,0.50263,0.50266,0.50263,0.50064,0.50104,0.50203])
    V_L1 = np.array([0.016042,0.083606,0.31554,0.44985,0.495,0.49864,0.49998,0.50151,0.50243,0.50267,0.50264,0.50254,0.50046,0.50093,0.50198])
    R_L1 = np.array([0.1,0.6,2.5,5.4,25.4,47,67,147,447,724,924,1000,86,116,274])
    I1 = -V_L1/R_L1
    P1 = -I1*V1
    
    # data med redusert belysning
    V2 = np.array([0.0422,0.1093,0.2438,0.3545,0.4552,0.4668,0.4738,0.4739, \
                   0.4743,0.3013,0.3745,0.2337,0.1617,0.4247])
    R2 = np.array([0.6,1.6,3.8,6.5,24,55,533,958,5758,5,7.3,3.6,2.4,11.5])
    I2 = -V2/R2
    P2 = -I2*V2
    i = np.argmax(P1)
    Imax1 = I1[i]
    Vmax1 = V1[i]
    i = np.argmax(P2)
    Imax2 = I2[i]
    Vmax2 = V2[i]
    
    plt.title('Maksimal effekt')
    plt.plot(R_L1,P1,'ro',label='full belysning, $P_{max}$ = %1.3g W' % np.max(P1))
    plt.plot(R2  ,P2,'bo',label='redusert belysning, $P_{max}$ = %1.1g W' % np.max(P2))
    plt.grid()
    plt.legend()
    plt.xlabel('R [$\Omega$]')
    plt.ylabel('P, [W]')
    plt.axis([0,40,-0,0.05]) #NB: Dataene gaar langt hoyere, men dette er 'interessant' omraade
    plt.show()
    plt.title('IV-karakteristikk')
    plt.plot(V1,I1,'ro',label='full belysning')
    plt.plot(V2,I2,'bo',label='redusert belysning')
    plt.plot([0,Vmax1],[Imax1,Imax1],'r-',label='$I_{max},V_{max}$')
    plt.plot([Vmax1,Vmax1],[0,Imax1],'r-')
    plt.plot([0,Vmax2],[Imax2,Imax2],'b-',label='$I_{max},V_{max}$')
    plt.plot([Vmax2,Vmax2],[0,Imax2],'b-')
    plt.grid()
    plt.xlabel('Spenning, V, [V]')
    plt.ylabel('Strom, I, [A]')
    plt.legend(loc='best')
    plt.show()



def oppg3_serie():
    # seriekoblet, en solcelle dekt til
    V2 = np.array([0.000692,0.001796,0.004209,0.006708,0.01043,0.03425,0.07618, \
                   0.1171,0.2463,0.4233])
    R2 = np.array([0.6,1.6,3.8,6.2,9.7,33,78,128,333,778])
    I2 = -V2/R2
    pmax2 = np.max(np.abs(I2*V2))
    
    # seriekoblet med begge solcellene
    V3 = np.array([0.07662,0.1744,0.4551,0.8443,0.9758,0.9924,1.0000,1.0023, \
                   0.2363,0.3583,0.6016,0.6745])
    R3 = np.array([0.6,1.4,3.7,8.9,34.4,87,322,2852,1.9,2.9,5,5.8])
    I3 = -V3/R3
    pmax3 = np.max(np.abs(I3*V3))
    
    plt.title('seriekobling')
    plt.plot(V2,I2,'bo',label='én solcelle tildekt, $P_{max}$ = %1.1e W' % pmax2)
    plt.plot(V3,I3,'ro',label='begge solceller belyst, $P_{max}$ = %1.1e W' % pmax3)
    plt.legend(loc='best')
    plt.grid()
    plt.xlabel('Strom, I, [A]')
    plt.ylabel('Spenning, V, [V]')
    plt.show()
    

def oppg3_parallell():
    # parallellkoblet, en solcelle dekt til
    V4 = np.array([0.0794,0.1163,0.1853,0.3371,0.3947,0.4175,0.4378,0.4563, \
                   0.4583,0.4599,0.2136,0.2742])
    R4 = np.array([0.6,0.9,1.5,3.5,5.6,7.7,12.7,54.7,97.4,224,1.8,2.5])
    I4 = -V4/R4
    pmax4 = np.max(np.abs(I4*V4))

    # parallellkoblet med begge solcellene
    V5 = np.array([0.1410,0.1666,0.2391,0.3358,0.4359,0.4452,0.4591,0.4752,0.4965, \
                   0.3011,0.3968])
    R5 = np.array([0.5,0.6,0.9,1.4,2.6,2.9,3.6,5.3,26.3,1.2,1.9])
    I5 = -V5/R5
    pmax5 = np.max(np.abs(I5*V5))

    plt.title('parallellkobling')
    plt.plot(V4,I4,'bo',label='én solcelle tildekt, $P_{max}$ = %1.1e W' % pmax4)
    plt.plot(V5,I5,'ro',label='begge solceller belyst, $P_{max}$ = %1.1e W' % pmax5)
    plt.legend(loc='best')
    plt.grid()
    plt.xlabel('Strom, I, [A]')
    plt.ylabel('Spenning, V, [V]')
    plt.show()

#I_err,V_err = uncertainties()
#print(I_err,V_err)
#oppg1(I_err,V_err)
oppg2()
#oppg3_serie()
#oppg3_parallell()

"""
pinn = 0.504
effekt = pmax/pinn*100
print(effekt, 'prosent')
"""