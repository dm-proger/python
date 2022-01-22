remote_menu = input("Please, make your choice: ")
def menu_bar(remote_menu):
    if remote_menu == 1:
        print(f"You are watching")
    elif remote_menu == 2:
        print(f"You are watching")
    elif remote_menu == 3:
        print(f"You are watching")
    else:
        watch_tv_restart = input("Press 0 to return to the main menu: ")
        if watch_tv_restart == 0:
            print(0)
            # main_menu()
        else:
            exit()
menu_bar(remote_menu)