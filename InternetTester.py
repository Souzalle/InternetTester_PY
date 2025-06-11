import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import speedtest

# cores
letras = "#FFFFFF"
fundo = "#233642"

janela = tk.Tk()
janela.title("Detectar Velocidade da internet")
janela.geometry("450x300")
janela.resizable(False, False)
janela.configure(background=fundo)

#Estilo para a Janela
style = ttk.Style()
style.configure("TFrame", background=fundo)
style.configure("TLabel", background = fundo, foreground=letras, front=("Helvetica", 10))

frameCima = ttk.Frame(janela)
frameCima.pack(pady=(20,50))

janela.mainloop()