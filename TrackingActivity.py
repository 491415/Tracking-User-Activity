import datetime
import win32gui

w = win32gui
date = datetime.datetime.now()
oldWindow = ""

while True:
    window = w.GetWindowText(w.GetForegroundWindow())
    if window != oldWindow:
        f = open("task.txt", "a+")
        print("Current open window name: %s. Current time and date: %s .\n" % (window, datetime.datetime.now()))
        oldWindow = window
        f.write("Current open window name is: %s. Current time and date is: %s .\n" % (window, datetime.datetime.now()))
        f.close()

# Delete all from file
# open("task.txt", "w").close()
