class get_templates():
    def __init__(self, name, put_type, value_type):
        self.name = name 
        self.put_type = put_type
        self.value_type = value_type

    def input_bool_html(self, group = False, special = False):
        block = "div"
        p = "p"
        element = "element"
        element_container = "element-container"

        if special:
            group = True
            element = "special-element"

        if group: 
            block = "container"
            p = "label"
            element_container = ""

        return f"""
        <{block} class="{element} input-bool {element_container}">
            <{p} class="name bool-name">{self.name}</{p}>
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="{self.name}" value="on" checked = "true">
                <label class="form-check-label">on</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="{self.name}" value="false">
                <label class="form-check-label">off</label>
            </div>
        </{block}>"""

    def input_range_html(self, group = False, special = False):
        block = "div"
        element = "element"
        element_container = "element-container"

        if special:
            group = True
            element = "special-element"

        if group: 
            block = "container"
            element_container = ""

        val = self.value_type.split(" ")
        min_value =  val[1]
        max_value =  val[2]
        step_value = val[3] 
        return f"""
        <{block} class = "{element} input-range {element_container}">
            <label class="form-label name">{self.name}</label>
            <label class="form-label value-max"></label>
            <input type="range" class="form-range" min="{min_value}" max="{max_value}" step = "{step_value}">
        </{block}>
        """
        
    def input_text_html(self, group = False, special = False):
        block = "div"
        element = "element"
        element_container = "element-container"

        if special:
            group = True
            element = "special-element"

        if group: 
            element_container = ""
            block = "container"

        return f"""
        <{block} class="{element} input-text mb-3 {element_container}">
            <label class="form-label name">{self.name}</label>
            <input type="text" class="form-control" placeholder="Set text for {self.name}">
        </{block}>""" 
    
    def output_html(self, group = False, special = False):
        block = "div"
        element = "element"
        element_container = "element-container"

        if special:
            element = "special-element"
            group = True

        if group: 
            block = "container"
            element_container = ""

        return f"""
        <{block} class="{element} output-element mb-3 {element_container}">
            <label class="form-label name">{self.name}</label>
            <label class="form-label">:</label>
            <label class="form-label value"><..></label>
        </{block}>""" 