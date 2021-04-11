from datetime import datetime
from model.base import BaseModel
from schemas.lead import Lead as LeadSchema


class Lead(BaseModel):

    def __init__(self):
        self.__leads = []

    def _get_model_data(self):
        """This method obtains the model data
        """
        return self.__leads

    def _get_entity_name(self):
        """This method obtains the model data
        """
        return "leads"

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

    def convert_in_prospect(self):
        pass

    def __calify_lead(self):
        pass
