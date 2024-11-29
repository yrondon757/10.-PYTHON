# Instalar esto con el siguiente comando "pip install pywhatkit"
import pywhatkit as kit
import datetime

numero = "+584241997595"
mensaje = "Hola desde python :D"
horaDeEnvio = datetime.datetime.now() + datetime.timedelta(minutes=1)

kit.sendwhatmsg(numero, mensaje, horaDeEnvio.hour, horaDeEnvio.minute, wait_time=15)
#kit.sendwhatmsg(numero, mensaje, 19, 25,)