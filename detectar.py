import cv2
import os
modelo = cv2.CascadeClassifier('modelo/haarcascade_frontalface_default.xml')

imagem = cv2.imread('teste/4.jpg')
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# gera uma matriz de faces detectadas

faces_detectadas = modelo.detectMultiScale(imagem_cinza)
print('Quantidades de faces detectadas : ' , len(faces_detectadas))

for (x, y, largura, altura) in faces_detectadas:
    cv2.rectangle(imagem, (x, y), (x + largura, y + altura), (255, 255, 0), 2)

cv2.imshow('faces ', imagem)
cv2.waitKey()
cv2.imshow('faces ', imagem)
cv2.waitKey()