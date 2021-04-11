from schemas.personal_info import PersonalInfo as PersonalInfoSchema
from abc import ABC, abstractmethod


class BaseSystem(ABC):

    @abstractmethod
    def _get_system_data(self):
        """This method obtains the system data
        """
        return []

    def _load_one(self, query: dict) -> PersonalInfoSchema:
        """This method gets the person info from external system

        :param query: (dict) The query to applied
        :return: (PersonalInfoSchema) The person info
        """
        system_data = self._get_system_data()
        if not len(system_data):
            return None

        return next((
            person for person in system_data
            if self.__is_valid_data(person, query)
        ), None)

    def __is_valid_data(self, person: PersonalInfoSchema, query: dict) -> bool:
        """This method check if all person data is according to query sent

        :param person: (PersonalInfoSchema) The person info
        :param query: (dict) The query to applied
        :return: (bool) Is valid data
        """
        return (
            person._number_identification ==
            query.get('number_identification') and
            person._date_birth == query.get('date_birth') and
            person._name == query.get('name') and
            person._last_name == query.get('last_name') and
            person._email == query.get('email')
        )
