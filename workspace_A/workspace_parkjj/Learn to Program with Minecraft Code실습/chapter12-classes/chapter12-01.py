from mcpi.minecraft import Minecraft
import time
from mcpi import block
mc=Minecraft.create()


class imcuty(object):
    
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
       
        
    def makelogan(self,blocktype):
        self.btype=blocktype
        self.makebody(self.btype)
        self.makeface(self.btype)
        self.makehat(self.btype)
    
    def makebody(self,blockt):
        blocktype=blockt
        time.sleep(0)
        mc.setBlocks(self.x+front,self.y,self.z,self.x+front+6,self.y+6,self.z+6,blocktype)
        time.sleep(1)
        if blockt==0:
            blocktype=0
        else :
            blocktype=block.DIAMOND_BLOCK.id
        mc.setBlock(self.x+front,self.y+5,self.z+3,blocktype)
        time.sleep(1)
        mc.setBlock(self.x+front,self.y+3,self.z+3,blocktype)
        time.sleep(1)
        mc.setBlock(self.x+front,self.y+1,self.z+3,blocktype)
        time.sleep(1)
    
    
    def makeface(self,blockt):
        blocktype=blockt
        mc.setBlocks(self.x+front+1,self.y+7,self.z+1,self.x+front+5,self.y+11,self.z+5,blocktype)
        time.sleep(1)
        if blockt==0:
            blocktype=0
        else :
            blocktype=35,15
        mc.setBlock(self.x+front+1,self.y+7,self.z+3,blocktype)
        mc.setBlock(self.x+front+1,self.y+8,self.z+2,blocktype)
        mc.setBlock(self.x+front+1,self.y+8,self.z+4,blocktype)
        time.sleep(1)
        mc.setBlock(self.x+front+1,self.y+10,self.z+2,blocktype)
        mc.setBlock(self.x+front+1,self.y+10,self.z+4,blocktype)
        time.sleep(1)
        if blockt==0:
            blocktype=0
        else :
            blocktype=35,14
        mc.setBlocks(self.x+front+1,self.y+9,self.z+3,self.x+front,self.y+9,self.z+3,blocktype)
        time.sleep(1)
    
    def clear(self,blocktype):
        self.btype=blocktype
        self.makebody(self.btype)
        self.makeface(self.btype)
        self.makehat(self.btype)
        
    
    def makehat(self,blockt):
        if blockt==0:
            blocktype=0
        else :
            blocktype=block.IRON_BLOCK.id
        mc.setBlocks(self.x+front,self.y+12,self.z,self.x+front+6,self.y+12,self.z+6,blocktype)
        time.sleep(1)
        mc.setBlocks(self.x+front+1,self.y+13,self.z+1,self.x+front+5,self.y+15,self.z+5,blocktype)
        time.sleep(1)    
    
    def getx(self):
        return self.x
    

x,y,z=mc.player.getPos()
front=0
print(x)
aa=imcuty(x,y,z)
aa.makelogan(9)
time.sleep(5)
aa.clear(0)

getget=aa.getx()
print(getget)
