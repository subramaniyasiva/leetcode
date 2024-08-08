s=input()
r=""
b=[]
s=s[::-1].split()
for x in s:
    a=x[::-1]
    b.append(a)
for y in b:
    r=r+y+" "
print(r.strip())


    
    
