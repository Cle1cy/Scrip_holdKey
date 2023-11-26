from pynput import keyboard as kb
from pynput.keyboard import Controller
import tkinter as tk
import threading

keyboard = Controller()

loop_active = False
current_listener = None

def save_selection():
    global loop_active
    global current_listener
    selected_key = key_entry.get()
    label_result.config(text=f"Tecla seleccionada: {selected_key}")
    
    if current_listener and current_listener.is_alive():
        current_listener.update_behavior(selected_key)  # Actualizar el comportamiento del hilo existente
    else:
        loop_active = True
        current_listener = CustomListener(selected_key)
        current_listener.start()
        
class CustomListener(threading.Thread):
    
    def __init__(self, selected_key):
        super().__init__()
        self.selected_key = selected_key
        self.keyboard = Controller()
        self.listener = kb.Listener(on_press=self.on_press, on_release=self.on_release)
        
    def run(self):
        self.listener.start()
        self.listener.join()
        
    @staticmethod
    def parse_key(key):
        key = str(key)
        key = key[1]
        return key
   
    def on_press(self, key):
        if loop_active and self.parse_key(key) == 'q':
            self.keyboard.release('q')
        elif loop_active and self.parse_key(key) == self.selected_key:
            self.keyboard.press('q')
            self.keyboard.release('q')
            
    def on_release(self, key):
        print("Se dejó de presionar " + self.parse_key(key))
        if key == kb.Key.esc:
            return False

    def update_behavior(self, selected_key):
        self.selected_key = selected_key

root = tk.Tk()
root.title("Seleccionar Tecla")

# Obtener las dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Definir el tamaño inicial de los widgets al 80% de la ventana
widget_width = int(screen_width * 0.8)
widget_height = int(screen_height * 0.8)

# Establecer el tamaño de la ventana
root.geometry(f"{widget_width}x{widget_height}+{screen_width // 2 - widget_width // 2}+{screen_height // 2 - widget_height // 2}")
root.resizable(True, True)  # Permitir redimensionar en ambos ejes

# Variables
key_entry = tk.Entry(root, justify='center', font=("Arial", 14))  # Cambiar la fuente y tamaño del Entry
entry_width = int(widget_width * 0.75)  # Tamaño del Entry (75% del widget)
key_entry.config(width=entry_width)

# Botón para guardar la selección
save_button = tk.Button(root, text="Guardar Selección", command=save_selection, font=("Arial", 12), bg='#4CAF50', fg='white')  # Cambiar colores y fuente del botón

# Etiqueta y campo de entrada para la tecla
label_key = tk.Label(root, text="Selecciona una tecla:", font=("Arial", 16))  # Cambiar tamaño y fuente de la etiqueta
label_result = tk.Label(root, text="Tecla seleccionada: ", font=("Arial", 14))  # Cambiar tamaño y fuente de la etiqueta

# Posicionamiento de los widgets en la ventana
label_key.pack(pady=10)  # Añadir espacio entre widgets
key_entry.pack(pady=5)  # Añadir espacio entre widgets
save_button.pack(pady=10)  # Añadir espacio entre widgets
label_result.pack(pady=10)  # Añadir espacio entre widgets

def on_closing():
    global loop_active
    loop_active = False  # Establecer el estado del hilo como inactivo
    root.destroy()  # Cerrar la ventana
    if current_listener and current_listener.is_alive():
        current_listener.join()  # Detener el hilo si está activo

root.protocol("WM_DELETE_WINDOW", on_closing)  # Llamar a la función on_closing al cerrar la ventana
root.mainloop()
