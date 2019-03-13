class Cat(object):   # house blue print 
    owner = "Craig"  #public variables 
    def __init__(self, name, weight):
        self.name = name        #private variables 
        self.weight2 = weight
    def eat(self, food):
        self.weight2 = self.weight2 + 0.05
        print(self.name + " is eating " + food)
    def eatAndSleep(self, food):
        self.eat(food)
        print(self.name + " is now sleeping...")
    def getWeightInGrams(self):
        return self.weight2 * 1000
    def getWeigth(self):
        return self.weight2
    
    
cat=Cat("DD",4)
print(cat.owner)
cat2=Cat("TT",3)
print(cat2.owner)
print(cat2.weight2)

cat.eat("fish")
cat2.eat("fish")

cat.eatAndSleep("fresh fish")
print(cat.getWeightInGrams())
print(cat2.getWeightInGrams())