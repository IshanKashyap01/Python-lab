def middle(a, b ,c) :
    m = min(a,b,c)
    M = max(a,b,c)
    R = a+b+c-m-M
    return R

print(middle(8,7,6))