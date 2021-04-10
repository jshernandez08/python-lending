class Menu:

    def __init__(self, model_instances):
        self.__model_instances = model_instances

    def execute_action(self, option: str):
        """This method execute the menu action

        :param option: (str) The option selected by the user
        """
        action = {
            '1': self.get_lead,
            '2': self.__model_instances['lead_model'].get_leads
        }.get(option, None)

        if not action:
            self.exit_app()
        action()

    def get_lead(self):
        """This method call get lead info from the model
        """
        number_identification = input("Enter number identification: ")
        self.__model_instances['lead_model'].get_lead(number_identification)

    def exit_app(self):
        """This method close the app
        """
        print("\nLeaving the app thanks ...")
        exit()

    def draw_menu(self):
        """This method draw the user menu info
        """
        print("(1) Get a leap info \n")
        print("(2) Get leaps info \n")
        print("(Any number outside the menu) Exit \n\n")
