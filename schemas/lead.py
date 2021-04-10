from datetime import datetime
from app.schemas.personal_info import PersonalInfo


class Lead(PersonalInfo):

    def __init__(self, number_identification: str, date_birth: datetime,
                 name: str, last_name: str, email: str):
        super().__init__(
            number_identification,
            date_birth,
            name,
            last_name,
            email
        )
