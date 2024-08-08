a={'I':1
'V':5
'X':10
'L':50
'C':100
'D':500
'M':1000}
=
r=0
for i in len(a)-1:
    if a[s[i]]>=a[s[i+1]]:
        sum=sum+a[s[i]]
        i=i+1
    else:
        sum=sum+a[s[i+1]]-a[s[i]]
returm sum
    
