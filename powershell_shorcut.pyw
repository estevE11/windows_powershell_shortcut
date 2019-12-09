import sys
import subprocess
from pynput import keyboard
from infi.systray import SysTrayIcon

keys = {}
combo_keys = []
ps_dir = "C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"

running = True

def main():
    global combo_keys
    combo_keys = open("keycombo.txt", "r").read().split(" ")
    print(combo_keys)

#    if sys.argv[1] != "none":
#i        ps_dir = sys.argv[1]

    for i in range(len(combo_keys)):
        keys[combo_keys[i]] = False

    with keyboard.Listener(on_press=key_pressed, on_release=key_released) as listener:
        listener.join()

def key_pressed(key):
    global combo_keys, running
    if running == False:
        return False
    key = format_key_string(key)
    print(key)
    keys[str(key)] = True
    run = True
    for k in combo_keys:
        print(keys[k])
        if keys[k] == False:
            run = False
    if run:
        print("Running powershel (or trying at least)")
        for i in range(len(combo_keys)):
            keys[combo_keys[i]] = False
        subprocess.call(ps_dir)


def key_released(key):
    if running == False:
        return False
    key = format_key_string(key)
    keys[str(key)] = False

def format_key_string(key):
    key = "{0}".format(key)
    if key.startswith("Key."):
        key = key[4:]

    if(key.startswith("'")):
        key = key[1:-1]

    return key

def on_quit_callback(systray):
    global running
    running = False

systray = SysTrayIcon("", "Power Shell Shortcut", None, on_quit=on_quit_callback)
systray.start()
main()