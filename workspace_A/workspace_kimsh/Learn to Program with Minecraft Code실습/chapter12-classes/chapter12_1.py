from mcpi.minecraft import Minecraft
from mcpi import block
import time
mc=Minecraft.create()

x,y,z=mc.player.getPos()
front=8
#blocktype=block.SNOW_BLOCK.id


class makesnowman(object):
    blocktype=block.SNOW_BLOCK.id
    
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def buildsnow(self):
        self.makebody()
        self.makebutton()
        self.makeface()
        self.makehat()
        
    def makebody(self):
        mc.setBlocks(x+front,y,z,x+front+6,y+6,z+6,self.blocktype)
        time.sleep(1)
        mc.setBlocks(x+front+1,y+7,z+1,x+front+5,y+11,z+5,self.blocktype)
        mc.postToChat("Make body")
        time.sleep(1)
        
    def makebutton(self):
        mc.setBlock(x+front,y+5,z+3,block.DIAMOND_BLOCK.id)
        time.sleep(1)
        mc.setBlock(x+front,y+3,z+3,block.DIAMOND_BLOCK.id)
        time.sleep(1)
        mc.setBlock(x+front,y+1,z+3,block.DIAMOND_BLOCK.id)
        mc.postToChat("Make buttones")
        time.sleep(1)
    
    def makeface(self):
        mc.setBlock(x+front+1,y+7,z+3,35,15)
        mc.setBlock(x+front+1,y+8,z+2,35,15)
        mc.setBlock(x+front+1,y+8,z+4,35,15)
        time.sleep(1)
        mc.setBlock(x+front+1,y+10,z+2,35,15)
        mc.setBlock(x+front+1,y+10,z+4,35,15)
        time.sleep(1)
        mc.setBlocks(x+front+1,y+9,z+3,x+front,y+9,z+3,35,1)
        mc.postToChat("Make face")
        time.sleep(1)
        
    def makehat(self):
        mc.setBlocks(x+front,y+12,z,x+front+6,y+12,z+6,block.IRON_BLOCK.id)
        time.sleep(1)
        mc.setBlocks(x+front+1,y+13,z+1,x+front+5,y+15,z+5,block.IRON_BLOCK.id)
        mc.postToChat("Make hat")
#===============================================================================
# def snowman():
#     time.sleep(3)
#     mc.setBlocks(x+front,y,z,x+front+6,y+6,z+6,blocktype)
#     time.sleep(1)
#     mc.setBlocks(x+front+1,y+7,z+1,x+front+5,y+11,z+5,blocktype)
#     time.sleep(1)
#     mc.setBlock(x+front,y+5,z+3,block.DIAMOND_BLOCK.id)
#     time.sleep(1)
#     mc.setBlock(x+front,y+3,z+3,block.DIAMOND_BLOCK.id)
#     time.sleep(1)
#     mc.setBlock(x+front,y+1,z+3,block.DIAMOND_BLOCK.id)
#     time.sleep(1)
#     mc.setBlock(x+front+1,y+7,z+3,35,15)
#     mc.setBlock(x+front+1,y+8,z+2,35,15)
#     mc.setBlock(x+front+1,y+8,z+4,35,15)
#     time.sleep(1)
#     mc.setBlock(x+front+1,y+10,z+2,35,15)
#     mc.setBlock(x+front+1,y+10,z+4,35,15)
#     time.sleep(1)
#     mc.setBlocks(x+front+1,y+9,z+3,x+front,y+9,z+3,35,1)
#     time.sleep(1)
#     mc.setBlocks(x+front+1,y+13,z+1,x+front+5,y+15,z+5,block.IRON_BLOCK.id)
#     time.sleep(1)
#     mc.setBlocks(x+front,y+12,z,x+front+6,y+12,z+6,block.IRON_BLOCK.id)
#===============================================================================

bibi=makesnowman(x,y,z+front)
#bibi.makehat()
print(bibi.blocktype)