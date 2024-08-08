nums=[1,3,5,6,12]
i=int(input())
l=0
u=len(nums)-1
while l<=u:
    mid=(l+u)//2
    mid_v=nums[mid]
    if mid_v==i:
        print(mid)
        break
    elif i<mid_v:
        u=mid-1
    else:
        l=mid+1
else:
    print(l)
    
