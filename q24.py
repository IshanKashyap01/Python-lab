Number = int(input("Please Enter any Number: "))
count = 0
i = 2

while(i <= Number//2):
    if(Number % i == 0):
        count = count + 1
        print("%d is not a Prime Number" %Number)
        exit(0)
    i = i + 1

print("%d is a Prime Number" %Number)
