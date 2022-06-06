import cv2
import numpy as np


#Se leen las imagenes
img = cv2.imread('IMG.jpg')
img1 = cv2.imread('IMG.jpg')
img2 = cv2.imread('IMG.jpg')
h,w=img.shape[:2]


#recorrer la matriz
for i in range (0,h):
	for j in range (0,w):
		#Elimina componentes rojo y verde
		img [i][j][1]=0
		img [i][j][2]=0
		
#recorrer la matriz
for i in range (0,h):
	for j in range (0,w):
		#Elimina componentes rojo y azul
		img1 [i][j][0]=0
		img1 [i][j][2]=0

#recorrer la matriz
for i in range (0,h):
	for j in range (0,w):
		#Elimina componentes verde y azul
		img2 [i][j][0]=0
		img2 [i][j][1]=0


C = img + img2 +img1 + 2 
cv2.imshow('C',C)

#Muestra la IMG en color Azul
cv2.imshow('imgColorBlue',img)

#Muestra la IMG en color Verde
cv2.imshow('imgColorGreen',img1)

#Muestra la IMG en color Rojo
cv2.imshow('imgColorRed',img2)



cv2.waitKey(0)
cv2.destroyAllWindows()
