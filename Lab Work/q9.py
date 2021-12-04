def sum_thrice(x, y, z):

    s = x + y + z  
    if x != y != z:
      s = s * 4
    return s

print("Value = ",sum_thrice(1, 2, 3))