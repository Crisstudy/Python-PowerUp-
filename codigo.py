# pyautogui .click -> clica
# pyautogui .write -> escreve um texto
# pyautogui .press -> pressiona uma tecla
# pyautogui .hotkey -> aperta um atalho

import pyautogui
import time
import pandas

pyautogui.PAUSE = 2.0
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo a passo do meu programa (lógica da programação)
# pip install pyautogui
# Passo 1 : entrar no Sistema da empresa 
# # Abrir o navegador
# (Ajuste os números 100, 100 se necessário para clicar fora da janela)
pyautogui.click(100, 10)

pyautogui.hotkey("command", "space") 
time.sleep(2) # Essencial para o Mac processar a abertura
pyautogui.write("google")
pyautogui.press("enter")

pyautogui.write(link)
time.sleep(2)
pyautogui.press("enter")

# Fazer uma pausa maior para o site carregar
time.sleep(3)

# Passo 2 : Fazer login
#clicar no campo de email
pyautogui.click(x=457, y=408)
pyautogui.write("cristinafigueiredosaraiva@gmail.com")
pyautogui.press("tab") # Passar para o proximo campo
pyautogui.write("sua senha dificilíma")
pyautogui.press("tab") #passar para o botão
pyautogui.press("enter")
# Fazer uma pausa maior para o site carregar
time.sleep(3)


# Passo 3 : Abrir a base de dados (importar o arquivo)
# pip install pandas openpyxl


table = pandas.read_csv("produtos.csv")
# Passo 4 : Cadastrar um produto

for line in table.index:
    pyautogui.click(x=450, y=296) # Clicar no campo do codigo

    codigo = str(table.loc[line, "codigo"])

    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    marca = str(table.loc[line, "marca"])

    pyautogui.write(marca)
    pyautogui.press("tab")

    # Tipo
    tipo = str(table.loc[line, "tipo"])

    pyautogui.write(tipo)
    pyautogui.press("tab")

    # Categoria
    categoria = str(table.loc[line, "categoria"])

    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Preço
    preco = str(table.loc[line, "preco_unitario"])

    pyautogui.write(preco)
    pyautogui.press("tab")

    # Custo
    custo = str(table.loc[line, "custo"])

    pyautogui.write(custo)
    pyautogui.press("tab")

    # Obs
    obs = str(table.loc[line, "obs"])

    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter") # clicou no enviar

    # Voltar para o inicio da tela 
    pyautogui.scroll(5000)

# Passo 5 : Repetir o passo 4 até acabar a lista de produtos 







