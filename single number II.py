from collections import Counter
nums=[2,2,2,3]
c=Counter(nums)
for x,y in c.items():
    if y==1:
        return x
