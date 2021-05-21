data = [
    {
        "LED-1": True,
        "LIGHTDISPLAY": "128",
        "DISPLAY": "",
        "RGB-LED": {
            "Red": "128",
            "Green": "128",
            "Blue": "128"
        },
        "time": "17/31/45"
    },
    {
        "RGB-LED": {
            "Red": "116",
            "Green": "128",
            "Blue": "128"
        },
        "time": "17/31/47"
    },
    {
        "RGB-LED": {
            "Red": "116",
            "Green": "128",
            "Blue": "0"
        },
        "time": "18/31/47"
    },
    {
        "RGB-LED": {
            "Red": "5",
            "Green": "128",
            "Blue": "128"
        },
        "time": "19/31/47"
    },
]

name = "RGB-LED"
value = [["Time"]]
value[0] += [el for el in dict(data[0][name]).keys()]
for element in data:
    time = element["time"]
    element = element[name]
    try:
        v = []
        v += [time]
        for el in dict(element).keys():
            v += [int(element[el])]
        value += [v]
    except KeyError:
        pass
print(value)