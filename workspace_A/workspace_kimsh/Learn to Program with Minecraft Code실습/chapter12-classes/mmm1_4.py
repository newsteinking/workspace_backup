import time

numbers=input("input your number")
print(numbers)
time.sleep(1)
numlist=[]

for number in numbers:
    numlist.append(number)
    time.sleep(0.5)
print(numlist)
numlist.reverse()

#str=>list   str.spliet()  str.split(" ") 
#list=>str    "".join(list)
print("".join(numlist))