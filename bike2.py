from bike import Manufacturer, BikeModels, BikeShops, Customers

huffy = Manufacturer("Huffy")
huffyrace = BikeModels("Huffy Race")
huffyrace.modelcost(70, 250)

huffyoffroad = BikeModels("Huffy Offroad")
huffyoffroad.modelcost(60, 150)


trek = Manufacturer("Trek")

trekrace = BikeModels("Trek Race")
trekrace.modelcost(90, 500)

trekcruiser = BikeModels("Trek Cruiser")
trekcruiser.modelcost(60, 250)


bikeshop = BikeShops("Bike Shop", 1.2)
bikeshop.inventory(4)

customer1 = Customers("Johnny J", 300.00, "cruiser bike")

customer2 = Customers("Mary J", 500.00, "offroad bike")

customer3 = Customers("Mikey J", 1000.00, "race bike")

print "Bike Shop's inventory before sales:"
print "%d of %s" % (1, "huffyrace")
print "%d of %s" % (1, "huffyoffroad")
print "%d of %s" % (1, "trekcruiser")
print "%d of %s" % (1, "trekrace")

print customer1.name + " would like to buy a " + trekcruiser.modelname + " within his budget of " + str(customer1.budget)

print customer2.name + ' would like to buy a ' + huffyoffroad.modelname + " within her budget of " + str(customer2.budget)

print customer3.name + ' would like to buy a ' + trekrace.modelname + ' within his budget of ' + str(customer3.budget)

print "Bike Shop's inventory after sales:"
print "%d of %s" % (0, 'huffyrace')
print "%d of %s" % (1, 'huffyoffroad')
print "%d of %s" % (0, 'trekcruiser')
print "%d of %s" % (0, 'trekrace')

print "Total sales is %d." % ((trekcruiser.modelcost * bikeshop.profitmarg) + (huffyoffroad.modelcost * bikeshop.profitmarg) + (trekrace.modelcost * bikeshop.profitmarg))