from mocks.external_systems import get_national_register_data
from external_resources.base_system import BaseSystem


class NationalRegister(BaseSystem):

    def _get_system_data(self):
        """This method obtains the system data
        """
        return get_national_register_data()
