class Menu:

    def __init__(self, model_instances: dict):
        self.__model_instances = model_instances

    def execute_action(self, option: str):
        """This method execute the menu action

        :param option: (str) The option selected by the user
        """
        action = {
            '1': self.__model_instances['lead_model']._load,
            '2': self.__get_lead,
            '3': self.__convert_in_prospect,
            '4': self.__model_instances['prospect_model']._load,
            '5': self.__get_prospect
        }.get(option, None)

        if not action:
            self.exit_app()
        action()

    def __get_lead(self):
        """This method call get lead info from the model
        """
        number_identification = input("Enter number identification: ")
        self.__model_instances['lead_model']._load_one(number_identification)

    def __convert_in_prospect(self):
        """This method call convert lead in prospect from the model
        """
        number_identification = input("Enter number identification: ")
        self.__model_instances['lead_model']._convert_in_prospect(
            number_identification
        )

    def __get_prospect(self):
        """This method call get prospect info from the model
        """
        number_identification = input("Enter number identification: ")
        self.__model_instances['prospect_model']._load_one(
            number_identification
        )

    def exit_app(self):
        """This method close the app
        """
        print("\nLeaving the app thanks ...")
        exit()

    def draw_menu(self):
        """This method draw the user menu info
        """
        print("(1) Get leaps info \n")
        print("(2) Get a leap info \n")
        print("(3) Convert lead in prospect \n")
        print("(4) Get prospects info \n")
        print("(5) Get prospect info \n")
        print("(Any number outside the menu) Exit \n\n")
