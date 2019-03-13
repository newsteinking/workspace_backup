from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time
x,y,z=mc.player.getPos()
front=10

#mc.setBlocks(x+front,y,z,x+front+6,y+6,z+6,block.WOOL.id,0)
#mc.setBlocks(x+front+1,y+1,z+1,x+front+1+4,y+1+4,z+1+4,0)
#mc.setBlocks(x+front,y+1,z+3,x+front,y+2,z+3,0)

class Building(object):
    def __init__(self, x, y, z, width, height, depth):
        self.x = x
        self.y = y
        self.z = z

        self.width = width
        self.height = height
        self.depth = depth

    def build(self):
        mc.setBlocks(self.x, self.y, self.z,
                     self.x + self.width, self.y + self.height, self.z + self.depth, 35)

        mc.setBlocks(self.x + 1, self.y + 1, self.z + 1,
                     self.x + self.width - 1, self.y + self.height - 1, self.z + self.depth - 1, 0)

        self.buildWindows()
        self.buildDoor()

    def clear(self):
        mc.setBlocks(self.x, self.y, self.z,
                     self.x + self.width, self.y + self.height, self.z + self.depth, 0)

    def buildWindows(self):
        mc.setBlock(self.x + (self.width / 4 * 3), self.y + 2, self.z, block.GLASS.id)
        mc.setBlock(self.x + (self.width / 4), self.y + 2, self.z, block.GLASS.id)

    def buildDoor(self):
        mc.setBlocks(self.x + (self.width / 2), self.y + 1, self.z, self.x + (self.width / 2), self.y + 2, self.z, block.DOOR_WOOD)
        

gost=Building(x,y,z,9,6,8)
gost.build()
time.sleep(15)
gost.clear()