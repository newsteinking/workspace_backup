from mcpi.minecraft import Minecraft
from mcpi import block
mc=Minecraft.create()
import time

score={}
time.sleep(10)
hitt=mc.events.pollBlockHits()
hits=len(hitt)
name=input("What's your name?")
score[name]=hits
mc.postToChat("{}'s score is {}.".format(name,score[name]))

