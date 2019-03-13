# No.1============================================

a=int(input("what is your a?"))
b=int(input("What is your b?"))
temp=a
a=b
b=temp

print(f'a={a} b={b}')
# No.2============================================ 

a=a+b
b=a-b
a=a-b
print(f'No.2 a={a} b={b}')

# No.3============================================ tuple^^

a,b=b,a
print(f'No.3 a={a} b={b}')