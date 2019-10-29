print 'Length conversion'
m = float(3200) # input value
print '%.1f meter(s) equals to' % (m) # intro, shows input
inch = m/0.0254 # meter -> inch calculation
print '%.2G inches' % (inch) # output 1
f = inch/12
print '%.2f feet' % (f) # output 2
yard = f/3
print '%.2f yards' % (yard) # output 3
km = m/1000
print '%.2f kilometers' % (km) # output 4
mile = m/1609.344
print '%.4G miles' %(mile) # output 5
