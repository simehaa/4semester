import numpy as np

def gauss(x, mu, sigma):
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-x*mu)**2/(s*sigma**2)

class Gauss:
    """docstring for Ga."""
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def __call__(self, x):
        mu = self.mu          # motsatt vei her i callfunskjonen (= self.***)
        sigma = self.sigma
        return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-x*mu)**2/(2*sigma**2)


g = Gauss(mu=0, sigma=1)

print g(3) # kaller paa g, som er et object, som en funksjon, det vil kun gaa naar jeg har __call__

#####################################################################

class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return np.sqrt(self.x**2 + self.y**2)

    def __add__(self, other):                               # blir kalt hvis jeg proever aa legge sammen objekt
        return Vec2d(self.x + other.x, self.y + other.y)

    def __mul__(self, scale):
        return Vec2d(self.x*scale, self.y*scale)


a = Vec2d(0, 3)
b = Vec2d(4, 0)

c = a + b
c *= 5

print c.length()
