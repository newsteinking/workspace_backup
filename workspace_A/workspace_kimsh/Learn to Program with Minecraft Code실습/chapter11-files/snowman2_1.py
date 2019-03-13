from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time
import shelve

x,y,z=mc.player.getPos()
front=8
blocktype=block.SNOW_BLOCK.id

def snowman():
    time.sleep(3)
    mc.setBlocks(x+front,y,z,x+front+6,y+6,z+6,blocktype)
    time.sleep(1)
    mc.setBlocks(x+front+1,y+7,z+1,x+front+5,y+11,z+5,blocktype)
    time.sleep(1)
    mc.setBlock(x+front,y+5,z+3,block.DIAMOND_BLOCK.id)
    time.sleep(1)
    mc.setBlock(x+front,y+3,z+3,block.DIAMOND_BLOCK.id)
    time.sleep(1)
    mc.setBlock(x+front,y+1,z+3,block.DIAMOND_BLOCK.id)
    time.sleep(1)
    mc.setBlock(x+front+1,y+7,z+3,35,15)
    mc.setBlock(x+front+1,y+8,z+2,35,15)
    mc.setBlock(x+front+1,y+8,z+4,35,15)
    time.sleep(1)
    mc.setBlock(x+front+1,y+10,z+2,35,15)
    mc.setBlock(x+front+1,y+10,z+4,35,15)
    time.sleep(1)
    mc.setBlocks(x+front+1,y+9,z+3,x+front,y+9,z+3,35,1)
    time.sleep(1)
    mc.setBlocks(x+front+1,y+13,z+1,x+front+5,y+15,z+5,block.IRON_BLOCK.id)
    time.sleep(1)
    mc.setBlocks(x+front,y+12,z,x+front+6,y+12,z+6,block.IRON_BLOCK.id)
    
def sortPair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2


def copyStructure(x1, y1, z1, x2, y2, z2):
    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z1, z2 = sortPair(z1, z2)

    width = x2 - x1
    height = y2 - y1
    length = z2 - z1

    structure = []

    print("Please wait...")

    # Copy the structure
    for row in range(height):
        structure.append([])
        for column in range(width):
            structure[row].append([])
            for depth in range(length):
                block = mc.getBlockWithData(x1 + column, y1 + row, z1 + depth)
                structure[row][column].append(block)

    return structure
snowman()
x1=x+8
y1=y 
z1=z
x2=x+8+7
y2=y+15
z2=z+6

structlist=copyStructure(int(x1)-2,int(y1)-2,int(z1)-2,int(x2)+1,int(y2)+1,int(z2)+1)
with shelve.open("snowman_test2") as shelvefile:
    shelvefile["snow"]=structlist
    shelvefile.close()