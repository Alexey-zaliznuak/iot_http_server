from control_elemets_storage import ControlElementStorage
from models.element_models import *

#Put your elements here
all_elements = [

element(name = "LED-1", value_type = "bool", put_type = "input"),
element(name = "BEACON", value_type = "range 0 1024 1", put_type = "input"),
element(name = "DISPLAY", value_type = "text", put_type = "input")

]

def init():
    storage = elements_manager(all_elements)
    storage.update_elements()
    return storage

if __name__ == "__main__":
    init()