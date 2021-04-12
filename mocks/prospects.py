from typing import List
from datetime import datetime
from schemas.prospect import Prospect as ProspectSchema


def get_prospects_data() -> List[ProspectSchema]:
    """This method obtains the prospects data
    """
    return [
        ProspectSchema(
            "09876", datetime(1970, 5, 17),
            "Juan", "Rodriguez", "juan@gmail.com"
        ),
        ProspectSchema(
            "54321", datetime(1980, 11, 16), "Sandra", "Valencia",
            "sandra@gmail.com"
        )
    ]
