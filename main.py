# print("Current open window name: %s. Current time and date: %s .\n" % (window, datetime.datetime.now()))
import datetime
import win32gui
import json
import time

def loadData(filePath:str):
    try:
        with open(filePath, "r") as file:
            return json.load(file)
    except:
        return {}
def saveData(filePath:str, data:str):
    with open(filePath, "w") as file:
        json.dump(data, file)

w = win32gui
date = datetime.datetime.now()
oldWindow = ""
oldTime = datetime.datetime.now()
DATA_FILE = "data.json"

while True:
    window = w.GetWindowText(w.GetForegroundWindow()).split("- ")[-1]
    data = loadData(DATA_FILE)
    
    try:
        data[window] += 1
    except:
        data[window] = 0

    saveData(DATA_FILE, data)
    time.sleep(1)