from datetime import datetime


class PersonalInfo:

    def __init__(self, number_identification: str, date_birth: datetime,
                 name: str, last_name: str, email: str):
        self._number_identification = number_identification
        self._date_birth = date_birth
        self._name = name
        self._last_name = last_name
        self._email = email
