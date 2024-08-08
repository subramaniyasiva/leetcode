
n = 19

i
while r <100:
    r=0
    #print(n)
    m = str(n)
    for x in m:
        r += int(x) * int(x)
    print(r)
    if r==100:
        print("true")
    else:
        print("false")
    
    
