a=input()
b=(a.strip())
print(b)
b=b[::-1]
c=[]
for x in b:
    if x==' ':
        break
    else:
        c.append(x)
print(len(c))
