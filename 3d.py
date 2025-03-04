import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir el rango de valores para x e y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Crear una malla de puntos (x, y)
X, Y = np.meshgrid(x, y)

# Definir la ecuación z = f(x, y) (por ejemplo, una paraboloide)
Z = X**2 + Y**2

# Crear una figura y un objeto 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
ax.plot_surface(X, Y, Z, cmap='viridis')

# Añadir etiquetas a los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar el gráfico
plt.show()
