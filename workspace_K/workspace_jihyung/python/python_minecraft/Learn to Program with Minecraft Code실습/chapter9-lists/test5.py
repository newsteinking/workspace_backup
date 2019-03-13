from mcpi.minecraft import Minecraft
mc=Minecraft.create()

blocks=[20,67,89]
x,y,z=mc.player.getPos()



mc.setBlock(x+2,y,z,blocks[0])
mc.setBlock(x+2,y+1,z,blocks[1])
mc.setBlock(x+2,y+2,z,blocks[2])