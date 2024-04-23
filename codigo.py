# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
#   https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui, time, pandas

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar 1 tecla doMOLO000251     teclado

# abrir o navegador (edge)
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.click(x=360, y=50)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(1)

# Passo 2: Fazer login
pyautogui.click(x=655, y=390)
pyautogui.write("vitorbittencourtoliveira@PowerUp.com.br")
pyautogui.press("tab")
pyautogui.write("Vitor@12345")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

# Passo 3: Importar a base de dados
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=650, y=275)
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(8001)

# Passo 5: Repetir o processo de cadastro até acabar

