import numpy as np
import matplotlib.pyplot as plt


def plot_flux_lambda(t,l,f,fignumber):
    plt.figure()
    plt.subplot(211)
    plt.plot(t,l,'b,')
    plt.ylabel("wavelength [nm]")
    plt.ticklabel_format(useOffset=False)
    plt.grid(True)
    plt.title("Data for star%i" % fignumber)
    plt.subplot(212)
    plt.plot(t,f,'c,')
    plt.xlabel("time [d]")
    plt.ylabel("relative flux")
    plt.ticklabel_format(useOffset=False)
    plt.grid(True)
    plt.savefig('c4_flux_lambda_figure_%i' % fignumber,bbox_inches='tight')
    plt.close()


def plot_velocity(t,v,fignumber,t_,v_):
    plt.title('radial velocity for star%i' % fignumber)
    try:
        plt.plot(t_,v_,'r-')
    except:
        pass
    plt.plot(t,v,'m,')
    plt.xlabel("time [d]")
    plt.ylabel("radial velocity [m/s]")
    plt.grid(True)
    plt.savefig('c4_velocity_figure_%i.png' % fignumber)
    plt.close()


def read(filename):
    infile = open(filename,'r')
    t,l,f = [],[],[] # time, lambda, flux
    for line in infile:
        a = line.split()
        t.append(eval(a[0]))
        l.append(eval(a[1]))
        f.append(eval(a[2]))
    infile.close()
    t = np.array(t); l = np.array(l); f = np.array(f)
    return t,l,f


def planetmasses(filenames,n=20):
    c = 299792458.
    Ms = [1.06,0.96,1.53,6.18,2.06] # star masses in solar masses
    # read from the graphs, adjusted with smaller intervals after results (not automated adjustment)
    v_sr =  [9.8,  11.5, 7.88,0,0]
    P =     [3888, 3854, 4444,0,0]
    t0 =    [2350, 4515, 1235,0,0]
    tmin  = [2200, 4400, 1150] # in days!
    tmax  = [2300, 4600, 1250]
    vrmin = [8.5,   9.5,   8]
    vrmax = [9.5,   17,   9]
    pmin  = [3900, 4400, 4400] # in days!
    pmax  = [4030, 4700, 5000]

    def least_mass(star_mass,star_rad_vel,period):
        G = 6.67e-11
        period *= 24*60*60
        return (star_mass*1.99e30)**(2/3.)*star_rad_vel*period**(1/3.)/(2*np.pi*G)**(1/3.)

    for i in range(len(filenames)):
        t,l,f = read(filenames[i])
        plot_flux_lambda(t,l,f,i)
        l0 = 656.3 # [nm] lambda_0
        v = (l-l0)*c/l0
        vp = np.average(v) # peculiar velocity
        vr = v - vp # radial velocity
        planetmass_estimate = least_mass(Ms[i],v_sr[i],P[i])
        if planetmass_estimate > 0:
            t0_,vr_,p_ = least_square(n,t,v,tmin[i],tmax[i],vrmin[i],vrmax[i],pmin[i],pmax[i])
            plot_velocity(t,vr,i,t,vr_*np.cos((t-t0_)*2*np.pi/p_))
            newmass = least_mass(Ms[i],vr_,p_)
            print "star%i, mass is greater that:\nestimate by eye: %e \nleast square: %e, t0 = %.f, vr = %.f, P = %.f" % (i,planetmass_estimate,newmass,t0_,vr_,p_)
        else:
            plot_velocity(t,vr,i,False,False)
            print "star%i, does not appear to have a orbiting planet" % i


def least_square(n,t,v,tmin,tmax,vrmin,vrmax,pmin,pmax):
    t0 = np.linspace(tmin,tmax,n)
    vr = np.linspace(vrmin,vrmax,n)
    p = np.linspace(pmin,pmax,n)
    err_p = 1e16; t0_ = tmin; vr_ = vrmin; p_ = pmin
    for T in t0: # finding which function gives the smallest error
        for V in vr:
            for P in p:
                v_mod = V*np.cos((t-T)*2*np.pi/P)
                err = np.sum((v_mod-v)**2)
                if err < err_p:
                    t0_ = T; vr_ = V; p_ = P # using the best values
                    err_p = err
    return t0_,vr_,p_


if __name__ == '__main__':
    filenames = ['star0_1.06.txt','star1_0.96.txt','star2_1.53.txt','star3_6.18.txt','star4_2.06.txt']
    planetmasses(filenames)


"""
[Command: python -u /home/simen/ast2000/1C4.py]
star0, mass is greater that:
estimate by eye: 1.497305e+27
least square:    1.376489e+27
star1, mass is greater that:
estimate by eye: 1.639912e+27
least square:    1.788481e+27
star2, mass is greater that:
estimate by eye: 1.607743e+27
least square:    1.626821e+27
star3, does not appear to have a orbiting planet
star4, does not appear to have a orbiting planet
[Finished in 23.257s]
"""
