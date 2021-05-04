from control_elemets_storage import ControlElementStorage
from .get_templates import get_templates

class elements_maneger():
    def __init__(self, elements:list):
        self.elements = elements
        self.storage = ControlElementStorage("./data/control-elements-state.db", "ControlElements")

    def update_elements(self):
        self.delete_elements()
        self.add_elements()

    def delete_elements(self):
        self.storage.delete_elements()

    def get_elements_html(self, group = False):
        html = "<container>\n"
        for element in self.elements:
            html += element.get_html() + "\n"
        return html
        
    def add_elements(self):
        for element in self.elements:
            element.add()