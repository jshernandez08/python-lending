from model.lead import Lead as LeadModel
from model.prospect import Prospect as ProspectModel
from menu import Menu


model_instances = {
    'lead_model': LeadModel(),
    'prospect_model': ProspectModel()
}


def populate_database():
    """This method populate all data for the app
    """
    for model_instance in model_instances.values():
        model_instance.populate()


def add_dependencies():
    """This method add dependencies models
    """
    model_instances['lead_model'].set_prospect_model(
        model_instances['prospect_model']
    )


def start_app():
    """This method starts the app"""
    populate_database()
    add_dependencies()
    menu = Menu(model_instances)
    while True:
        menu.draw_menu()
        input_user = input("Choice a option: ")
        menu.execute_action(input_user)


if __name__ == '__main__':
    start_app()
