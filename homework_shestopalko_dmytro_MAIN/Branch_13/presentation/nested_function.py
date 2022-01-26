def outer():
    x = 3
    def inner(): #it is a nested function
        y = 3
        result = x + y
        return result #outer function returns the inner function
    return inner # we are returning the reference to the outer inner f-n

outer_var = outer() # result of the execution of the outer f-n will be stored in the variable
print(outer_var())
print(outer_var.__name__) # we are printing the referenceto the inner function