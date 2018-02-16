class Polynomial(object):
    """Takes one argument, a list of coefficients to the 
    polynomial starting from constant, x, x**2 and so on"""
    def __init__(self,list_of_coefficients):
        self.list = list_of_coefficients
        
    def __call__(self,x):
        f = 0
        for i in range(len(self.list)):
            f += self.list[i]*x**i
        return f
    
    def __add__(self,other):
        a = len(self.list)
        b = len(other.list)
        if a >= b:
            new = self.list[:]
            for i in range(b):
                new[i] += other.list[i]
        else:
            new = other.list[:]
            for i in range(a):
                new[i] += self.list[i]
        return new
    
    def __sub__(self,other):
        a = len(self.list)
        b = len(other.list)
        if a >= b:
            new = self.list[:]
            for i in range(b):
                new[i] -= other.list[i]
        else:
            new = other.list[:]
            for i in range(b):
                new[i] *= -1
            for i in range(a):
                new[i] += self.list[i]
        return new
    
    def __mul__(self,k):
        new = self.list[:]
        for i in range(len(self.list)):
            new[i] *= k
        return new
    
    def __repr__(self):
        r = ''
        n = len(self.list)
        for i in range(n):
            coeff = self.list[i]
            if coeff > 0:
                r += '+ %ix**%i ' % (abs(coeff),i)
            elif coeff == 0:
                pass
            else:
                r += '- %ix**%i ' % (abs(coeff),i)
        if r.startswith('+ '):
            r = r[2:]
        r1 = r.replace('x**1','x')
        r2 = r1.replace('x**0','')
        return r2[:-1]
        

    def __eq__(self,other):
        if self.list == other.list:
            return True
        
    def coefficients(self):
        return self.list
        
    def degree(self):
        return len(self.list) - 1

if __name__ == '__main__':
    a = Polynomials([1,2,-3])
    b = Polynomials([-4,0,2,5])
    print(a+b)
    print(a-b)
    print(a*-1)
    print(repr(b))
    print(b.degree())
    print(b.coefficients())
    if a == b:
        print('somethings wrong...')
    c = Polynomials([1,2,-3])
    if a == c:
        print('success')
        
"""
runfile('C:/Users/simen/INF3331-Simehaa/assignment3/polynomials.py', wdir='C:/Users/simen/INF3331-Simehaa/assignment3')
[-3, 2, -1, 5]
[5, 2, -5, -5]
[-1, -2, 3]
- 4 + 2x**2 + 5x**3
4
[-4, 0, 2, 5]
success
"""
