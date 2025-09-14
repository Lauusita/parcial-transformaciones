import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button
import numpy as np
import cv2

imagen_1 = cv2.imread("./assets/mono.jpeg")
imagen_2 = cv2.imread("./assets/bayas.jpeg")

compararImg1 = cv2.imread("./assets/compare1.png")
compararImg2 = cv2.imread("./assets/compare2.png")

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

def mostrar(ax, imagen):
  ax.clear()
  ax.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
  ax.set_aspect('equal', 'box')

def sumaImagenes(imagen_1, imagen_2, alpha=0.4):
  if alpha > 1:
    print("Los pesos deben estar entre 0 y 1")
    return
  
  filas, cols, canales = imagen_1.shape
  salida = np.zeros_like(imagen_1, dtype=np.uint8)

  imagen_2 = cv2.resize(imagen_2, (cols, filas))

  for i in range(filas):
    for j in range(cols):
      for c in range(3):
        salida[i, j, c] = int(
          alpha * imagen_1[i, j, c] + (1 - alpha) * imagen_2[i, j, c]
        )

  mostrar(ax, salida)
  plt.show()

def restaImagenes(imagen_1, imagen_2):
  gray_imagen_1 = cv2.cvtColor(imagen_1, cv2.COLOR_BGR2GRAY)
  gray_imagen_2 = cv2.cvtColor(imagen_2, cv2.COLOR_BGR2GRAY)

  filas, cols = gray_imagen_1.shape

  gray_imagen_2 = cv2.resize(gray_imagen_2, (cols, filas))

  imgResta = np.zeros((filas, cols), dtype=np.uint8)

  for i in range(filas):
    for j in range(cols):
      valoresimagen_1 = int(gray_imagen_1[i, j])
      valoresimagen_2 = int(gray_imagen_2[i, j])
      valor = valoresimagen_1 - valoresimagen_2
      if valor < 0:
        valor = 0
      imgResta[i, j] = valor

  mostrar(ax, imgResta)
  plt.show()

def imagenAlCuadrado(imagen):
  gray_imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
  filas, cols = gray_imagen.shape

  imgCuadrado = np.zeros((filas, cols), dtype=np.float32)

  I_min = 255**2 
  I_max = 0

  for i in range(filas):
    for j in range(cols):
      valor = int(gray_imagen[i, j]) ** 2
      imgCuadrado[i][j] = valor
      if valor < I_min:
        I_min = valor
      if valor > I_max:
        I_max = valor

  I_min = np.min(imgCuadrado)
  I_max = np.max(imgCuadrado)

  imgNorm = (imgCuadrado - I_min) / (I_max - I_min) * 255
  imgNorm = imgNorm.astype(np.uint8)

  mostrar(ax, imgNorm)
  cv2.imshow("Original", gray_imagen)
  plt.show()

def imagenRaizCuadrada(imagen):
  filas, cols, cn = imagen.shape

  imgRaiz = np.zeros((filas, cols, cn), dtype=np.uint8)

  I_min = 255
  I_max = 0

  for i in range(filas):
    for j in range(cols):
      for c in range(cn): 
        valor = int(np.sqrt(imagen[i, j, c]))
        imgRaiz[i, j, c] = valor
        if valor < I_min:
          I_min = valor
        if valor > I_max:
          I_max = valor

  I_min = np.min(imgRaiz)
  I_max = np.max(imgRaiz)

  imgNorm = (imgRaiz - I_min) / (I_max - I_min) * 255
  imgNorm = imgNorm.astype(np.uint8)

  mostrar(ax, imgNorm)
  cv2.imshow("Original", imagen)
  plt.show()

def imagenRaizCubica(imagen):
  filas, cols, cn = imagen.shape

  imgRaiz = np.zeros((filas, cols, cn), dtype=np.uint8)

  I_min = 255
  I_max = 0

  for i in range(filas):
    for j in range(cols):
      for c in range(cn): 
        valor = int(np.cbrt(imagen[i, j, c]))
        imgRaiz[i, j, c] = valor
        if valor < I_min:
          I_min = valor
        if valor > I_max:
          I_max = valor

  I_min = np.min(imgRaiz)
  I_max = np.max(imgRaiz)

  imgNorm = (imgRaiz - I_min) / (I_max - I_min) * 255
  imgNorm = imgNorm.astype(np.uint8)

  mostrar(ax, imgNorm)
  cv2.imshow("Original", imagen)
  plt.show()


# Gráficas
def mostrarGrafica(ax, x, y, lim):
  if 0 <= lim <= 255:
    y_clip = np.clip(y, 0, 255)
    ax.plot(x, y_clip, color="red")

  ax.set_xlim(0, 255)
  ax.set_ylim(0, 255)
  ax.set_aspect('equal', 'box')
  ax.grid(True)
  plt.show()

def identidad():
  x = np.linspace(0, 255, 100)
  y = x
  ax.plot(x, y)
  mostrarGrafica(ax, x, y, 255)
  plt.show()

def suma(escalar):
  x = np.linspace(0, 255, 100)
  y = x + escalar

  ax.plot(x, y)

  y_top = 255
  x_top = y_top - escalar

  mostrarGrafica(ax, x, y, x_top)

def resta(escalar):
  x = np.linspace(0, 255, 100)
  y = x - escalar

  ax.plot(x, y)

  y_bottom = 0
  x_bottom = y_bottom + escalar

  mostrarGrafica(ax, x, y, x_bottom)

def multiplicarPor2():
  x = np.linspace(0, 255, 100)
  y = 2 * x

  ax.plot(x, y)

  y_top = 255
  x_top = y_top / 2

  mostrarGrafica(ax, x, y, x_top)
  plt.show()

def dividirPor2():
  x = np.linspace(0, 255, 100)
  y = x / 2
  ax.plot(x, y)

  mostrarGrafica(ax, x, y, 255)
  plt.show()
  
def multiplicarPor3():
  x = np.linspace(0, 255, 100)
  y = 3* x

  ax.plot(x, y)

  y_top = 255
  x_top = y_top / 3

  mostrarGrafica(ax, x, y, x_top)
  plt.show()

# sumaImagenes(imagen_1, imagen_2, alpha=0.6)
# imagenAlCuadrado(imagen_1)
# imagenRaizCuadrada(imagen_1)
# imagenRaizCubica(imagen_1)

# identidad()
# suma(64)
# resta(64)
# multiplicarPor2()
# dividirPor2()
# multiplicarPor3()
