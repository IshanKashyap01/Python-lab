quan = int(input("Enter quantity : "))
if (quan*100) > 10000: 
    print("Cost is",((quan*100)-(0.5*quan*100)) )
else: 
    print("Cost is",(quan*100))