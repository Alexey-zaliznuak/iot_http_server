from control_elemets_storage import ControlElementStorage
from models.element import element
from models.elements_maneger import elements_maneger
from models.group import group
#Put your elements here
all_elements = [

element(name = "LED-1", value_type = "bool", put_type = "input"),
#element(name = "LIDISPLAYGHT", value_type = "range 0 255 1", put_type = "input"),
group([
element(name = "R", value_type = "range 0 255 1", put_type = "input"),
element(name = "G", value_type = "range 0 255 1", put_type = "input"),
element(name = "B", value_type = "range 0 255 1", put_type = "input"),
]),

group([
element(name = "temperature", value_type = "text", put_type = "output"),
group([
element(name = "humidity-sensor", value_type = "text", put_type = "output"),
element(name = "gas-sensor", value_type = "text", put_type = "output"),
]),
]),
]

def init(update = True):
    storage = elements_maneger(all_elements)
    if update:
        storage.update_elements()
    return storage

if __name__ == "__main__":
    init()