from mcpi.minecraft import Minecraft
logan=Minecraft.create()
import time

name="Juns"
logan.postToChat("Your name is {}".format(name))
logan.postToChat("Your name is %s" %name)

name='juns'
print(name.upper())

a=name.upper()
print(a)

b=a.lower()
print(b)

spamstr="spam"
print(spamstr *3)
print(spamstr +spamstr +spamstr )

#===============================================================================
# #number1=int(input("input your number :"))
# #number2=int(input("input your number2 :"))
# sum=number1+number2
# print("{}+{}={}".format(number1,number2,sum))
# #logan.postToChat("{} + {} = {}".format(number1,number2,sum))
#===============================================================================

number3=float(input("input your number3 :"))
root=int(number3**0.5)
print(root)

cute=input("what's your name? :")
logan.postToChat("hello {}".format(cute))
