def first_reverse(str):
    aa=list(reversed(str))
    print(aa)
    bb=''.join(aa)
    return bb

def first_reverse2(str):
    str2=str[::+5]
    return str2
print(first_reverse2("13579"))

print(first_reverse("12345"))

#54321

# str ==> list    str.split()   str.split(" ")
#list ==> str     ''.join(list)