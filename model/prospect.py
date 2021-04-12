from typing import List
from model.base import BaseModel
from mocks.prospects import get_prospects_data
from schemas.prospect import Prospect as ProspectSchema


class Prospect(BaseModel):

    def __init__(self):
        self.__prospects = []

    def _get_model_data(self) -> List[ProspectSchema]:
        """This method obtains the model data
        """
        return self.__prospects

    def _get_entity_name(self) -> str:
        """This method obtains the model data
        """
        return "prospects"

    def add_propect(self, prospect: ProspectSchema):
        """This method add a new prospect

        :param prospect: (ProspectSchema) The prospect info
        """
        self.__prospects.append(prospect)

    def populate(self):
        """This method populate prospects data info
        """
        self.__prospects = get_prospects_data()
