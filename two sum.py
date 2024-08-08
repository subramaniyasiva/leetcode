a=[2,7,11,15]
s=a[0]
target=9

e=a[-1]
for x in range(len(a)):
    if a[s]+a[e]==target:
        r=[a.index(s),a.index(e)]
        
    elif a[s]+a[e]>target:
        e=a[e]-1
    else:
        s=a[s]+1
    
