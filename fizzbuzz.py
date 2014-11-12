fizz = range(1, 101)
buzz = []

for i in fizz: 

  if not (i % 3) == 0:
		buzz += "fizz"
    
	if not (i % 5) == 0:
		buzz += "buzz"
  
 # else: 
		#buzz.append(i)
		
print "Fizz buzz counting up to 100" 

print buzz or str(i)

