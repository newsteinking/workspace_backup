from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

x=25.222
y=4
z=22.222

time.sleep(1)
mc.player.setPos(x,y+10,z)