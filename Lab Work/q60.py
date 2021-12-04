def start_process(p):
    if (p=="Yes" or p=="yes" or p=="YES"):
        return ("Start process")
    elif (p=="NO" or p=="no" or p=="No"):
        return ("Start process aborted")
    else:
        return ("Sorry for the input")

p= (input("Enter the input : "))
result = start_process(p)
print(result)