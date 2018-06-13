initial_amount = 100
p = 5.5                   # interest rate in %
amount = initial_amount
years = 0
while amount <= 1.5*initial_amount:
    amount *= (p/100. + 1)
    years += 1
print years


# a) pocket calulator gave 8 years
# b) the loop run forever because of integer division
# c) placed += and *=
# d) This program finds out how many years it takes for money
   # to reach a certain amount with a fixed interest rate
