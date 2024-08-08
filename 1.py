a=[1,2,3,4,2,3,2,2]
for i in range(len(a)+1):
    if 2 in a:
        a.remove(2)
print(a)
