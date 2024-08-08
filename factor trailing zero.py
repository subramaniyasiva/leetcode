def factp(n):
   
        
    
    if n==1:
        return n
        
    else:
        r=(n*factp(n-1))
        return r
    
    
n=int(input())
if n==0:
    print('0')
else:
    print(str(factp(n)).count('0'))

