from schemas.lead import Lead as LeadSchema


def test_get_model_data(database):
    """This method checks if data return is correct
    """
    data = database['lead_model']._get_model_data()
    assert len(data) > 0

    for lead in data:
        assert isinstance(lead, LeadSchema)


def test_remove_lead(database):
    """This method checks if data return is correct
    """
    database['lead_model']._Lead__remove_lead("1234")
    data = database['lead_model']._get_model_data()
    for lead in data:
        assert not lead._number_identification == "1234"


def test_calify(database):
    """This method checks if data return is correct
    """
    calification = database['lead_model']._Lead__calify()
    assert calification >= 0 and calification <= 100
