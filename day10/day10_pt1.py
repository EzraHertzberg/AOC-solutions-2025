import time
import os

bpm = 20
interval = 60 / bpm

chords = ["f","c"]
counter = 0
cur_cord = 0

while True:
    os.system("cls")
    counter = counter + 1

    if counter == 3:
        counter = 1
        if cur_cord < len(chords) - 1:
            cur_cord += 1
        else:
            cur_cord = 0
            
    if chords[cur_cord] == "f":
        print(f"{counter} F chord 2 sharps")
    else:
        print(f"  {counter} C chord 3 sharps")
    time.sleep(interval)