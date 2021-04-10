from model.lead import Lead as LeadModel
from menu import Menu


model_instances = {
    'lead_model': LeadModel()
}


def populate_database():
    """This method populate all data for the app
    """
    for model_instance in model_instances.values():
        model_instance.populate()


def start_app():
    """This method starts the app"""
    populate_database()
    menu = Menu(model_instances)
    while True:
        menu.draw_menu()
        input_user = input("Choice a option: ")
        menu.execute_action(input_user)


if __name__ == '__main__':
    start_app()
