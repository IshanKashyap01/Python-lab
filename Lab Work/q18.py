n = 687
sum = 0
while (n != 0):
    sum = sum + int(n % 10)
    n = int(n/10)

print("sum of digits of a given number = " ,sum)