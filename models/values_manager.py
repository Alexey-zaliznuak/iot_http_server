from datetime import datetime
from time import perf_counter, sleep
import json

def clear(old_values, new_values):
    try:
        keys = list(old_values[0].keys())
    except IndexError:
        return new_values
    else:
        for key in keys:
            if key == "time": 
                continue
            last_key = None
            for val in old_values:
                try:
                    last_key = val[str(key)]
                except KeyError:
                    pass
            if last_key == new_values[key]:
                new_values.pop(key)
    return new_values

class ValuesManeger():
    def __init__(self, start_time, new = True,): 
        self.file = "./data/data_file.json"
        self.start_time = perf_counter()
        if not new:
            try:   
                with open(self.file, "r") as read_file:
                    data = json.load(read_file)
            except:        
                print("Value maneger: created new data file")
                with open(self.file, "w") as write_file:
                   json.dump([], write_file, indent = 4)
        else:
            with open(self.file, "w") as write_file:
                json.dump([], write_file, indent = 4)

    def write(self, *args):
        if len(args) == 1:
            elments = args[0]
        else:
            elments = args
        
        time = datetime.now()

        elements = elments
        print("value:",args)
        elements["time"] = f"{time.hour}/{time.minute}/{time.second}/{time.microsecond%10000}"
        elements["time"] = f"{time.hour}:{time.minute}:{time.second}"

        with open(self.file, "r") as read_file:
            data = json.load(read_file)
            data += [clear(data, elements)]
        
        with open(self.file, "w") as write_file:
            json.dump(data, write_file, indent = 4)
    
    def get(self, name):
        value = [["Time",name]]
        with open(self.file, "r") as read_file:
            data = json.load(read_file)
        
        print(data[0][name], type(data[0][name]))
        
        if type(data[0][name]) == str: 
            for element in data:    
                try:
                    value += [[element["time"],int(element[name])]]
                except KeyError:
                    pass
            return list(value)
        elif type(data[0][name]) == dict:
            value = [["Time"]]
            value[0] += [el for el in dict(data[0][name]).keys()]
            for element in data:
                try:
                    time = element["time"]
                    element = element[name]

                    v = []
                    v += [time]
                    for el in dict(element).keys():
                        v += [int(element[el])]

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
            value += [new_value]
        return value