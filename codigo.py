#Passo 1: Abrir o sistema da empresa   

import pyautogui
import time
import pandas
import keyboard
import sys
pyautogui.PAUSE = 0.3

#pyautogui.click  -> clicar
#pyautogui.press  -> pressionar uma tecla
#pyautogui.write  -> escrever
#pyautogui.hotkey -> atalho de teclado (ctrol,c)
#Passo 2: Fazer login

# apertar a  tecla win
pyautogui.press("win")
# digitar o texto chrome
pyautogui.write("chrome")
time.sleep(0.6)
# apertar a  tecla enter
pyautogui.press("enter")
time.sleep(0.5)
#entrar no link
pyautogui.click(x=1403, y=134)
pyautogui.click(x=789, y=667)
#pedir pro computador esperar 5 segundos
time.sleep(0.5)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#Passo 2: fazer login
time.sleep(0.5)
pyautogui.click (x=688, y=407)
pyautogui.write("emaildesconhecido@gmail.com")
pyautogui.press("tab")
pyautogui.write("elysiumltda@gmail.com")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.click(x=705, y=292)
#Passo 3:Importar a base de dados dos produtosp

tabela = pandas.read_csv("produtos.csv")
print(tabela)


#Passo 4 Cadastrar 1 produto

for linha in tabela.index:
    #para cancelar o script utilizando f2
    if keyboard.is_pressed("f2"):
        print("F2 detectado! Script cancelado.")
        sys.exit(0)
    pyautogui.click(x=705, y=292)

    #codigo do produto
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    #marca do produto
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    
    #tipo do produto
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    #categoria 
    categoria = tabela.loc[linha,"categoria" ]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    #preço unitario
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    #custo
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    #obs
    
    
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter") #botao de enviar
    pyautogui.scroll(10000)

#Repetir o passo 4 até acabar todos os produtos

