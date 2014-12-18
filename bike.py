class Manufacturer(object):
  def __init__(self, manufname):
    self.manufname = manufname
  
class BikeModels(Manufacturer):
  def __init__(self, modelname, framecost, wheelcost, numwheels, manufname):
    super(BikeModels, self).__init__(manufname)
    self.modelname = modelname
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
    
class Customers(object):
  def __init__(self, name, budget, market):
    self.name = name
    self.budget = budget
    self.market = market
    
