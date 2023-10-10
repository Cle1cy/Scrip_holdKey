from pynput import keyboard as kb
from pynput.keyboard import Key, Controller

keyboard = Controller()

def parse_key(key):
    key = str(key)
    key = key[1]
    return key

def press(key):
    if parse_key(key) == 'q':
        keyboard.press('q')
    else:
        exit()
    
        
def stop(key):
    print("se paró de presionar " + parse_key(key))
    
with kb.Listener(press, stop) as listener:
    listener.join()
