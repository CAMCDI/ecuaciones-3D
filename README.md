# Graficador de Ecuaciones en 3D

Este es un script en Python que permite graficar ecuaciones en tres dimensiones usando `matplotlib` y `numpy`.

## 📌 Características
- Graficación de funciones matemáticas en 3D.
- Uso de `matplotlib` para renderizar la gráfica.
- No requiere interfaz gráfica (GUI).
- Personalizable: puedes modificar la función a graficar.

## 🚀 Requisitos
Antes de ejecutar el script, asegúrate de tener instaladas las siguientes bibliotecas:

```sh
pip install numpy matplotlib
```

## 📜 Uso
1. Clona este repositorio:

```sh
git clone <URL_DEL_REPO>
cd <NOMBRE_DEL_REPO>
```

2. Ejecuta el script en la terminal:

```sh
python graficador3d.py
```

3. Se abrirá una ventana mostrando la gráfica en 3D.

## ✏️ Personalización
Para cambiar la ecuación que se grafica, edita la función `f(x, y)` en `graficador3d.py`.
Ejemplo:

```python
def f(x, y):
    return np.cos(x) * np.sin(y)
```

## 🖼️ Ejemplo de Gráfica
![Ejemplo de gráfica 3D](https://matplotlib.org/stable/_images/sphx_glr_plot_3d_surface_001.png)

## 📄 Licencia
Este proyecto está bajo la licencia MIT. ¡Siéntete libre de modificar y mejorar el código! 😃

