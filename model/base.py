from abc import ABC, abstractmethod
from prettytable import PrettyTable


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

    @abstractmethod
    def populate(self):
        """This method populate data info
        """
        pass

    def _load_one(self, number_identification: str):
        """This method draw the person info

        :param number_identification: (str) The identification person
        """
        model_data = self._get_model_data()
        if not len(model_data):
            self.__draw_not_has_data()
            return

        person_info = self._get_person_info(number_identification)
        if not person_info:
            self._draw_person_not_found(number_identification)
            return

        print("\n")
        x = PrettyTable()
        x.field_names = [
            "Identification number", "Date of birth",
            "Name", "Last name", "Email"
        ]
        x.add_rows([
            [
                person_info._number_identification,
                person_info._date_birth,
                person_info._name,
                person_info._last_name,
                person_info._email
            ]
        ])
        print(x)
        print("\n")

    def _get_person_info(self, number_identification: str) -> any:
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

        print("\n")
        x = PrettyTable()
        x.field_names = [
            "Identification number", "Date of birth",
            "Name", "Last name", "Email"
        ]
        for person in model_data:
            x.add_row([
                person._number_identification,
                person._date_birth,
                person._name,
                person._last_name,
                person._email
            ])
        print(x)
        print("\n")

    def __draw_not_has_data(self):
        """This method draw error log when model not have data
        """
        print("\n")
        print(f"List {self._get_entity_name()} are empty \n")
        print("\n")

    def _draw_person_not_found(self, number_identification: str):
        """This method draw error log when model not found person
        """
        print("\n")
        print(
            f"Person with identidicacion {number_identification} not found \n")
        print("\n")
