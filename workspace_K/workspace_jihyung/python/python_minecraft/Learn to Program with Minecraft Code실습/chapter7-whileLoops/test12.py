from mcpi.minecraft import Minecraft
mc=Minecraft.create()

username=input("enter your user name:")
while True:
    message=input("enter your message")
    if message=="exit":
        break
    mc.postToChat("your username is {} :messe is {}".format(username,message))
mc.postToChat("finish")