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
                <input class="form-check-input" type="radio" name="{self.name}" value="on" checked = "true">
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