from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time


height=10
levels=reversed(range(height))
print(levels)
x,y,z=mc.player.getPos()
x+=10

# for level in levels:
#     print(level)
#     mc.setBlocks(x-level,y,z-level,x+level,y,z+level,103)
#     y+=1

z+=20
width=10*2

for  i in range(10):
    mc.setBlocks(x+i,y+i,z+i,x+width-i,y+i,z+width-i,103)



# try:
#     pass
# except expression as identifier:
#     pass
# else:
#     pass