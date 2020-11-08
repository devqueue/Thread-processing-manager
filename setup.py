from cx_Freeze import setup, Executable


executables = [Executable("process-handler.py", base = "Win32GUI")]

packages = ["idna", "sys", "glob", "webbrowser", "time", "os", "random", "threading", "ctypes", "plyer", "pynput", "pyautogui"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Process handler",
    options = options,
    version = "0.1.1",
    description = 'This is an application that handles background apps and kills the ones you dont use',
    executables = executables
)