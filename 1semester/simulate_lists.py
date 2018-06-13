a = [1, 3, 5, 7, 11]   # defining list a
b = [13, 17]           # defining list b
c = a + b              # adding a and b
print c                # printing out the new list c
b[0] = -1              # -1 for the first element in b
d = [e+1 for e in a]   # a new list d where each element is +1 from a
print d                # printing d
d.append(b[0] + 1)     # adding the first element from b + 1 to d
d.append(b[-1] + 1)    # adding the last element from b + 1 to d
print d[-2:]           # printing list d from the second last to the last element
for e1 in a:           # nested list
    for e2 in b:       # adding and printing a1 + b1 ...
        print e1 + e2
