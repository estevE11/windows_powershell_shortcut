import sys
import subprocess
from pynput import keyboard

keys = {}
ps_dir = "C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"

def main():
    if len(sys.argv) < 3:
        return

    if sys.argv[1] != "none":
        ps_dir = sys.argv[1]

    for i in range(len(sys.argv)-2):
        keys[sys.argv[i+2]] = False
    print(keys)

    with keyboard.Listener(on_press=key_pressed, on_release=key_released) as listener:
        listener.join()

def key_pressed(key):
    print('{0} pressed'.format(key))
    keys[str(key)] = True
    run = True
    for key in keys:
        if keys[key] == False:
            run = False
    if run:
        subprocess.call(ps_dir)

def key_released(key):
    print('{0} pressed'.format(key))
    keys[str(key)] = False

main()