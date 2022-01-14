def my_generator():
    count = 100
    while count:
        yield count #we do not leave function in this place
        count -= 1



def main():
    for item in my_generator():
        print(item)

    created_generator = my_generator()

    print(next(created_generator))

    print("Hello")

    print(next(created_generator))

    print("Hi")

    for item in created_generator:
        print(item)

    print("Hey")
    for item in created_generator:
        print(item)

    print("Hey Again")
    for item in created_generator:
        print(item)



if __name__ == "__main__":
    main()