from control_elemets_storage import ControlElementStorage
from .get_templates import get_templates
class element():
    def __init__(self, name, put_type, value_type):
        self.name = name 
        self.put_type = put_type
        self.value_type = value_type

    def add(self):
        db_path = "./data/control-elements-state.db"
        storage = ControlElementStorage(db_path, "ControlElements")
        if not storage.availability(self.name):
            storage.write(self.name, self.put_type, self.value_type)

    def get_html(self, group = False):
        html = "<h2>Type Error: type of this element not defined</h2>"
        if self.put_type == "input":
            if self.value_type == "bool":
                html = get_templates(self.name, self.put_type, self.value_type).input_bool_html(group)
            if self.value_type.startswith("range"):
                html = get_templates(self.name, self.put_type, self.value_type).input_range_html(group)
            if self.value_type == "text":
                html = get_templates(self.name, self.put_type, self.value_type).input_text_html(group)
        if self.put_type == "output":
            html = get_templates(self.name, self.put_type, self.value_type).output_html(group)
        return html