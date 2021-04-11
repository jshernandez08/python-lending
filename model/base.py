from abc import ABC, abstractmethod


class BaseModel(ABC):

    @abstractmethod
    def _get_model_data(self):
        """This method obtains the model data
        """
        return []

    @abstractmethod
    def _get_entity_name(self):
        """This method obtains the model data
        """
        return ""

    def _load_one(self, number_identification: str):
        """This method draw the person info

        :param number_identification: (str) The identification person
        """
        model_data = self._get_model_data()
        if not len(model_data):
            self.__draw_not_has_data()
            return

        person_info = self.__get_person_info(number_identification)
        if not person_info:
            self.__draw_person_not_found(number_identification)
            return

        print("\n*****************************\n")
        print(f"Identification number: {person_info._number_identification} \n")
        print(f"Date of birth: {person_info._date_birth} \n")
        print(f"Name: {person_info._name} \n")
        print(f"Last name: {person_info._last_name} \n")
        print(f"Email: {person_info._email} \n")
        print("***************************** \n\n")

    def __get_person_info(self, number_identification: str) -> any:
        """This method obtains the person info

        :param number_identification: (str) The identification person
        :return: (any) The person info
        """
        return next((
            person for person in self._get_model_data()
            if person._number_identification == number_identification
        ), None)

    def _load(self):
        """This method draw the persons info
        """
        model_data = self._get_model_data()
        if not len(model_data):
            self.__draw_not_has_data()
            return

        for person in model_data:
            print("\n*****************************\n")
            print(f"Identification number: {person._number_identification} \n")
            print(f"Date of birth: {person._date_birth} \n")
            print(f"Name: {person._name} \n")
            print(f"Last name: {person._last_name} \n")
            print(f"Email: {person._email} \n")
            print("***************************** \n\n")

    def __draw_not_has_data(self):
        """This method draw error log when model not have data
        """
        print("\n*****************************\n")
        print(f"List {self._get_entity_name()} are empty \n")
        print("***************************** \n\n")

    def __draw_person_not_found(self, number_identification: str):
        """This method draw error log when model not found person
        """
        print("\n*****************************\n")
        print(f"Person with identidicacion {number_identification} not found \n")
        print("***************************** \n\n")

