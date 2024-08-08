a=[1,1,1,2,3,4,5,3]
cur=1
while cur:
    l=cur-1
    r=cur+1
    if a[cur] > a[l] and a[cur]>a[r]:
        print(cur)
        break
    cur=cur+1
