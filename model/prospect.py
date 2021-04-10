from datetime import datetime
from schemas.prospect import Prospect as ProspectSchema


class Prospect:

    def __init__(self):
        self.__prospects = []

    def get_prospect(self, number_identification: str):
        """This method draw the prospect info

        :param number_identification: (str) The identification prospect
        """
        if not len(self.__prospects):
            self.__draw_not_has_prospects()
            return

        prospect_info = self.__get_prospect_info(number_identification)
        if not prospect_info:
            self.__draw_prospect_not_found(number_identification)
            return

        print("\n*****************************\n")
        print(f"Identification number: {prospect_info._number_identification} \n")
        print(f"Date of birth: {prospect_info._date_birth} \n")
        print(f"Name: {prospect_info._name} \n")
        print(f"Last name: {prospect_info._last_name} \n")
        print(f"Email: {prospect_info._email} \n")
        print("***************************** \n\n")

    def __get_prospect_info(
            self, number_identification: str) -> ProspectSchema:
        """This method obtains the prospect info

        :param number_identification: (str) The identification prospect
        :return: (ProspectSchema) The prospect info
        """
        return next((
            prospect for prospect in self.__prospects
            if prospect._number_identification == number_identification
        ), None)

    def get_prospects(self):
        """This method draw the prospects info
        """
        if not len(self.__prospects):
            self.__draw_not_has_prospects()
            return

        for prospect in self.__prospects:
            print("\n*****************************\n")
            print(f"Identification number: {prospect._number_identification} \n")
            print(f"Date of birth: {prospect._date_birth} \n")
            print(f"Name: {prospect._name} \n")
            print(f"Last name: {prospect._last_name} \n")
            print(f"Email: {prospect._email} \n")
            print("***************************** \n\n")

    def populate(self):
        """This method populate prospects data info
        """
        self.__prospects = [
            ProspectSchema(
                "09876", datetime(1970, 5, 17),
                "Juan", "Rodriguez", "juan@gmail.com"
            ),
            ProspectSchema(
                "54321", datetime(1980, 11, 16), "Sandra", "Valencia",
                "sandra@gmail.com"
            )
        ]

    def __draw_not_has_prospects(self):
        """This method draw error log when model not has prospects data
        """
        print("\n*****************************\n")
        print("List prospects are empty \n")
        print("***************************** \n\n")

    def __draw_prospect_not_found(self, number_identification: str):
        """This method draw error log when model not found prospect
        """
        print("\n*****************************\n")
        print(f"prospect with identidicacion {number_identification} not found \n")
        print("***************************** \n\n")
