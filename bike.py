class BicycleInd(object):
  def __init__(self, avgcost, avgprofit, avgcustsales):
    self.avgcost = avgcost
    self.avgprofit = avgprofit
    self.avgcustsales = avgcustsales
    
class Manufacturer(BicycleInd):
  def __init__(self, manuname):
    self.manuname = manuname

    def manutotalprice(self, manufmargin):
      self.manufmargin = manufmargin
      
      if manuprofit: 
        manuprofitamount = self.modelcost() * manufmargin
        manutotaprice = self.modelcost() + manuprofitamount
class BikeModels(Manufacturer):
  manutotalprice = []
  def __init__(self, modelname):
    self.modelname = modelname
    
  def modelweight(self, frameweight, wheelweight):
    self.frameweight = frameweight
    self.wheelweight = wheelweight
    
    numwheels = 2.00
    
    if wheelweight and frameweight:
      wheelweight = numwheels * wheelweight
      modelweight = wheelweight + frameweight
      
  def modelcost(self, wheelcost, framecost):
    self.wheelcost = wheelcost
    self.framecost = framecost
    
    numwheels = 2.00
    
    if wheelcost and framecost:
      wheelcost = numwheels * wheelcost
      modelcost = wheelcost + framecost
      
class Wheels(Manufacturer):
  def __init__(self, wheelname, wheelcost, wheelweight):
    self.wheelname = wheelname
    self.wheelcost = wheelcost
    self.wheelweight = wheelweight

class Frames(Manufacturer):
  def __init__(self, framename, framecost, frameweight):
    self.framename = framename
    self.framecost = framecost
    self.frameweight = frameweight
    
class BikeShops(Manufacturer):
  shopprofit = []
  def __init__(self, shopname):
    self.shopname = shopname
    
  def inventory(self, numinstock):
    self.numinstock = numinstock
    
  def shoptotalprice(self, shopprofit):
    self.shopprofit = shopprofit
    return super(Bikeshops, self).manutotalprice
  
  if shopprofit:
    shopprofitamount = manutotalprice * shopprofit
    shoptotalprice = manutotalprice + shopprofitamount
    
class Customers(BicycleInd):
  def __init__(self, name, budget, market):
    self.name = name
    self.budget = budget
    self.market = market
    