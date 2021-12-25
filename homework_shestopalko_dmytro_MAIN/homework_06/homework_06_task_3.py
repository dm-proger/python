def is_name_valid(name_from_storage: str, name_from_input:str) -> bool:
    return name_from_storage == name_from_input.lower()


def name_check() -> None:
    name = 'dmytro'
    user_name = input("Enter your name: ")

    is_equal = is_name_valid(name_from_storage=name, name_from_input=user_name)

    message_about_state = "" if is_equal else "not"
    message = f'Name{name} is {message_about_state} equal to {user_name}'
    print(message)


if __name__ == "__main__":
    name_check()
