from collections import Counter
s="bbbaaaba"
t="aaabbbba"
a=list(Counter(s).values())
b=list(Counter(t).values())
print(a)
print(b)
print(a==b)

