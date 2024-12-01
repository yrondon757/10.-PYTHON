# Vamos a instalar pyautogui
# pip install pyautogui
import pyautogui, webbrowser, time, threading, os

def app():
  while True:
    print("---------- Bienvenido al spam de Whatsapp -------------")
    print("El numero debe llevar su codigo de pais (Ejemplo: +58)")
    numero = input("Ingresa el numero que deseas spamear\n")
    os.system("cls")
    mensaje = input("Ingresa lo que deseas spamear\n")
    os.system("cls")
    tiempoDeSpam = input("Cuantos segundos quieres que dure el spam?\n")
    os.system("cls")
    tiempoDeEnvio = input("Cada cuantos segundos quieres que se envie el mensaje?\n")
    os.system("cls")
    print("Estas seguro que quieres continuar?")
    input("Presione ENTER para hacer el spam")
    os.system("cls")
    print("Cargando...")
    webbrowser.open("https://web.whatsapp.com/send?phone=" + numero)
    time.sleep(10)
    
    def timer(timer_runs):
      while timer_runs.is_set():
        pyautogui.typewrite(str(mensaje))
        pyautogui.press("enter")
        time.sleep(int(tiempoDeEnvio))
        
    timer_runs = threading.Event()
    timer_runs.set()
    
    t = threading.Thread(target=timer, args=(timer_runs,))
    t.start()
    time.sleep(int(tiempoDeSpam))
    timer_runs.clear()
    os.system("cls")
    print("El spam fue realizado Exitosamente!")
    break
  
app()