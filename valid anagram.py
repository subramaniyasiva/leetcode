from collections import Counter
a="anagram"
t="naagarm"
if sorted(a)==sorted(t):
    print("true")
else:
    print("false")
print(Counter(a))
print(Counter(t))
