from control_elemets_storage import ControlElementStorage
from .get_templates import get_templates

class elements_maneger():
    def __init__(self, elements:list):
        self.elements = elements
        self.get_templates = get_templates
        self.storage = ControlElementStorage("./data/control-elements-state.db", "ControlElements")

        names = []
        for element in elements:
            if type(element) == list:
                for el in element:
                    if el.name in names:
                        raise ValueError(f"name {el.name} was used")
                    else:
                        names += [el.name]
                continue
            if element.name in names:
                raise ValueError(f"name {element.name} was used")
                break
            else:
                names += [element.name]

    def update_elements(self):
        self.delete_elements()
        self.add_elements()
    def delete_elements(self):
        self.storage.delete_elements()
    def get_elements_html(self):
        html = "<container>\n"
        for element in self.elements:
            if type(element) == list:
                html += "<div class = 'elements-group'>"
                for el in element:
                    if element.index(el) != len(element) - 1:
                        html += el.get_html(group = True) + "\n" + "<p></p>"
                    else:
                        html += el.get_html(group = True) 
                html += "</div>" + "\n"
            else:
                html += element.get_html() + "\n"
        return html
    def add_elements(self):
        for element in self.elements:
            if type(element) == list:
                for el in element:
                    el.add()
                continue
            element.add()