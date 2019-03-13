from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time
import shelve

x,y,z=mc.player.getPos()
def buildStructure(x, y, z, structure):
    xStart = x
    zStart = z
    for row in structure:
        for column in row:
            for block in column:
                mc.setBlock(x, y, z, block.id, block.data)
                z+=1
            x+=1
            z=zStart
        y+=1
        x=xStart
        
x+=10
with shelve.open("snowman_test2") as f:
    buildStructure(x,y,z,f["snow"])
         