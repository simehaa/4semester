F = 0
print 'Fahrenheit | Celsius | Approx_Celsius'  # headline print
while F <= 150:                 # making loop for F from 0 to 150
    C = (F - 32)*5./9           # F to C formula
    C_approx = (F - 30)/2.0     # F to C approximate formula
    F += 10                     # increment
    print '%7.1f F  | %5.1f C | %5.1f C' % (F, C, C_approx)  # table print

"""
simen@simen-VirtualBox:~/python/uke3$ python f2c_approx_table.py
Fahrenheit | Celsius | Approx_Celsius
   10.0 F  | -17.8 C | -15.0 C
   20.0 F  | -12.2 C | -10.0 C
   30.0 F  |  -6.7 C |  -5.0 C
   40.0 F  |  -1.1 C |   0.0 C
   50.0 F  |   4.4 C |   5.0 C
   60.0 F  |  10.0 C |  10.0 C
   70.0 F  |  15.6 C |  15.0 C
   80.0 F  |  21.1 C |  20.0 C
   90.0 F  |  26.7 C |  25.0 C
  100.0 F  |  32.2 C |  30.0 C
  110.0 F  |  37.8 C |  35.0 C
  120.0 F  |  43.3 C |  40.0 C
  130.0 F  |  48.9 C |  45.0 C
  140.0 F  |  54.4 C |  50.0 C
  150.0 F  |  60.0 C |  55.0 C
  160.0 F  |  65.6 C |  60.0 C
"""
