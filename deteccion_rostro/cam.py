import cv2 # Vamos a importar la biblioteca de OpenCV, vamos a utilizar para procesamiento de imagenes y video

# Vamos a cargar el clasificador de rostros de OpenCV
cascada_rostros = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Vamos a capturar el video desde la camara
video = cv2.VideoCapture(0)
# El argumento 0 indica que se utilizara la camara predeterminada del sistema

# Ahora vamos a iniciar un bucle infinito para procesar los fotogramas del video
while True:
  # Vamos a leer el siguiente frame de la camara
  ret, frame = video.read()
  # ret indica si la lectura fue exitosa, y fotograma contiene la imagen capturada.
  if not ret:
    break
  
  # Ahora vamos a convertir el fotograma a escala de grises
  # Es necesario porque el clasificador de rostros opera sobre imagenes en blanco y negro
  gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
  rostros = cascada_rostros.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5)
  # scaleFactor -> Especifica cuanto se reduce la imagen en cada escala: Vamos a colocarle un valor de 1.1
  # minNeighbors -> Especifica el numero minimo de vecinos para considerar un rostro
  
  for (x, y, w, h) in rostros:
    cv2.rectangle(frame, (x,y), (x + w, y + h), (255, 0, 0), 2)
    # El color se define del rectangulo detectado en el siguiente formato BGR
    # El ultimo argumento es el grosor del rectangulo
    
  # Vamos a mostrar el fotograma con los rostros detectados
  cv2.imshow("Detector de rostros", frame)
  
  if cv2.waitKey(1) & 0xFF == ord("x"):
    break
  
# Vamos a liberar los recursos utilizados
video.release()
# Vamos a cerrar las ventas abiertas por openCV
cv2.destroyAllWindows()