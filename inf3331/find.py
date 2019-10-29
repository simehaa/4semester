import sys
from os import listdir

# commandline arguments: filetype folder_path
filetype = sys.argv[1]
folder_path = sys.argv[2]
directory = listdir(folder_path)
for i in directory:
    if i.endswith(filetype):
        print(folder_path + '/' + i)

"""
runfile('C:/Users/simen/INF3331-Simehaa/assignment3/find.py', args='.sh C:/Users/simen/INF3331-Simehaa/assignment2', wdir='C:/Users/simen/INF3331-Simehaa/assignment3')
C:/Users/simen/INF3331-Simehaa/assignment2calc.sh
C:/Users/simen/INF3331-Simehaa/assignment2clock.sh
"""
