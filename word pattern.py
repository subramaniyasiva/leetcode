from collections import Counter
pattern="abba"
s="og cat cat dog"
p=Counter(pattern)
print(p)
s=s.replace(" ","")
print(s)
print(Counter(s))

