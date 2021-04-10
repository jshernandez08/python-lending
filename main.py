from menu import draw_menu


def get_action(option):
    """This method obtains the option action

    :return: (def) The action option
    """
    return {
        '1': "Option 1"
    }.get(option, None)


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
