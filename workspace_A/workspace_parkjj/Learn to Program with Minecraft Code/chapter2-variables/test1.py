from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

A=100
time.sleep(1)
mc.postToChat(A)

B=200
time.sleep(1)
mc.postToChat(B)

C=A+B
time.sleep(1)
mc.postToChat(C)

time.sleep(1)
mc.postToChat(A+B+100)

time.sleep(1)
mc.postToChat(200+300)

my_string1="six hundred"
my_string2="seven hundred"
my_string3=my_string1+my_string2
mc.postToChat("six hundred" + "seven hundred")
