from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

x=int(input("input your x : "))
y=int(input("input your y : "))
z=int(input("input your z : "))

if -25<=x<=-35:
    mc.postToChat("gunchu")

else:
    mc.postToChat("muly")

if -25<=y<=-35:
    mc.postToChat("gunchu")

else:
    mc.postToChat("muly")

if -25<=z<=-35:
    mc.postToChat("gunchu")

else:
    mc.postToChat("muly")
