intervals=[[1,3],[2,6],[8,10],[15,18]]
r=[]
a=[intervals[0]]
for x in intervals[1:]:
    if x[0]<=a[-1]:
        print(yes)
