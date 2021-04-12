from typing import List
from mocks.external_systems import get_national_register_data
from schemas.personal_info import PersonalInfo as PersonalInfoSchema
from external_resources.base_system import BaseSystem


class NationalRegister(BaseSystem):

    def _get_system_data(self) -> List[PersonalInfoSchema]:
        """This method obtains the system data
        """
        return get_national_register_data()
