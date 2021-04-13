from datetime import datetime
from schemas.prospect import Prospect as ProspectSchema


def test_get_model_data(database):
    """This method checks if data return is correct
    """
    data = database['prospect_model']._get_model_data()
    assert len(data) > 0

    for prospect in data:
        assert isinstance(prospect, ProspectSchema)


def test_add_propect(database):
    """This method checks if data return is correct
    """
    database['prospect_model'].add_propect(
        ProspectSchema(
            "56789", datetime(1980, 8, 16),
            "Alexa", "Ruiz", "alexa@gmail.com"
        )
    )
    data = database['prospect_model']._get_model_data()
    identifications = [p._number_identification for p in data]
    assert "56789" in identifications
