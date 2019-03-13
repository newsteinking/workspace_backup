from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time
from mcpi import block
pos=logan.player.getPos()
x=pos.x
y=pos.y
z=pos.z
up=3

blocktype=block.SUGAR_CANE.id
logan.setBlock(x+up,y,z,blocktype)
blocknumber=logan.getBlock(x+up,y,z)
check=blocknumber == blocktype
if check==True:
    logan.postToChat("block number is [ {} ]".format(blocknumber))
