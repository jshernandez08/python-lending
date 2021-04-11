from mocks.external_systems import get_national_judicial_data
from external_resources.base_system import BaseSystem


class NationalJudicial(BaseSystem):

    def _get_system_data(self):
        """This method obtains the system data
        """
        return get_national_judicial_data()
