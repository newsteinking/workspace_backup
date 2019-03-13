from mcpi.minecraft import Minecraft
mc=Minecraft.create()

def makecost(cost):
    price=cost+2
    price=price*10
    return price

a=makecost(1000)
print(a)