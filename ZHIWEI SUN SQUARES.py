 """	Goal
Given a positive integer n, find the number of ordered tuples (a, b, c, d, e) over non-negative integers for which a² + b² + c² + d² = n and b + 3c + 5d = e².

Note: A conjecture by 孙智伟 (Sūn, Zhìwěi) states that this count is always at least 1.

For example, if n is 9, there are 3 solutions, namely:

(0, 0, 3, 0, 3)
(1, 0, 2, 2, 4)
(3, 0, 0, 0, 0)
"""
import math

n=int(input())
l=[]
for b in range(0,math.floor(n**0.5)+1):
    for c in range(0,math.floor(n**0.5)+1):
        for d in range(0,math.floor(n**0.5)+1):
            if (b+3*c+5*d)**0.5==math.floor((b+3*c+5*d)**0.5):
                l+=[[b,c,d]]
    s=0
    for j in l:
        for a in range(0,math.floor(n**0.5)+1):
            if a**2+j[0]**2+j[1]**2+j[2]**2==n:
                s+=1
        
print("the number of ordered tuples (a, b, c, d, e) is : ",s)

    
    
    
    
    
    
    
    
