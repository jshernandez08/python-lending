from schemas.personal_info import PersonalInfo as PersonalInfoSchema
from abc import ABC, abstractmethod


class BaseSystem(ABC):

    @abstractmethod
    def _get_system_data(self):
        """This method obtains the system data
        """
        return []

    def _load_one(self, number_identification: str) -> PersonalInfoSchema:
        """This method gets the person info from external system

        :param number_identification: (str) The identification person
        :return: (PersonalInfoSchema) The person info
        """
        system_data = self._get_system_data()
        if not len(system_data):
            return None

        return next((
            person for person in system_data
            if person._number_identification == number_identification
        ), None)
