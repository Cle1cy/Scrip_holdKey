from pynput import keyboard as kb

class Teclas:

    __key_press = False
    __key_stop = False
    __key_user = ""
    
    def __init__(self,key_user):
        self.__key_user = key_user
    
    def get_Key_user(self):
        return self.key_user
    
    def set_Key_user(self, key_user):
        self.__key_user = key_user
        
    def key_parse(key_user):
        key_user = str(key_user)
        key_user= key_user[1]
        return key_user
    
    def press(key):   #Get if you are pressing the "q" key
        Teclas.key_parse(key)
        print('KEY' + key_parse)

    def stop(key):  #Get if you stoped to press the "q" key
        print('stop Key ' + str(key))


    with kb.Listener(press, stop) as listener:
    	listener.join()
    
