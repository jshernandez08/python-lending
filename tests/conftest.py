import pytest
from model.lead import Lead as LeadModel
from model.prospect import Prospect as ProspectModel


@pytest.fixture(scope="package")
def database():
    """This method populate all data for the tests
    """
    model_instances = {
        'lead_model': LeadModel(),
        'prospect_model': ProspectModel()
    }
    for model_instance in model_instances.values():
        model_instance.populate()
    return model_instances
