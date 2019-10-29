# sum all integers from 1 to n
n = raw_input("the sum of all integers \nfrom 1 to ")
n = int(n)
s = 0
for i in range(1, n + 1):
    s += i
print ' = %i' %s
