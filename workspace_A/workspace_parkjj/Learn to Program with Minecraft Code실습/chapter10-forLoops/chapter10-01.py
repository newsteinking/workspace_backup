numbers=input("Input your number:")
my_list=[]
for i in numbers:
    my_list.append(i)
print(my_list)
my_list.reverse()
print(my_list)
print("".join(my_list))

#"".join(list) ==> list -> str