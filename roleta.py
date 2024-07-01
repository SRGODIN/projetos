import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configurações da roleta
numeros = list(range(37))
cores = ['red' if i % 2 == 0 else 'black' for i in numeros]
cores[0] = 'green'  # Número 0 em verde

# Função para criar a roleta
def criar_roleta(ax):
    ax.clear()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')

    # Desenhando os setores da roleta
    for i, num in enumerate(numeros):
        angulo_inicial = i * (360 / 37)
        angulo_final = (i + 1) * (360 / 37)
        ax.add_patch(plt.Polygon(
            [(0, 0),
             (np.cos(np.radians(angulo_inicial)), np.sin(np.radians(angulo_inicial))),
             (np.cos(np.radians(angulo_final)), np.sin(np.radians(angulo_final)))],
            color=cores[i]
        ))
        x_text = 1.2 * np.cos(np.radians((angulo_inicial + angulo_final) / 2))
        y_text = 1.2 * np.sin(np.radians((angulo_inicial + angulo_final) / 2))
        ax.text(x_text, y_text, str(num), horizontalalignment='center', verticalalignment='center', color='white', fontsize=12, fontweight='bold')

    # Desenhando o círculo da roleta
    ax.add_patch(plt.Circle((0, 0), 1, fill=False, edgecolor='black', linewidth=2))

# Função para simular a queda da bolinha
def simular_bolinha():
    criar_roleta(ax)

    # Selecionar um número aleatório
    numero_sorteado = np.random.choice(numeros)
    angulo_bolinha = numero_sorteado * (360 / 37) + (360 / 74)  # Centralizar a bolinha no setor
    x_bolinha = 0.8 * np.cos(np.radians(angulo_bolinha))
    y_bolinha = 0.8 * np.sin(np.radians(angulo_bolinha))

    ax.add_patch(plt.Circle((x_bolinha, y_bolinha), 0.05, color='white', zorder=10))
    plt.title(f"Numero sorteado: {numero_sorteado}")

    canvas.draw()

# Função para detectar a pressão da tecla espaço
def pressionar_tecla(event):
    if event.keysym == 'space':
        simular_bolinha()

# Configurar a interface do tkinter
root = tk.Tk()
root.title("Roleta de Cassino")

fig, ax = plt.subplots(figsize=(8, 8))

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Simular a bolinha ao iniciar
simular_bolinha()

# Vincular o evento de tecla espaço
root.bind('<KeyPress>', pressionar_tecla)

root.mainloop()

