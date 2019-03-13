from mcpi.minecraft import Minecraft
mc=Minecraft.create()

ainput =input("test:")

if ainput=='y':
    mc.postToChat("Yyes")
else:
    mc.postToChat("Nno")
