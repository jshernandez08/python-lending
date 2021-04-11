from datetime import datetime
from model.base import BaseModel
from schemas.prospect import Prospect as ProspectSchema


class Prospect(BaseModel):

    def __init__(self):
        self.__prospects = []

    def _get_model_data(self):
        """This method obtains the model data
        """
        return self.__prospects

    def _get_entity_name(self):
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
