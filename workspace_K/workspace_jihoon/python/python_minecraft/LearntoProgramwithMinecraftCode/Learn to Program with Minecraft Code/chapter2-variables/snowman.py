import mcpi.minecraft as minecraft
import mcpi.block as block
mc1= minecraft.Minecraft.create()
mc1.player.setPos(94,4,-5)
# mc.player.setPos(0,100,0)
p1=mc1.player.getTilePos()
mc1.setBlock(p1.x,p1.y,p1.z,block.SNOW)

mc2= minecraft.Minecraft.create()
mc2.player.setPos(100,4,-5)
p2=mc2.player.getTilePos()
mc2.setBlock(p2.x,p2.y,p2.z,block.SNOW)
