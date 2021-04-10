from menu import draw_menu, get_action


def start_app():
    """This method starts the app"""
    run_app = True
    while run_app:
        draw_menu()
        input_user = input("Choice a option: ")
        user_action = get_action(input_user)

        if not user_action:
            print("\n Leaving the app thanks ...")
            exit()

        print(user_action)


if __name__ == '__main__':
    start_app()
