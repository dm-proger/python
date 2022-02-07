# Write a Python program to detect the number of local variables declared in a function.

def variables():
    var_01 = True
    var_02 = "string"
    var_03 = 9.23
    var_04 = [23, 34, 45, 56]
    var_05 = {}




if __name__ == "__main__":
    print(variables.__code__.co_nlocals)