from control_elemets_storage import ControlElementStorage
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