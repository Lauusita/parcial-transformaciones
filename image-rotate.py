import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button
import numpy as np
import cv2

imagen = cv2.imread("./assets/mono.jpeg")
imagen_actual = imagen.copy()

offset_x = 0
offset_y = 0

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

axboxRotar = plt.axes([0.2, 0.05, 0.6, 0.05])    
text_boxRotar = TextBox(axboxRotar, 'Rotar | Ángulo:', initial="0")

ax_boton_derecha = plt.axes([0.7, 0.12, 0.2, 0.075])
buttonDerecha = Button(ax_boton_derecha, "Derecha ➡️")

ax_boton_izquierda = plt.axes([0.1, 0.12, 0.2, 0.075])
buttonIzquierda = Button(ax_boton_izquierda, "⬅️ Izquierda")

ax_boton_arriba = plt.axes([0.5, 0.12, 0.2, 0.075])
buttonArriba = Button(ax_boton_arriba, "Arriba ⬆️")

ax_boton_abajo = plt.axes([0.3, 0.12, 0.2, 0.075])
buttonAbajo = Button(ax_boton_abajo, "⬇️ Abajo")

def mostrar_casa(ax):
  ax.clear()
  h, w = imagen_actual.shape[:2]
  
  extent = [
    -w + offset_x, w + offset_x,
    -h + offset_y, h+ offset_y
  ]
  ax.imshow(
    cv2.cvtColor(imagen_actual, cv2.COLOR_BGR2RGB),
    extent=extent
  )
  ax.set_aspect('equal', 'box')
  ax.set_xlim(-500, 500)
  ax.set_ylim(-500, 500)
  ax.set_title('Casa (5 puntos)')
  ax.grid(True)

def rotar_manual(imagen, angulo):
  theta = np.radians(angulo)
  cos_theta = np.cos(theta)
  sin_theta = np.sin(theta)

  h, w = imagen.shape[:2]
  cx, cy = w // 2, h // 2

  salida = np.zeros_like(imagen)

  for y in range(h):
    for x in range(w):
      x_rel = x - cx
      y_rel = y - cy

      # Rotación inversa
      x_ori =  cos_theta * x_rel + sin_theta * y_rel + cx
      y_ori = -sin_theta * x_rel + cos_theta * y_rel + cy

      x_ori = int(round(x_ori))
      y_ori = int(round(y_ori))

      if 0 <= x_ori < w and 0 <= y_ori < h:
        salida[y, x] = imagen[y_ori, x_ori]

  return salida

def teclaDerecha(event):
    global offset_x
    offset_x += 50
    mostrar_casa(ax)
    plt.draw()

def teclaIzquierda(event):
    global offset_x
    offset_x -= 50
    mostrar_casa(ax)
    plt.draw()

def teclaArriba(event):
    global offset_y
    offset_y += 50
    mostrar_casa(ax)
    plt.draw()

def teclaAbajo(event):
    global offset_y
    offset_y -= 50
    mostrar_casa(ax)
    plt.draw()

def aplicar_rotacion(theta):
  global imagen_actual
  try:
    angulo = float(theta)
    imagen_actual = rotar_manual(imagen, angulo)
    mostrar_casa(ax)
    plt.draw()
  except ValueError:
    print("Por favor ingresa un número válido.")

mostrar_casa(ax)

buttonDerecha.on_clicked(teclaDerecha)
buttonIzquierda.on_clicked(teclaIzquierda)
buttonAbajo.on_clicked(teclaAbajo)
buttonArriba.on_clicked(teclaArriba)
text_boxRotar.on_submit(aplicar_rotacion)
plt.show()