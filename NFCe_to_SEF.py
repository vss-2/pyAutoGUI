import pyautogui
import os

def resetEstado():
    pyautogui.moveTo(1915,1075)
    pyautogui.click()
    #Abre a área de trabalhom usando atalho do inferior direito (Windows 7)
    pyautogui.moveTo(520,1060)
    pyautogui.click()
    #Abre o SEF
    return

def preenche(dadoPreenchido):
    dP = str(dadoPreenchido)
    if(dP[len(dP)-1] == ','):
        dP = dP+'0'
    print(dP)
    for i in range(len(str(dP))):
        pyautogui.write(dP[i], interval=0.3)
    return

def fazNotas(path):
    leitor = open(path+'\\listaVendasRafel201912.txt', 'r+')
    texto = leitor.readlines()
    for linha in texto:
        conteudo = linha.split()
        data   = conteudo[0]
        data   = data.replace('/','')
        cupom  = conteudo[1]
        modelo = conteudo[2]
        serie  = conteudo[3]
        total  = conteudo[4]
        valor  = total.replace(',', '.')
        valor  = float(valor)
        print(data, cupom, modelo, serie, total)
        dezoitoPCT = str(round((valor*0.18), 2))
        dezoitoPCT = dezoitoPCT.replace('.', ',')
        # Minera os dados do arquivo e calcula o valor do ICMS (18%)
        
        pyautogui.moveTo(70,170)
        pyautogui.click() # Aperta no botao "Nova" do contexto Nota
        pyautogui.moveTo(180,145)
        pyautogui.click() # Aperta no Situação
        # pyautogui.write(['0', 'tab', 'tab', 'del', data, 'tab', serie, 'tab', cupom, 'tab', 'tab', 'tab', total], interval=0.5)
        pyautogui.write(['0', 'tab', 'tab', 'del'], interval=1.2)
        preenche(data)
        pyautogui.moveTo(475,235)
        pyautogui.click()
        preenche(serie)
        pyautogui.press('tab')
        preenche(cupom)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        preenche(total)
        # Preenche a primeira tela (Primeiro campo 0, depois data, o id da nota e valor de ICMS)

        pyautogui.moveTo(200,990)
        pyautogui.click()
        # Aperta na aba Novo

        # pyautogui.write(['5102', 'tab', total, 'tab', total, 'tab', '18,00', 'tab', dezoitoPCT], interval=0.3)
        pyautogui.write(['','',''], interval=0.3)
        preenche('5102')
        pyautogui.press('tab')
        preenche(total)
        pyautogui.press('tab')
        preenche(total)
        pyautogui.press('tab')
        preenche('18,00')
        pyautogui.press('tab')
        preenche(dezoitoPCT)
        pyautogui.moveTo(80,260)
        pyautogui.write(['', '', ''], interval=0.3)
        pyautogui.moveTo(80,260)
        # Preenche os dados confirma duas vezes e reinicia o laço
    return

if __name__ == "__main__":
    resetEstado()
    path = os.getcwd()
    fazNotas(path)
    exit
