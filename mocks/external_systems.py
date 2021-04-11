from datetime import datetime
from schemas.personal_info import PersonalInfo as PersonalInfoSchema


def get_national_register_data():
    """This method obtains the national register data
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


def get_national_judicial_data():
    """This method obtains the national judicial data
    """
    return [
        PersonalInfoSchema(
            "1234", datetime(1992, 5, 17),
            "Carlos", "Vargas", "carlos@gmail.com"
        )
    ]
