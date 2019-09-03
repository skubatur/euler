# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def get_x(R, ra, rb):
    hyp = ra + rb
    y = 2*R - hyp
    x = math.sqrt(hyp*hyp - y*y)
    
    return x

def helper(R, rads):
    sum_ = 0
    
    for i in range(len(rads)-2):
        sum_ = math.fsum([get_x(R, rads[i], rads[i+2]), sum_])
      
    if len(rads) >= 2:
        sum_ = math.fsum([get_x(R, rads[0], rads[1]), sum_])
    
    if len(rads) == 1:
        return math.fsum([sum_, 2*rads[-1]])
    else:
        return math.fsum([rads[-2], sum_ , rads[-1]])


[R, n] = list(map(int, input().strip().split(' ')))

r = list(map(int, input().strip().split(' ')))
    
r = sorted(r)
# O = []

# while r:
#     L = len(O)
#     if len(r) > 1:
#         O = O[:L//2] + [r.pop(), r.pop()] + O[L//2:]
#     else:
#         O = O[:L//2] + [r.pop()] + O[L//2:]
        
print(round(1000*helper(R, r)))
        
        
