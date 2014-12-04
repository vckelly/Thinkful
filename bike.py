class Manufacturer(object):
  def __init__(self, manufname):
    self.manufname = manufname
  
  def modelcost(self, framecost, wheelcost):
    self.framecost = framecost
    self.wheelcost = wheelcost

    
class BikeModels(Manufacturer):
  def __init__(self, modelname):
    self.modelname = modelname
    
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
    
class Customers(object):
  def __init__(self, name, budget, market):
    self.name = name
    self.budget = budget
    self.market = market
    
