def outer_fun(a, b, c):
    

    # inner function
    def addition(a, b,c):
        return a + b + c

    # call inner function from outer function
    add = addition(a, b, c)
    # add 5 to the result
    return add + 5

result = outer_fun(5, 10,15)
print(result)