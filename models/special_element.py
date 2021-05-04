from control_elemets_storage import ControlElementStorage
from models.elements_maneger import elements_maneger
from models.element import element as element_class

class special_element():
    def __init__(self, elements:list, name:str, value_type = "list"):
        self.elements = elements
        self.value_type = value_type
        self.name = name
        if self.value_type not in ["list", "dict", "str"]:
            raise ValueError(f"{value_type} not in ['list', 'dict', 'str']")

    def get_html(self):
        html = f"<div class = 'special-element-group' value_type = {str(self.value_type)} name = {self.name}>"
        html += f'<p><label class="form-label special-name">{self.name}</label></p>'
        for element in self.elements:
            if type(element) != element_class:
                if self.elements.index(element) != len(self.elements) - 1:
                    html += element.get_html() + "\n" + "<p></p>"
                else:
                    html += element.get_html() 
            else:
                if self.elements.index(element) != len(self.elements) - 1:
                    html += element.get_html(special = True) + "\n" + "<p></p>"
                else:
                    html += element.get_html(special = True) 
        html += "</div>" + "\n"
        return html
            
    def add(self):
        return elements_maneger(self.elements).get_elements_html()