def decorate_robot(func):
    def inner_robot():
        print("Executing", func. __name__, "function")
        func()
        print("finished execution")
    return inner_robot

@decorate_robot
def speak_robot():
    print("Hello humans")

speak_robot()















