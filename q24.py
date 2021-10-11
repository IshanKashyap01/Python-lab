i = 1
num = int(input("Enter the number: "))
while i < num / 2:
    if(num % i == 0):
        print("Number is not a prime number")
        exit(0)
print("Number is prime")
