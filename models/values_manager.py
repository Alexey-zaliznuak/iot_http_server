from datetime import datetime
import json

def current_time():
    times = datetime.now()
    #day = times.day

    hour = times.hour
    minute = times.minute
    second = times.second
    microseconds = times.microsecond
    
    if len(str(minute)) < 2:
        minute = f"0{minute}"

    if len(str(hour)) < 2:
        hour = f"0{hour}"

    mod_time = f"{hour}/{minute}/{second}/{str(microseconds)}"
    return mod_time

class ValuesManeger():
    def __init__(self, new = True): 
        if not new:
            try:   
                with open("data_file.json", "r") as read_file:
                    data = json.load(read_file)
            except:        
                print("Value maneger: created new data file")
                with open("data_file.json", "w") as write_file:
                   json.dump([], write_file, indent = 4)
        else:
            with open("data_file.json", "w") as write_file:
                json.dump([], write_file, indent = 4)

    def write(self, *args):
        if len(args) == 1:
            elments = args[0]
        else:
            elments = args

        elements = elments
        print(elements)
        elements["time"] = current_time()

        with open("data_file.json", "r") as read_file:
            data = json.load(read_file)
            data += [elements]
        
        with open("data_file.json", "w") as write_file:
            json.dump(data, write_file, indent = 4)
    
    def get(self, name):
        value = []
        with open("data_file.json", "r") as read_file:
            data = json.load(read_file)
        
        for element in data:
            for el in element:
                try:
                    value += [{el[name]:element[len(element)-1]["time"]}]
                except KeyError:
                    pass
        return value