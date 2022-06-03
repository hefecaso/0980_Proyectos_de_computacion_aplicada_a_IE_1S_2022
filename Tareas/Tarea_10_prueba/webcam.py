import cv2

'''
Usaremos el fichero de pre-entrenamiento disponible en:
https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
'''

haar_file = 'haarcascade_frontalface_default.xml'

#Cargamos el fichero en OpenCV
face_cascade = cv2.CascadeClassifier(haar_file)

#Llamamos a nuestro capturador, el cero es la webcam predeterminada
webcam = cv2.VideoCapture(0)

#Iniciamos un ciclo para mantener abierta la cámara
while True:
    #Cargamos la imágen
    (_, im) = webcam.read()
    #Agregamos escala de grises para que reconozca el clasificador
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #Determinamos la escala, puede ser una o varias
    faces = face_cascade.detectMultiScale(gray)

    #Pintamos las caras que se lograron reconocer
    for (x, y, w, h) in faces:
        #Pintamos el rectángulo y definimos parámetros de tamaño
        #Azul = (255,0,0) y colocamos 2 pixeles
        cv2.rectangle(im, (x,y), (x+w, y+h), (255, 0, 0), 2)

    #Mostramos en pantalla
    cv2.imshow('OpenCV', im)

    #Si presionamos esc, se detiene
    key = cv2.waitKey(10)
    if key == 27:
        break
