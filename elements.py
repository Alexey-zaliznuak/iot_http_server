from models.element import element
from models.elements_maneger import elements_maneger
from models.group import group
from models.special_element import special_element as special
from models.control_elemets_storage import ControlElementStorage


inputs_elements_keys = ["LIGHTDISPLAY", "RGB-LED",]
output_elements_keys = ["humidity","temperature"]

all_elements = [
#Put your elements here:

element(name = "LIGHTDISPLAY", value_type = "range 0 255 1", put_type = "input"),

special([
    element(name = "Red", value_type = "range°С 0 255 1", put_type = "input"),
    element(name = "Green", value_type = "range°С 0 255 1", put_type = "input"),
    element(name = "Blue", value_type = "range°С 0 255 1", put_type = "input"),
],name = "RGB-LED"),


element(name = "humidity", value_type = "intMr", put_type = "output"),
element(name = "temperature", value_type = "int°С", put_type = "output"),
]


keys = []
keys += inputs_elements_keys
keys += output_elements_keys

new_keys = []
for index, element in enumerate(all_elements):
    if type(element) == special:
        new_keys += [f"special-{keys[index]}"]
    else:
        new_keys += [f"element-{keys[index]}"]
keys = new_keys

def init(update = True):
    storage = elements_maneger(all_elements)
    return storage

if __name__ == "__main__":
    init()
    