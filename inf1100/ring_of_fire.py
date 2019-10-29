import sys, os
import numpy as np

ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = []
rules = []
drink = []
names = []
K = 0

for s in range(4):
    for r in ranks:
        deck.append(r)
np.random.shuffle(deck)

try:
    players = int(raw_input('How many players? - '))
except ValueError:
    print 'players must be a number'
    players = int(raw_input('How many players? - '))

for i in range(players):
    player = raw_input('Name of Player %i? - ' % (i + 1))
    names.append(player)

while len(names) < 52:
    names = names + names


for i in range(len(deck)):
    os.system('clear')

    if i == 51:
        raw_input('last card!')
    elif i == 0:
        a = raw_input('Press enter to start Ring of Fire!')
    else:
        raw_input('%i cards left, and %ss turn. Pick a card' % ((52 - i), names[i]))
    card = deck[-1]; del deck[-1]
    if 'A' in card:
        print 'Waterfall!'
        raw_input('raise your drinks and drink till the end!')
    elif '2' in card:
        print 'Two is for you'
        raw_input('pick someone to drink')
    elif '3' in card:
        print 'Three is for me'
        raw_input('you drink for yourself')
    elif '4' in card:
        print 'Four is for whores'
        raw_input('all girls drink')
    elif '5' in card:
        print '5 is GRIS'
        raw_input('current GRIS holder is %s' % names[i])
    elif '6' in card:
        print 'Six is for dicks'
        raw_input('all guys drink')
    elif '7' in card:
        print 'Seven is heaven'
        raw_input('raise you arms!')
    elif '8' in card:
        print 'Eight is for mate'
        raw_input('pick a mate')
    elif '9' in card:
        print 'Nine is rhyme'
        raw_input('try to rhyme')
    elif '10' in card:
        print 'Ten is category'
        raw_input('make a category')
    elif 'J' in card:
        print 'Eleven: make a rule. current rules:'
        for u in range(len(rules)):
            print rules[u]
        rule = raw_input('new rule: ')
        rules.append('%s' % rule)
    elif 'Q' in card:
        print 'Queen is question master'
        raw_input('%s is the current question master' % names[i])
    elif 'K' in card:
        K += 1
        if K > 3:
            print 'Oh no! you got the last king, \
            \nthe cup is yours to drink, and it now contains \
            \n%s, %s and %s' % (drink[0], drink[1], drink[2])
            raw_input('I wish you the best of luck!')
        else:
            print 'King is kings cup'
            drink.append(str(raw_input('what drink did you add? - ')))

    a = np.random.random_integers(1,52)
    if a == 13 or a == i:
        raw_input('Oh no! you tipped over the stack of cards. Finish your drink!')


print 'Game Over'
