nums=[0,1,2,4,5,7]
a=[nums[0]]
r=[]
for x in nums[0:]:
    if x-a[-1]==1:
        
        a.append(x)
    else:
        b=a[0],"->",a[-1]
        r.append(b)
        #a=[]
        #y=x+1
        
        
print(a)
print(r)
    
