nums=[2,3,3]
#a=set(nums)
n=len(nums)

for x in set(a):
    d=nums.count(x)
    if d > n/2:
        print(d)
    
