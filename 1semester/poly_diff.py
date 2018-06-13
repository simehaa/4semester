def diff(poly):
    dp = {}
    for j in poly:
        if j != 0:
            dp[j-1] = j*poly[j]
    return dp


p = {5: 4,4: 3,3: 2,1: 1,0: 8}
print diff(p)



# 3*x + 5*x**4 + 7*x**2
# expected: 3 + 20*x**3 + 14*x
"""
simen@simen-VirtualBox:~/python/uke8$ python poly_diff.py
{0: 3, 1: 14, 3: 20}
"""
