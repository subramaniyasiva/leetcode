nums = [1, 2, 0, 1]
nums=set(nums)
print(nums)
nums = sorted(nums)
print(nums)
r = []
a = [nums[0]]

for x in nums[1:]:
    if x == a[-1] + 1:
        a.append(x)
    else:
        r.append(a)
        a = [x]

r.append(a)  # Append the last sequence

print(r)
b = max(r, key=len)
print(len(b))
