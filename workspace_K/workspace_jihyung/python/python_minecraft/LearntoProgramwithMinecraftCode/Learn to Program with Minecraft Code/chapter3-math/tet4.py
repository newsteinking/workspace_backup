from mcpi.minecraft import Minecraft
mc=Minecraft.create()

pos=mc.player.getPos()
x=pos.x
y=pos.y
z=pos.z
height=3
h2=height*2
h3=height*height*height*height
blocktype=67

mc.setBlocks(x+2,y,z+2,x+2,y+h3-1,z+2,blocktype)
