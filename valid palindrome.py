s = "acb"
t = "ahbgdc"
e=[]
for x in s:
    if x in t:
        e.append(t.index(x))
print(e==sorted(e) and len(e)==len(s))

