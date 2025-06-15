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

logo_image = Image.open('logo.png')
logo_image = logo_image.resize((50,50))
logo_image = ImageTk.PhotoImage(logo_image)
logo_label = ttk.Label(frameCima, image=logo_image)
logo_label.pack(side="left", padx=(10,5))

nome_label = ttk.Label(frameCima, text="Detectar Velocidade da Internet", font=("Helvetica", 18, "bold"))
nome_label.pack(side="left")

frameConteudo = ttk.Frame(janela)
frameConteudo.pack(pady=(20,20))



#função velocidade
def calcular_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download / 1000000 #Mbps
    upload_speed = st.upload() / 1000000 #Mbps

    return download_speed, upload_speed


# função inicializar o texto

def start_test():
    info_label.config(text="Testando...")
    download_speed, upload_speed = calcular_speed()

    # Atualizar as variaveis de velocidade
    speed_var["download"].set(f"{download_speed: .2f} Mbps")
    speed_var["upload"].set(f"{upload_speed: .2f} Mbps")





info_label = ttk.Label(frameConteudo, text="Pressione o botão para testar a velocidade da internet")
info_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

download_label = ttk.Label(frameConteudo, text="Velocidade de Download: ")
download_label.grid(row=1, column=0, sticky='w', pady=(0, 5))

upload_label = ttk.Label(frameConteudo, text="Velocidade de Upload: ")
upload_label.grid(row=2, column=0, sticky='w', pady=(0, 5))

speed_var = {
    'download': tk.StringVar(),
    'upload': tk.StringVar(),
}


rapido_image_local = "cheetah.png"
normal_image_local = "horse.png"
lento_image_local = "turtle.png"

rapido_imagem = Image.open(rapido_image_local)
normal_image = Image.open(normal_image_local)
lento_image = Image.open(lento_image_local)

iniciar_botão = ttk.Button(frameConteudo, text="Iniciar Teste", command= start_test)
iniciar_botão.grid(row=3, column=0, columnspan=3, pady=(20, 0))


janela.mainloop()