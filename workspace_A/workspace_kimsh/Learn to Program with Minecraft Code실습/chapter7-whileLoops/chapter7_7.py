from mcpi.minecraft import Minecraft
mc=Minecraft.create()

name=input("What's your name? : ")
while True:
    msg=input("input your massage(exit) : ")
    if msg=="exit":
        break
    mc.postToChat("your name is {},your massage is {}".format(name,msg))
mc.postToChat("exit...")