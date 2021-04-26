from control_elemets_storage import ControlElementStorage
from .element import element
from .element_maneger import elements_maneger
from .get_templates import get_templates

class element(element):
    def get_html(self,):
        html = "<h2>Type Error: type of this element not defined</h2>"
        if self.put_type == "input":
            if self.value_type == "bool":
                html = get_templates(self.name, self.put_type, self.value_type).input_bool_html()
            if self.value_type.startswith("range"):
                html = get_templates(self.name, self.put_type, self.value_type).input_range_html()
            if self.value_type == "text":
                html = get_templates(self.name, self.put_type, self.value_type).input_text_html()
        if self.put_type == "output":
            html = ""
        return html