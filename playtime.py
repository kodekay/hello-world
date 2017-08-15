bread = 50
peanutButter = 40
jelly = 40
sandwich = 4

if bread == 2:
	print "I have enough slices of bread."
elif bread > 2:
	print "I have {0} slices of bread. That's {1} more than enough!".format(bread, bread/2)
elif bread == 1:
	print "I could probably make an open-faced sandwich."
else:
	print "Looks like I won't be having a sandwich for lunch."

if peanutButter == 1:
	print "I have enough tablespoons of peanut butter."
elif peanutButter > 1:
	print "I have {0} tablespoons of peanut butter. That's {1} more than enough!".format(peanutButter, peanutButter/2)
else: 
	print "Looks like I won't be having peanut butter on my sandwich."

if jelly == 1:
	print "I have enough tablespoons of jelly."
elif jelly > 1:
	print "I have {0} tablespoons of jelly. More than enough!".format(jelly)
else: 
	print "Looks like I won't be having jelly on my sandwich."

if bread == 2 and peanutButter == 1 and jelly == 1:
	print "I can have a peanut butter and jelly sandwich for lunch! I can make {0} sandwich.".format(sandwich/sandwich)
elif bread > 2 and peanutButter > 1 and jelly > 1:
	print "I have {0} sets of bread. {1} tablespoons of peanut butter and {2} tablespoons of jelly. Therefore, I can make {3} total sandwiches.".format(bread/2, peanutButter, jelly, (bread/2+peanutButter/2+jelly/2))
elif bread < 1 and peanutButter < 1 and jelly < 1:
	print "Looks like I won't be having lunch!"
else:
	print "I'll need to get creative with lunch."

print min(bread, peanutButter, jelly)
