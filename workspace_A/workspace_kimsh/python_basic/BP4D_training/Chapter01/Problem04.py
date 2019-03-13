# No.1========================================
def change(str2):
    strlist=[]
    for i in str2:
        strlist.append(i)
    strlist.reverse()
    a="".join(strlist)
    return a
print(change("123456789"))

# No.2========================================

def change2(sttring):
    changed_str=sttring[::-1]
    return changed_str
print(change2("tomato"))