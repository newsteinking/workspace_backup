from mcpi.minecraft import Minecraft
from test.test_itertools import take
mc=Minecraft.create()
import time

count=1
while count<5:
    mc.postToChat(count)
    count+=1