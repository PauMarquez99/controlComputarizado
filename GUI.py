import tkinter as tk

window = tk.Tk()

tk.label(window, text="Simulador de Planta").grid(row=0, column=2)

tk.label(window, text="Planta").grid(row=1, column=0, columnspan=5, sticky="ew")