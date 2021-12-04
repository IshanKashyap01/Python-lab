def check_user_input(input):
    try:
        
        val = int(input)
        print("Input is an integer number. Number = ", val)
    except ValueError:
        try:
            
            val = float(input)
            print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No value")


input1 = input("Enter your Age ")
check_user_input(input1)

input2 = input("Enter any number ")
check_user_input(input2)

input2 = input("Enter the last number ")
check_user_input(input2)