def b():
    print("Inside the method B.")
     
def a():
    print("Inside the method A.")
     
    return b

returned_function = a()
returned_function()