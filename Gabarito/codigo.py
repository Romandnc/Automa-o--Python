
#link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#primeiramente veja o passo a passo do trabalho a ser feito 

import pyautogui
import time
pyautogui.PAUSE = 0.5 #tempo de espera entre a execusão de um comando entre outro 

#abrir o navegador
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

#entrar no sistema 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=682, y=462)
pyautogui.write("treinamento@gmail.com")

pyautogui.press("tab") #passa pro poximo campo
pyautogui.write("treinamento123")

pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

#importando arquivos extrernos, interessante para quem trabalha com dados
import pandas 
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])

    #cadastrando produtos 
    pyautogui.click(x=647, y=326)
    pyautogui.write(codigo)

    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

#tratamento da observação
    obs=str(tabela.loc[linha, "obs"])
    if obs != "nan":
         pyautogui.write(obs)
   
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll (5000)


#pyautogui.click ->clicar com mouse
#pyautogui.write->escrever um texto
#pyautogui.press -> pressionar uma tecla do teclado 
#pyautogui.hotkey("ctrl","t")