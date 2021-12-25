# Task 1

x = input('two words and more')
if len(x) >= 2:
    y = x[:+2] + x[-2:]
else:
    y = 'Empty String'
print(x)

'''
input_string = "hello world"

l = len(input_string)
new_string = ""

for i in range(0, len(input_string)):
    if l < 2:
        break
    else:
        if i in (0, 1, l - 2, l - 1):
            new_string = new_string + input_string[i]
        else:
            continue

print("New String : " + new_string)

'''

# I have copied the essential part of this code from
# https://www.geeksforgeeks.org/python-create-a-string-made-of-the-first-and-last-two-characters-from-a-given-string/
# due to fact I didn`t know how to make it

#Task 2
'''
phone_number = input("Enter your phone number: ")
phone_number = type(int)
length = len(phone_number)
    if length == 10:
        print("Thank you for submitting the form")
    elif len > 10:
        print("Please, check the number again")
    elif len < 10:
        print("Please, check the number again")
    else:
        print("The wrong value")
        
'''
# Task 3
def name_check():
    name='dmytro'
    user_name = input("Enter your name: ")

    if name == user_name.lower():
        return True
    else:
        return False

    if __name__ == "__main__":
        print(name_check())

'''
name = input("Enter your name: dmytro")
if name == "Dmytro":
    print(True)
elif name =="dmytro":
    print(True)
else:
print("Enter the correct name")

'''

'''
x = '0123456789'
if  x.isdigit() == True:
    if len(x) == 10:
        print("Okey, it's a correct number")
    else:
        print("Your number must be 10 characters long")
else:
    print("It's not a number!")
    
'''
