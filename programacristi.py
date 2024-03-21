import pyautogui
import datetime
import keyboard
from screeninfo import get_monitors  # Importa la función get_monitors desde la biblioteca screeninfo

def capture_screen_and_save(e):
    # Obtén el tamaño total del escritorio (que incluye todas las pantallas)
    width, height = pyautogui.size()

    # Encuentra la coordenada superior izquierda de la pantalla principal
    for monitor in get_monitors():
        if monitor.x == 0 and monitor.y == 0:
            left, top = monitor.x, monitor.y
            break
    else:
        left, top = 0, 0  # Si no se encuentra una pantalla principal, usa (0, 0)

    # Captura la pantalla principal
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    # Genera la ruta completa para el archivo en el escritorio usando la fecha y hora
    desktop_path = "C:\\Users\\Yolanda Hernández\\Desktop\\programaCristi"
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"{desktop_path}/screenshot_{current_time}.jpg"

    # Guarda la captura de pantalla como un archivo JPG
    screenshot.save(file_name, "JPEG")

    print(f"Captura de pantalla guardada como {file_name}")

# Configura la combinación de teclas para capturar la pantalla
keyboard.add_hotkey('print screen', capture_screen_and_save)

# Mantén el script en ejecución
keyboard.wait("esc")


