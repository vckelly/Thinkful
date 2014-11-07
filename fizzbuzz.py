fizz = range(1, 100)
buzz = []

for i in fizz: 

	if (i % 5) == 0 and (i % 3) == 0:
		buzz.append("fizzbuzz")

	elif (i % 5) == 0: 
		buzz.append("buzz")

	elif (i % 3) == 0:
		buzz.append("fizz")

	else: 
		buzz.append(i)
		
print "Fizz buzz counting up to 100" 

print buzz

