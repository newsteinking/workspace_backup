from mcpi.minecraft import Minecraft
from mcpi import block
import time
mc=Minecraft.create()

x,y,z=mc.player.getPos()
front=3
def cost(ainput):
    output=ainput*0.2
    return output

def make_melon():
    return block.MELON.id

def make_sand():
    return block.SAND.id

def make_ice():
    return block.ICE.id

def make_cobweb():
    return block.COBWEB.id

#if __name__=="__main__":
mc.postToChat(cost(100))
mc.setBlock(x+front,y,z,make_melon())