from datetime import datetime
from external_resources.base_system import BaseSystem
from schemas.personal_info import PersonalInfo as PersonalInfoSchema


class NationalRegister(BaseSystem):

    def _get_system_data(self):
        """This method obtains the system data
        """
        return [
            PersonalInfoSchema(
                "1234", datetime(1992, 5, 17),
                "Carlos", "Vargas", "carlos@gmail.com"
            ),
            PersonalInfoSchema(
                "56789", datetime(1980, 8, 16), "Alexa", "Ruiz",
                "alexa@gmail.com"
            )
        ]
