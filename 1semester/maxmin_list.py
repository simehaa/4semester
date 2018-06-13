a_list = [1, 3, 4, 10, 2, 100, 1.4, 1.9]

def maxel(a):
    max_elem = a[0]
    for elem in a:
        if elem > max_elem:
            max_elem = elem
    return max_elem

print maxel(a_list)

def minst(a):
    min_elem = a[0]
    for elem in a:
        if elem < min_elem:
            min_elem = elem
    return min_elem

print minst(a_list)
