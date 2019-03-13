from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time

name1=input("Whats your name? :")
message=input("Whats your message? :")
logan.postToChat("hello "+message+" "+name1)