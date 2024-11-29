# Importar credenciales
from credenciales import user_email, user_email_password

# Vamos a importar las librerias necesarias
from email.message import EmailMessage # Para crear el contenido del email
import smtplib # Esto es para conectarnos al servidor SMTP y enviar emails
import ssl # Para crear un contexto de SSL seguro

def envio_email(email_recibir, nombre):
  # Vamos a configurar el correo del remitente (El que correo que enviara el email)
  email_sender = user_email # Direccion de correo del remitente
  email_password = user_email_password # Contrasena de aplicacion del Correo Gmail
  email_receiver = email_recibir # Direccion de correo del destinatario
  
  # Vamos hacer la configuracion del asunto y del cuerpo del correo
  subject = "Esto es una prueba con python" # Asunto del correo
  body = f"Hola {nombre}" # Esto es el contenido o cuerpo del correo
  
  # Vamos a crear el mensaje de email con los datos de configuracion
  em = EmailMessage()
  em["From"] = email_sender # Direccion del remitente
  em["To"] = email_receiver # Direccion del destinatario
  em["Subject"] = subject # Asunto del correo
  em.set_content(body) # Contenido o cuerpo del correo
  
  # Vamos a crear el contexto SSL para la conexion segura
  context = ssl.create_default_context() # Configuracion del contexto SSL seguro
  
  # Vamos a conectar el servidor SMTP de Gmail utilizando SSL
  with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password) # Iniciar sesion en el correo remitente.
    smtp.sendmail(email_sender, email_receiver, em.as_string()) # Enviamos el correo
    
# Vamos a llamar a la funcion enviar correo
envio_email("", "Rosibel")
lista_correos = ["hola@gmail.com","pepe@gmail.com"]

for correo in lista_correos :
  envio_email(correo, correo.split("@")[0])