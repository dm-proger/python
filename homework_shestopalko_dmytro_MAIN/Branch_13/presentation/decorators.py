def speak_robot():
    print("Hello humans")

def decorate_robot(func):#decorator function takes a function
    def inner_robot():
        print("Executing", func.__name__, "function")#func.__name__ - acces the name of the f-n that is executed
        func()
        print("Finished execution")
    return inner_robot

decorated_func = decorate_robot(speak_robot)
decorated_func()