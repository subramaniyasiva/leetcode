from collections import Counter

nums = [0,0,1,1,1,1,2,3,3]
a = Counter(nums)
r=0
for x, y in a.items():
    if y > 2:
        b=y-2
        r=r+b
        for i in range(b):
            nums.remove(x)
print(len(nums)-r)
print(nums)
