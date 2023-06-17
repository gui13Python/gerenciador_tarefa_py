
# importa as bibliotecas que são utilizadas
import datetime
import time
import os 
import pyautogui
import pyttsx3
import win32gui, win32con #### bilioteca para console 



def tarefa_pronta():
    # Inicializa o mecanismo de fala
    engine = pyttsx3.init()
    # Define o texto a ser falado
    texto = "Tarefa adicionada com Sucesso!"
    # Faz o mecanismo de fala pronunciar o texto
    engine.say(texto)
    # Aguarda a finalização da fala
    engine.runAndWait()



def exe():
    #guarda o caminho do seu arquivo para execusão
    arq = pyautogui.prompt(text='digite o caminho do seu arquivo a ser execultado \n Exemplo: \n C:\\Users\\seuUSUARIO\\Desktop\\arquivo.exe', title='agendador de tarefa' , default='')
    # guarda a hora que foi determinada 
    alarme = pyautogui.prompt(text='Digite a hora que o progama vai ser execultado \n Exmplo: \n 18:00', title='AGENDADOR DE TAREFA' , default='')
    # espera um segundo 
    time.sleep(1)
    # chama a função que fala que a tarefa foi agendada 
    tarefa_pronta()
    # roda o progama ate que a hora seja igual a selecionada 
    while True:
        # Obtém a hora atual
        hora_atual = datetime.datetime.now()
        # Formata a hora no formato HH:MM:SS
        hora_formatada = hora_atual.strftime("%H:%M")
        # Exibe a hora formatada e mostra no terminal  
        print("A hora atual é:", hora_formatada)
        #oculta o terminal 
        hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hide , win32con.SW_HIDE)  ### esconde telinha preta(CMD) CONSOLE 
        # recebe a hora que foi selecionada
        hora = alarme
        # verifica se a hora do pc é igual a hora selecionada
        if hora_formatada == hora:
        # abre o progama selecionado pelo (CMD)
            destino = os.system(arq)
            # Para o progama depois que execulta a tarefa
            break


exe()