from models.element import element
from models.elements_maneger import elements_maneger
from models.group import group
from models.special_element import special_element as special
from models.control_elemets_storage import ControlElementStorage


all_elements = [
#Put your elements here:

element(name = "LIGHTDISPLAY", value_type = "range 0 255 1", put_type = "input"),

special([
    element(name = "Red", value_type = "range 0 255 1", put_type = "input"),
    element(name = "Green", value_type = "range 0 255 1", put_type = "input"),
    element(name = "Blue", value_type = "range 0 255 1", put_type = "input"),
],name = "RGB-LED"),

# special([
#     element(name = "first", value_type = "bool", put_type = "input"),
#     element(name = "second", value_type = "bool", put_type = "input"),
#     element(name = "third", value_type = "bool", put_type = "input"),
# ],name = "LEDS"),

# group([
#     element(name = "humidity-sensor", value_type = "int", put_type = "output"),
#     element(name = "gas-sensor", value_type = "text", put_type = "output"),
#     element(name = "temperature", value_type = "text", put_type = "output"),
# ])

#//
]

def init(update = True):
    storage = elements_maneger(all_elements)
    return storage

if __name__ == "__main__":
    init()