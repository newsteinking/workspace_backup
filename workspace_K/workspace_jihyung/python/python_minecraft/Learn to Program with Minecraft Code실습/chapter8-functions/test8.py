from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getPos()


def  makecost(cost):
    price =cost+2
    pice=price*10
    return price
    
cost=1300
print(makecost(1300))
    
    
    