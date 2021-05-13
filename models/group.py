from models.control_elemets_storage import ControlElementStorage
from models.elements_maneger import elements_maneger
from models.element import element as element_class

class group():
    def __init__(self, elements:list):
        self.elements = elements
    def get_html(self):
        html = "<div class = 'elements-group'>"
        for element in self.elements:
            if type(element) != element_class:
                if self.elements.index(element) != len(self.elements) - 1:
                    html += element.get_html() + "\n" + "<p></p>"
                else:
                    html += element.get_html() 
            else:
                if self.elements.index(element) != len(self.elements) - 1:
                    html += element.get_html(group = True) + "\n" + "<p></p>"
                else:
                    html += element.get_html(group = True) 
        html += "</div>" + "\n"
        return html
    def get_elements(self):
        return self.elements

    def add(self):
        return elements_maneger(self.elements).get_elements_html()