import random, numpy as np, matplotlib.pyplot as plt

def play_game():
    sum_dice = 0
    die1 = random.randint(1,6)
    sum_dice = die1

    for i in range(die1):
        die2 = random.randint(1,6)
        sum_dice += die2

    if sum_dice > 20:
        return True
    else:
        return False

def simulate(M):
    N = 0
    for i in range(M):
        success = play_game()
        if success:
            N += 1

    return float(N)/M


x = np.random.randint(1,3,100)
print x == 2
print x == 1
