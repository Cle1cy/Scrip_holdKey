from pynput import keyboard as kb
import pyautogui

key_press = False
key_user = ""
typing_active = False  # Variable para rastrear si estás escribiendo con pyautogui

def parse_key(key):
    key = str(key)
    key = key[1]
    return key

def press(key):
    global typing_active
    
    if parse_key(key) == 'q':
        typing_active = True
        pyautogui.write('q') 

def stop(key):
    global typing_active
    
    if typing_active:
        typing_active = False
    else:
        print("se paró de presionar " + parse_key(key))

with kb.Listener(press, stop) as listener:
    listener.join()
