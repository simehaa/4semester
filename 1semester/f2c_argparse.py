import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--F','--Fahrenheit',type=float,\
                    default=100,help='Give Fahrenheit degrees')

args = parser.parse_args()
F = args.F
C = (F - 32)*5./9

print "%g degrees F is %1.f degrees C" % (F,C)
