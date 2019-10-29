import random

def new_hat():
    colors = ['red','blue','yellow','purple']
    hat = []
    for color in colors:
        for i in range(10):
            hat.append(color)
    return hat

def draw_balls(hat):
    balls = []
    for i in range(10):
        ball = random.choice(hat)
        balls.append(ball)
        hat.remove(ball)
    return balls

N = 100000
M = 0

for i in range(N):
    hat = new_hat()
    balls = draw_balls(hat)
    if balls.count('blue') == 2 and balls.count('purple') == 2:
        M += 1

print 'probability = %.4f' % (float(M)/N)
