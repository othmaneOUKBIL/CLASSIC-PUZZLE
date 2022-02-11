import math
d=[9,24,144,365,888,2020,12345,23456,24576]

for k in d:
    n=k
    l=[]
    for b in range(0,math.floor(n**0.5)+1):
        for c in range(0,math.floor(n**0.5)+1):
            for d in range(0,math.floor(n**0.5)+1):
                if (b+3*c+5*d)**0.5==math.floor((b+3*c+5*d)**0.5):
                    l+=[[b,c,d]]
    s=0
    i=1
    for j in l:
        for a in range(0,math.floor(n**0.5)+1):
            if a**2+j[0]**2+j[1]**2+j[2]**2==n:
                s+=1
        i+=1
    print("test",k," OK ",s)

    
    
    
    
    
    
    
    