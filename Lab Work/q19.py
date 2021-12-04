n = 4513
product = 1

while (n != 0):
    product = product * (n % 10)
    n = n // 10

print("product of digits of a given number = ",product)