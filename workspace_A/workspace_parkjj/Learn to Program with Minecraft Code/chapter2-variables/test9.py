from mcpi.minecraft import Minecraft
mc=Minecraft.create()

A="Hello "
B="Worlds"
C=A+str(3)
D=C+B
mc.postToChat(D)

print('My name is {}'.format(A))

Name="Jejun"
Age=13
Job="students"
print('My name is {} and, my age is {}. Last my job is {}.'.format(Name,Age,Job))
print("Hello, World!")

print('Hello,','world!')

print('My name is %s and, my age is %d. Last my job is %s.'%s(Name,Age,Job))