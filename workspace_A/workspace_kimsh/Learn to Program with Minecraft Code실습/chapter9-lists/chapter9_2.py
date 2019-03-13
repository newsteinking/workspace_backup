# array       a=array([])
# list        a=[2,3,4]
# tuple       a=(2,3,4)
# dictionary  a={1:'a',2:'b'}  

a=[1,2,3,4]

print(a)
print(a[0])
print(a[2])
print(len(a))

a[2]=100
print(a)

b=['Babo',2,1,9]
print(b)
b[0]='BIBI'
print(b)
print(b*3)
print(b.index(9))
print(2 in b)
print('Babo' in b)
#===============================================================================
# cha a={a,b,c}
# printf(%s,a[0])
#===============================================================================

food=[]
food.append('food')
print(food)
food.append('fighter')
print(food)
food.insert(1,1)
print(food)
potato="test"
print(potato)
tube=(1,2,3,4)
print(tube)
tube=1,2,3,4
print(tube)
print(type(tube))

a,b=3,4
print(a)
print(b)
print(type(a))