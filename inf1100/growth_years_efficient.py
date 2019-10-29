xp = 100           # start money
p = 5              # [%] interest rate
N = 4              # [years]
int_counter = 0    # counter for while loop

outfile = open('growth.dat','w')                       # saving new file growth.dat
outfile.write('Interest rate = %.2f percent\n' % p)    # file heading
outfile.write('year - money\n')                        # table heading
while int_counter <= N:
    outfile.write('   %i %8.2f\n' % (int_counter, xp)) # year and money print, including year 0
    x = (100 + p)/100.*xp
    xp = x
    int_counter += 1
outfile.close()

"""
simen@simen-VirtualBox:~/python/uke7$
"""
