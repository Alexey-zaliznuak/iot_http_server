from control_elemets_storage import ControlElementStorage
class get_templates():
    def __init__(self, name, put_type, value_type):
        self.name = name 
        self.put_type = put_type
        self.value_type = value_type
    def input_bool_html(self):
        return f"""
        <div class="element-container input-bool">
            <p class="form-label name">{self.name}</p>
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="{self.name}" value="onn" checked = "true">
                <label class="form-check-label">onn</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="{self.name}" value="false">
                <label class="form-check-label">off</label>
            </div>
        </div>"""

    def input_range_html(self):
        val = self.value_type.split(" ")
        min_value =  val[1]
        max_value =  val[2]
        step_value = val[3] 
        return f"""
        <div class = "element-container input-range">
            <label class="form-label name">{self.name}</label>
            <label class="form-label value-max"></label>
            <input type="range" class="form-range" min="{min_value}" max="{max_value}" step = "{step_value}">
        </div>
        """
        
    def input_text_html(self):
        return f"""
        <div class="element-container input-text mb-3">
            <label class="form-label name">{self.name}</label>
            <input type="text" class="form-control" placeholder="Set text for {self.name}">
        </div>""" 
class elements_manager():
    def __init__(self, elements:list):
        self.elements = elements
        self.get_templates = get_templates
        self.storage = ControlElementStorage("./data/control-elements-state.db", "ControlElements")
    def update_elements(self):
        self.delete_elements()
        self.add_elements()
    def delete_elements(self):
        self.storage.delete_elements()
    def get_elements_html(self):
        html = "<container>\n"
        for element in self.elements:
            html += element.get_html() + "\n"
        return html
    def add_elements(self):
        for element in self.elements:
            element.add()
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

    def get_html(self):
        html = "<h2>Type Error: type of this element not defined</h2>"
        if self.put_type == "input":
            if self.value_type == "bool":
                html = get_templates(self.name, self.put_type, self.value_type).input_bool_html()
            if self.value_type.startswith("range"):
                html = get_templates(self.name, self.put_type, self.value_type).input_range_html()
            if self.value_type == "text":
                html = get_templates(self.name, self.put_type, self.value_type).input_text_html()
        if self.put_type == "output":
                pass
        return html