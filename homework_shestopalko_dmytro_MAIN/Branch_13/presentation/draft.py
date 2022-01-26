def speak_robot():
    print("Hello humans!")

def decorate_robot(func):
    def inner_robot():
        print("executing", func.__name__, "function")
        func()
        print("Finished execution")
    return inner_robot

decorated_func = decorate_robot(speak_robot)
decorated_func()
