import time
t0 = time.time()
while time.time() - t0 < 3:
    print 'Zzz'
    time.sleep(1)                         # adds 1 second
print 'Beep Beep Beep! time to wake up'
