from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import cm 

zfile = pd.read_csv("dados_Res.txt", header=None)
z = np.array(zfile.values.flatten())

x,y = np.meshgrid(np.linspace(-1,1,201), np.linspace(-1,1,201))


fig = plt.figure(figsize=[15,12])
ax = fig.gca(projection='3d')


ax.set_xlabel('Eixo x', fontsize=13)
ax.set_ylabel('Eixo y', fontsize=13)
ax.set_zlabel('Eixo z', fontsize=13)

arr_2d = np.reshape(z, (201, 201))

surf = ax.plot_surface(x,y,arr_2d, cmap=cm.coolwarm)
ax.set_title('Grafico de Resultado da Funcao Multimodal')
fig.colorbar(surf, ax = ax, shrink = 0.5, aspect =5)

plt.show()