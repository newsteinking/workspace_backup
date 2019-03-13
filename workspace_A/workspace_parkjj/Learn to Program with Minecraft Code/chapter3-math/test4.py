from mcpi.minecraft import Minecraft
Logan=Minecraft.create()
import time

x=2
y=1
z=1
blocktype=103
blocktypeAir=0

Logan.player.setTilePos(x,y,z)
Logan.setBlock(x,y,z,blocktypeAir)
Logan.setBlock(x,y+1,z,blocktypeAir)
Logan.setBlock(x**2,y,z,blocktype)
#time.sleep(5)

y=y+1
#y+=1
Logan.setBlock(x,y,z,blocktype)
z=z+1

pos=Logan.player.getPos()
x=int(pos.x)
y=int(pos.y)
z=int(pos.z)

Logan.postToChat("x:{},y:{},z:{}".format(x,y,z))
Logan.postToChat("Boom!!")

x=x+20
z=z+20
Logan.player.setTilePos(x,y+100,z)
#x=x+1
#z=z+1
#Logan.setBlock(x+1,y,z+1,0)
Logan.setBlock(x,y-1,z,30)
time.sleep(4)
Logan.setBlock(x,y-1,z,11)
time.sleep(2)
Logan.setBlock(x,y-1,z,9)
Logan.postToChat("cool!")
