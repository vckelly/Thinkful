class Manufacturer(object):
  def __init__(self, manufname):
    self.manufname = manufname
  
  def modelcost(self, framecost, wheelcost):
    self.framecost = framecost
    self.wheelcost = wheelcost

    
class BikeModels(Manufacturer):
  def __init__(self, modelname):
    self.modelname = modelname
    
    numwheels = 2.00
    
    wheelcost = wheelcost * numwheels
      
    
class BikeShops(Manufacturer):
  def __init__(self, shopname):
    self.shopname = shopname
    
  def inventory(self, numinstock):
    self.numinstock = numinstock
    
  def shoptotalprice(self, shopprofit):
    self.shopprofit = shopprofit
    
    shopprofit = modelcost * shopprofit
    
class Customers(BicycleInd):
  def __init__(self, name, budget, market):
    self.name = name
    self.budget = budget
    self.market = market
    
