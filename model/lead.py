from typing import List
from random import randint
from multiprocessing import Pool
from model.base import BaseModel
from mocks.leads import get_leads_data
from schemas.prospect import Prospect as ProspectSchema
from schemas.lead import Lead as LeadSchema
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

    def _get_model_data(self) -> List[LeadSchema]:
        """This method obtains the model data
        """
        return self.__leads

    def _get_entity_name(self) -> str:
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
        self.__leads = get_leads_data()

    def _convert_in_prospect(self, number_identification: str):
        """This method verifies and convert a lead in prospect

        :param number_identification: (str) The identification person
        """
        person_info = self._get_person_info(number_identification)
        if not person_info:
            self._draw_person_not_found(number_identification)
            return

        query = {
            'number_identification': person_info._number_identification,
            'date_birth': person_info._date_birth,
            'name': person_info._name,
            'last_name': person_info._last_name,
            'email': person_info._email
        }

        # connect with external systems parallelly
        pool = Pool()
        conn_national_register = pool.apply_async(
            NationalRegister()._load_one, (query,)
        )
        conn_national_judicial = pool.apply_async(
            NationalJudicial()._load_one, (query,)
        )
        person_national_register_info = conn_national_register.get()
        person_judicial_info = conn_national_judicial.get()

        if not person_national_register_info:
            self.__draw_error_not_in_register(number_identification)
            return

        if person_judicial_info is not None:
            self.__draw_error_judicial(number_identification)
            return

        person_score = self.__calify()
        if person_score < 60:
            self.__draw_error_score(number_identification, person_score)
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

    def __draw_error_score(self, number_identification: str, score: int):
        """This method draw log error when lead has score less than 60
        """
        print("\n*****************************\n")
        print(
            f"Person with identidicacion {number_identification} "
            f"has a score equal to {score} and this score less than 60, so "
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

    def __calify(self):
        """This method obtains a random score for a lead

        :return: (int) The random score
        """
        return randint(0, 100)
