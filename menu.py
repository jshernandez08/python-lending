
def get_action(option: str) -> any:
    """This method obtains the option action

    :return: (def) The action option
    """
    return {
        '1': "Option 1"
    }.get(option, None)


def draw_menu():
    print("**************************** \n")
    print("(1) Get a leap info \n")
    print("(Any number outside the menu) Exit \n\n")
