a = [1, 2, 2]
b = len(a) + 1
print(b)
c = [a[0]]

for i in range(1, len(a)):
    if a[i] > c[-1]:
        b = b + 1
    c.append(a[i])
    print("Iteration", i, "b =", b)

print("Final c:", c)
print("Final b:", b)
