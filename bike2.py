from bike import BicycleInd, Manufacturer, BikeModels, Frames, Wheels, BikeShops, Customers

huffy = Manufacturer("Huffy")

huffyraceW = Wheels("Light", 70, 1)
huffyraceF = Frames("Light", 250, 2)
huffyrace = BikeModels("Huffy Race")
huffyrace.modelweight(1, 3)
huffyrace.modelcost(70, 250)
huffyrace.manutotalprice(.20)

huffyoffroadW = Wheels("Heavy", 60, 3)
huffyoffroadF = Frames("Heavy", 150, 6)
huffyoffroad = BikeModels("Huffy Offroad")
huffyoffroad.modelweight(3, 6)
huffyoffroad.modelcost(60, 150)
huffyoffroad.manutotalprice(.20)

trek = Manufacturer("Trek")

trekraceW = Wheels("Light", 90, .5)
trekraceF = Frames("Light", 500, 2)
trekrace = BikeModels("Trek Race")
trekrace.modelweight(.5, 2)
trekrace.modelcost(90, 500)
trekrace.manutotalprice(.20)

trekcruiserW = Wheels("Medium", 60, 1.5)
trekcruiserF = Frames("Medium", 250, 5)
trekcruiser = BikeModels("Trek Cruiser")
trekcrusier.modelweight(1.5, 5)
trekcruiser.modelcost(60, 250)
trekcruiser.manutotalprice(.20)

bikeshop = BikeShops("Bike Shop")
bikeshop.inventory(4)
bikeshophuffyrace = huffyrace.shoptotalprice(.20)
bikeshophuffyoffroad = huffyoffroad.shoptotalprice(.20)
bikeshoptrekrace = trekrace.shoptotalprice(.20)
bikeshoptrekcrusier = trekcruiser.shoptotalprice(.20)

print huffyrace + huffyrace.modelweight
print huffyoffroad + huffyoffroad.modelweight
print trekrace + trekrace.modelweight
print trekcruiser + trekcruiser.modelweight

customer1 = Customers("Johnny J", 200.00, "cruiser bike")
print customer1.name + (customer1.budget >= shoptotalprice)

customer2 = Customers("Mary J", 500, "offroad bike")
print customer2.name + (customer2.budget >= shoptotalprice) 

customer3 = Customers("Mikey J", 1000, "race bike")
print customer3.name + (customer3.budget >= shoptotalprice)

print "Bike Shop's inventory before sales:"
print "%d of %s" % (1, huffyrace)
print "%d of %s" % (1, huffyoffroad)
print "%d of %s" % (1, trekcruiser)
print "%d of %s" % (1, trekrace)

print customer1.name + trekcruiser.shoptotalprice + (trekcruiser.shopttotalprice - customer1.budget)

print customer2.name + huffyoffroad.shoptotalprice + (huffyoffroad.shoptotalprice - customer2.budget)

print customer3.name + trekrace.shoptotalprice + (trekrace.shoptotalprice - customer3.budget)

print "Bike Shop's inventory after sales:"
print "%d of %s" % (1, huffyrace)
print "%d of %s" % (0, huffyoffroad)
print "%d of %s" % (0, trekcrusier)
print "%d of %s" % (0, trekrace)

print "Total profit on sales is %d." % ((bikeshophuffyoffroad - huffyoffroadprice) + (bikeshoptrekcrusier - trekcrusierprice) + (bikeshoptrekrace - trekraceprice))