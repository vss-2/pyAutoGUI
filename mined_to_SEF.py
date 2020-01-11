import os
from os import listdir
from os.path import isfile, join

## Esse aqui bota no SEF dados minerados anteriormente (NFCout_to_SEF.py)

def dirAtual():
    soArquivos = [arq for arq in listdir(os.getcwd()) if isfile(join(os.getcwd(), arq))]
    soArquivos = list(filter(lambda x:x.endswith('.txt'), soArquivos))
    return soArquivos

def preenche(dadoPreenchido):
    dP = str(dadoPreenchido)
    if(dP[len(dP)-1] == ','):
        dP = dP+'0'
    print(dP)
    for i in range(len(str(dP))):
        pyautogui.write(dP[i], interval=0.3)
    return

def automatizado(serie, nfcid, nome, ender, bairr, cep, cidad, estad, cnpfj, valbt, val18, data):
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
    preenche(nfcid)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    preenche(valbt)
    # Preenche a primeira tela (Primeiro campo 0, depois data, o id da nota e valor de ICMS)

    pyautogui.moveTo(200,990)
    pyautogui.click()
    # Aperta na aba Novo

    # pyautogui.write(['5102', 'tab', total, 'tab', total, 'tab', '18,00', 'tab', dezoitoPCT], interval=0.3)
    pyautogui.write(['','',''], interval=0.3)
    preenche('5102')
    pyautogui.press('tab')
    preenche(valbt)
    pyautogui.press('tab')
    preenche(valbt)
    pyautogui.press('tab')
    preenche('18,00')
    pyautogui.press('tab')
    preenche(val18)
    print(nome, cnpfj, cidad, estad)
    exit
    # Preenche os dados confirma duas vezes e reinicia o laço
    return

def preencherSEF(arqPath, arq):
    linhas = open(arqPath[len(arqPath)-9:len(arqPath)])
    texto = linhas.readlines()
    for dado in texto:
        serie = dado[0]
        serie = serie[len(serie)-9:len(serie)-4]
        nfcid = dado[1]
        nome  = dado[2]
        ender = dado[3]
        bairr = dado[4]
        cep   = dado[5]
        cidad = dado[6]
        estad = dado[7]
        cnpfj = dado[8]
        valbt = dado[9]
        val18 = dado[10]
        data  = dado[11]
        automatizado(serie, nfcid, nome, ender, bairr, cep, cidad, estad, cnpfj, valbt, val18, data)
        # call(['rm', arq])
        call(['del', arq], shell=True)
    return

if __name__ == "__main__":
    arquivos = dirAtual()
    print(arquivos)
    for arq in arquivos:
        # preencherSEF(str(os.getcwd()+'/'+arq), arq)
        preencherSEF(str(os.getcwd()+'\\'+arq))
    exit
