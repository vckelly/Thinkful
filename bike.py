class Manufacturer(object):
  def __init__(self, manufname):
    self.manufname = manufname
<<<<<<< HEAD
  
=======

  def modelcost(self, framecost, wheelcost):
    self.framecost = framecost
    self.wheelcost = wheelcost


>>>>>>> 25dbd3e4e6f9bc8200ec930aa9441c29b4d41f61
class BikeModels(Manufacturer):
  def __init__(self, modelname, framecost, wheelcost, numwheels, manufname):
    super(BikeModels, self).__init__(manufname)
    self.modelname = modelname
<<<<<<< HEAD
    self.framecost = framecost
    self.wheelcost = wheelcost
    self.numwheels = numwheels
    
  def modelcost(self):
    return self.framecost + (self.wheelcost * self.numwheels)
  
 
class BikeShops(object):
  def __init__(self, shopname, profitmarg, bikes):
    self.shopname = shopname
    self.profitmarg = profitmarg
    self.bikes = bikes
    
  def inventory(self):
    return len(bikes)
  
  def manufacturer(self):
    return [x.manufname for x in self.bikes]
    
=======

  def modelcost(self, framecost, wheelcost):
    self.framecost = framecost
    self.wheelcost = wheelcost

    numwheels = 2.00

    wheelcost = wheelcost * numwheels


class BikeShops(Manufacturer):
  def __init__(self, shopname, profitmarg):
    self.shopname = shopname
    self.profitmarg = profitmarg

  def modelcost(self, framecost, wheelcost):
    self.framecost = framecost
    self.wheelcost = wheelcost

  def inventory(self, numinstock):
    self.numinstock = numinstock

  shopprofit = modelcost * profitmarg

>>>>>>> 25dbd3e4e6f9bc8200ec930aa9441c29b4d41f61
class Customers(object):
  def __init__(self, name, budget, market):
    self.name = name
    self.budget = budget
    self.market = market

