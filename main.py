from pynput import keyboard as kb
from pynput.keyboard import Controller

keyboard = Controller()

q_pressed = False  # Variable para rastrear el estado de la tecla 'q'

def parse_key(key):
    key = str(key)
    key = key[1]
    return key

def on_press(key):
    global q_pressed
    if parse_key(key) == 'q' and not q_pressed:
        keyboard.press('q')
        q_pressed = True

def on_release(key):
    global q_pressed
    print("se paró de presionar " + parse_key(key))
    if key == kb.Key.esc:
        return False
    if parse_key(key) == 'q' and q_pressed:
        keyboard.release('q')
        q_pressed = False
    
with kb.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
