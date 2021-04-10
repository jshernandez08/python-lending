from datetime import datetime
from schemas.lead import Lead as LeadSchema


class Lead:

    def __init__(self):
        self.__leads = []

    def get_lead(self, number_identification: str):
        """This method draw the lead info

        :param number_identification: (str) The identification lead
        """
        if not len(self.__leads):
            self.__draw_not_has_leads()
            return

        lead_info = self.__get_lead_info(number_identification)
        if not lead_info:
            self.__draw_lead_not_found(number_identification)
            return

        print("\n*****************************\n")
        print(f"Identification number: {lead_info._number_identification} \n")
        print(f"Date of birth: {lead_info._date_birth} \n")
        print(f"Name: {lead_info._name} \n")
        print(f"Last name: {lead_info._last_name} \n")
        print(f"Email: {lead_info._email} \n")
        print("***************************** \n\n")

    def __get_lead_info(self, number_identification: str) -> LeadSchema:
        """This method obtains the lead info

        :param number_identification: (str) The identification lead
        :return: (LeadSchema) The lead info
        """
        return next((
            lead for lead in self.__leads
            if lead._number_identification == number_identification
        ), None)

    def get_leads(self):
        """This method draw the leads info
        """
        if not len(self.__leads):
            self.__draw_not_has_leads()
            return

        for lead in self.__leads:
            print("\n*****************************\n")
            print(f"Identification number: {lead._number_identification} \n")
            print(f"Date of birth: {lead._date_birth} \n")
            print(f"Name: {lead._name} \n")
            print(f"Last name: {lead._last_name} \n")
            print(f"Email: {lead._email} \n")
            print("***************************** \n\n")

    def populate(self):
        """This method populate leads data info
        """
        self.__leads = [
            LeadSchema(
                "1234", datetime(1992, 5, 17),
                "Carlos", "Vargas", "carlos@gmail.com"
            ),
            LeadSchema(
                "56789", datetime(1980, 8, 16), "Alexa", "Ruiz",
                "alexa@gmail.com"
            )
        ]

    def __draw_not_has_leads(self):
        """This method draw error log when model not has leads data
        """
        print("\n*****************************\n")
        print("List leads are empty \n")
        print("***************************** \n\n")

    def __draw_lead_not_found(self, number_identification: str):
        """This method draw error log when model not found lead
        """
        print("\n*****************************\n")
        print(f"Lead with identidicacion {number_identification} not found \n")
        print("***************************** \n\n")

    def convert_in_prospect(self):
        pass

    def __calify_lead(self):
        pass
