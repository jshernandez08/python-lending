from datetime import datetime
from model.base import BaseModel
from schemas.lead import Lead as LeadSchema
from schemas.prospect import Prospect as ProspectSchema
from model.prospect import Prospect as ProspectModel
from external_resources.national_register import NationalRegister
from external_resources.national_judicial import NationalJudicial


class Lead(BaseModel):

    def __init__(self):
        self.__leads = []
        self.__prospect_model = None

    def set_prospect_model(self, prospect_model: ProspectModel):
        """This method set the dependencie prospect model
        """
        self.__prospect_model = prospect_model

    def _get_model_data(self):
        """This method obtains the model data
        """
        return self.__leads

    def _get_entity_name(self):
        """This method obtains the model data
        """
        return "leads"

    def __remove_lead(self, number_identification: str):
        """This method removed a lead from the current data

        :param number_identification: (str) The identification person
        """
        self.__leads = [
            lead for lead in self.__leads
            if lead._number_identification != number_identification
        ]

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
            ),
            LeadSchema(
                "9812", datetime(1980, 8, 16), "Javier", "Correa",
                "javier@gmail.com"
            )
        ]

    def _convert_in_prospect(self, number_identification: str):
        """This method verifies and convert a lead in prospect

        :param number_identification: (str) The identification person
        """
        person_info = self._get_person_info(number_identification)
        if not person_info:
            self._draw_person_not_found(number_identification)
            return

        person_national_register_info = NationalRegister()._load_one(
            number_identification
        )
        if not person_national_register_info:
            self.__draw_error_not_in_register(number_identification)
            return

        person_judicial_info = NationalJudicial()._load_one(
            number_identification
        )
        if person_judicial_info is not None:
            self.__draw_error_judicial(number_identification)
            return

        self.__remove_lead(number_identification)
        self.__prospect_model.add_propect(
            ProspectSchema(
                person_info._number_identification,
                person_info._date_birth,
                person_info._name,
                person_info._last_name,
                person_info._email
            )
        )
        self.__draw_success_convert_prospect(number_identification)

    def __draw_error_not_in_register(self, number_identification: str):
        """This method draw log error when lead no in national register
        """
        print("\n*****************************\n")
        print(
            f"Person with identidicacion {number_identification} "
            "not in national register, "
            "you can not have convert this in prospect\n"
        )
        print("***************************** \n\n")

    def __draw_error_judicial(self, number_identification: str):
        """This method draw log error when lead has judicial registers
        """
        print("\n*****************************\n")
        print(
            f"Person with identidicacion {number_identification} "
            "has judicial registers, "
            "you can not have convert this in prospect\n"
        )
        print("***************************** \n\n")

    def __draw_success_convert_prospect(self, number_identification: str):
        print("\n*****************************\n")
        print(
            f"Person with identidicacion {number_identification} "
            "convert in prospect successfully\n"
        )
        print("***************************** \n\n")

    def __calify_lead(self):
        pass
