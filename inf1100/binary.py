a = raw_input("Number to be converted: ")
a = int(a)
b = raw_input("Numeral system (up to 16): ")
b = int(b)

if b == 2:
    print "Binary"
elif b == 3:
    print "Ternary"
elif b == 4:
    print "Quaternary"
elif b == 5:
    print "Quinary"
elif b == 6:
    print "Senery"
elif b == 8:
    print "Octal"
elif b == 12:
    print "Duodecimal"
elif b == 16:
    print "Hexadecimal"

while a > 0:
    d = a%b
    a = a//b
    if d == 10 : d = 'a'
    elif d == 11 : d = 'b'
    elif d == 12 : d = 'c'
    elif d == 13 : d = 'd'
    elif d == 14 : d = 'e'
    elif d == 15 : d = 'f'
    print d;
