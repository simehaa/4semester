"""
What to do with a physics degree
"""

input_u = raw_input("Are you a physics student? y/n\n")
input_u = str(input_u)
input_u = input_u.lower()

if input_u == "y" or input_u == "yes" or input_u == "aye":
	a = False

	while a == False:
		career = raw_input("Do you want to know  what  a physics degree should be used for? y/n \n")
		career = str(career)
		career = career.lower()
		if career == "y" or career == "yes":
			print "You should nuke those damned chemists!"
			a = True
		else:
			print "Haha, really funny. Give me some actual input"
elif input_u == "n" or input_u == "no":
	print "Get outta here"
	exit()
else:
	print "Not funny"
	exit()
