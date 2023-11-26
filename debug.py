from pynput import keyboard as kb
from pynput.keyboard import Controller

keyboard = Controller()

#def parse_key(key):
#    key = str(key)
#    key = key[1]
#    return key

def on_press(key):
    if parse_key(key) == 'z':
        keyboard.press('q')   
        keyboard.release('q')
        
        
def on_release(key):
    print("se paró de presionar " + parse_key(key))
    if key == kb.Key.esc:
        return False
    
with kb.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
