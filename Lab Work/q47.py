def get_sum(n):
    
    s = 0
    for digit in str(n): 
      s += int(digit)      
    return s
   
n = 26794
print(get_sum(n))