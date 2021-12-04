while True:
    try:

        income = int(input("Please enter your taxable income in india: "))
    except ValueError:
        print("Sorry, We didn't understand that please enter taxable income as a number")

        continue
    else:
        break
tax = 0
if income <= 100000:
    tax = 0
    income = income - 100000 
elif (income <= 100000 and income>100000):
    while(income > 100000):
        tax = tax + (0 + (income)*10)/100
        income = income - 100000
else: 
    tax = tax +   (0 + (income)*20)/100


print("You owe", tax, "Rupees in income tax!!")