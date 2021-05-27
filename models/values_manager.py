from datetime import datetime
from models.special_element import special_element as special
from time import perf_counter, sleep
import json

def clear(old_values, new_values, keys):
    for key in keys:
        key = key[8:]
        if key == "time": 
            continue
        last_key = None
        for val in old_values:
            try:
                last_key = val[str(key)]
            except KeyError:
                pass
        try:  
            if last_key == new_values[key]:
                new_values.pop(key)
        except KeyError as Exception:
            pass

    
    if len(new_values.items()) != 1:
        return new_values
    else:
        return None

class ValuesManeger():
    def __init__(self, start_time, keys, all_elements): 
        self.keys = keys
        self.file = "./data/data_file.json"
        self.start_time = perf_counter()
        self.all_elements = all_elements
        if not True:
            try:   
                with open(self.file, "r") as read_file:
                    data = json.load(read_file)
            except:        
                with open(self.file, "w") as write_file:
                   json.dump([], write_file, indent = 4)
        else:
            with open(self.file, "w") as write_file:
                json.dump([], write_file, indent = 4)
        new_values = {}
        for key in keys:
            if key.startswith("special"):
                new_values[key[8:]] = {}
            else:
                new_values[key[8:]] = "null"
        self.write(new_values)

    def write(self, *args):
        if len(args) == 1:
            elments = args[0]
        else:
            elments = args
        
        time = datetime.now()

        elements = elments
        #rint(elements)
        # print("value:",args)
        # elements["time"] = f"{time.hour}/{time.minute}/{time.second}{time.microsecond%10000}"
        elements["time"] = f"{time.hour}:{time.minute}:{time.second}"

        with open(self.file, "r") as read_file:
            data = json.load(read_file)
            if clear(data, elements, self.keys) is not None:
                data += [clear(data, elements, self.keys)]
        
        with open(self.file, "w") as write_file:
            json.dump(data, write_file, indent = 4)
    
    def get(self, name):
        value = [["Time",name]]
        with open(self.file, "r") as read_file:
            data = json.load(read_file)
        
        if type(data[0][name]) == str: 
            for element in data:    
                try:
                    if [[element["time"],int(element[name])]] != {}:
                        value += [[element["time"],int(element[name])]]
                except KeyError:
                    pass
                except ValueError:
                    pass
            return list(value)
        elif type(data[0][name]) == dict:
            value = [["Time"]]
            name = "RGB-LED"
            names = []
            for el in self.all_elements:
                if type(el) == special:
                    if el.name == name:
                        for el in el.elements:
                            names += [el.name]

            value[0] += names

            for element in data:
                try:
                    time = element["time"]
                    element = element[name]
                    v = []
                    v += [time]
                    for el in dict(element).keys():
                        v += [int(element[el])]
                    
                    if len(v) >1:
                        value += [v]
                except KeyError:
                    pass
            return list(value)

    def get_all(self):
        value = []
        with open(self.file, "r") as read_file:
            data = json.load(read_file)

        new_value = {}
        for v in data:
            for key in dict(v).keys():
                if key != "time":
                    new_value[key] = v[key]
        return new_value