q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
# a)
  # 1)
print q[0][0]
  # 2)
print q[1]
  # 3)
print q[2][1]
  # 4)
print q[1][0]
  # [-1] refers to the last element ['g', 'h'] and [-2]
  # refers to the second last element in that list: 'g'
# b)
for i in q:
    for j in range(len(i)):
        print i[j]

# i is the index in q (0, 1 and 2)
# j is the index in each element i q
# first big loop: i = 0, and j finds each element in the list
# where i = 0, for the length 3 in this case, j = a, b then c
