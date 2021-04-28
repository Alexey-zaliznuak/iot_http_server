from control_elemets_storage import ControlElementStorage
from models.element import element
from models.element_maneger import elements_maneger

#Put your elements here
all_elements = [

element(name = "LED-1", value_type = "bool", put_type = "input"),
element(name = "BEACON-1", value_type = "range 0 1024 1", put_type = "input"),
element(name = "DISPLAY-1", value_type = "text", put_type = "input"),

[
element(name = "temperature", value_type = "text", put_type = "output"),
element(name = "humidity-sensor", value_type = "text", put_type = "output"),
element(name = "gas-sensor", value_type = "text", put_type = "output")
],

]

def init(update = True):
    storage = elements_maneger(all_elements)
    if update:
        storage.update_elements()
    return storage

if __name__ == "__main__":
    init()