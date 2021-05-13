from models.control_elemets_storage import ControlElementStorage
from .get_templates import get_templates
class element():
    def __init__(self, name, put_type, value_type):
        self.name = name 
        self.put_type = put_type
        self.value_type = value_type
       

    def get_html(self, group = False, special = False):
        html = f"<center><h2>Type Error: element type '{self.value_type}' not defined</h2></center>"

        db_path = "./data/control-elements-state.db"
        storage = ControlElementStorage(db_path, "ControlElements")
        if not storage.availability(self.name):
           storage.write(self.name, self.put_type, self.value_type)
           
        if self.put_type == "input":
            if self.value_type == "bool":
                html = get_templates(self.name, self.put_type, self.value_type).input_bool_html(group, special)
            if self.value_type.startswith("range"):
                html = get_templates(self.name, self.put_type, self.value_type).input_range_html(group, special)
            if self.value_type == "text":
                html = get_templates(self.name, self.put_type, self.value_type).input_text_html(group, special)
        if self.put_type == "output":
            html = get_templates(self.name, self.put_type, self.value_type).output_html(group, special)
        return html