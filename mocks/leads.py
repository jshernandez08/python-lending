from datetime import datetime
from schemas.lead import Lead as LeadSchema


def get_leads_data():
    """This method obtains the leads data
    """
    return [
        LeadSchema(
            "1234", datetime(1992, 5, 17),
            "Carlos", "Vargas", "carlos@gmail.com"
        ),
        LeadSchema(
            "56789", datetime(1980, 8, 16), "Alexa", "Ruiz",
            "alexa@gmail.com"
        ),
        LeadSchema(
            "9812", datetime(1980, 8, 16), "Javier", "Correa",
            "javier@gmail.com"
        )
    ]
