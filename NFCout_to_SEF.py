import os
from os import listdir
from os.path import isfile, join
from subprocess import call
import pyautogui

## Minera dados e joga em arquivos .txt para serem usados posteriormente (mined_to_SEF.py)

def dirAtual():
    soArquivos = [arq for arq in listdir(os.getcwd()) if isfile(join(os.getcwd(), arq))]
    soArquivos = filter(lambda x:x.endswith('.pdf'), soArquivos)
    return soArquivos

def minerarDados(localArquivo):
    localArquivotxt = localArquivo[0:len(localArquivo)-3]
    localArquivotxt = localArquivotxt+'txt'
    
    leitor = open(localArquivotxt, 'r', errors='ignore')
    texto  = leitor.readlines()
    contador = 0
    sobrescrever = True
    chaveAcesso, nome, endereco, bairro, cidade, cep, cpfj, uf, data, fone, valorNota = '','','','','','','','','','',''
    for linha in texto:
        if(  linha == 'CHAVE DE ACESSO\n' and sobrescrever):
            chaveAcesso = texto[contador+2]
        elif(linha == 'NOME/RAZÃO SOCIAL\n' and sobrescrever):
            nome = texto[contador+1]
        elif(linha == 'ENDEREÇO\n' and sobrescrever):
            if (len(endereco) == 0):
                endereco = texto[contador+1]
        elif(linha == 'BAIRRO/DISTRITO\n' and sobrescrever):
            bairro = texto[contador+1]
        elif(linha == 'CEP\n' and sobrescrever):
            cep = texto[contador+1]
        elif(linha == 'CNPJ/CPF\n' and sobrescrever):
            cpfj = texto[contador+1]
        elif(linha == 'MUNICÍPIO\n' and sobrescrever):
            cidade = texto[contador+1]
        elif(linha == 'UF\n' and sobrescrever):
            uf = texto[contador+1]
        elif(linha == 'FONE/FAX:\n' and sobrescrever):
            fone = texto[contador+1]
        elif(linha == 'VALOR TOTAL DA NOTA\n' and sobrescrever):
            valorNota = texto[contador+1]
            if(len(valorNota) == 1):
                valorNota = texto[contador+6]
        elif(linha.startswith('DAT')):
            data   = texto[contador+1]
        elif(linha == 'FRETE POR CONTA\n' and sobrescrever):
            sobrescrever = False
            break
        contador = contador + 1
    leitor.close()
    escritor = open(localArquivotxt, 'w')

    vNponto = str(valorNota).replace('.','')

    vNponto = str(valorNota).replace(',','.')

    if(vNponto[1] == '.'):
        vNponto = str(vNponto[0])+str(vNponto[2:len(vNponto)])
    if(vNponto[2] == '.'):
        vNponto = str(vNponto[0])+str(vNponto[1])+str(vNponto[3:len(vNponto)])
    vNponto = float(vNponto)
    dezoitoPCT = str(round((vNponto*0.18), 2))
    
    virgula = str(dezoitoPCT)
    if(virgula[len(virgula)-2] == '.'):
        virgula = virgula+'0'
    
    chaveAcesso = chaveAcesso.replace(' ','')
    virgula = virgula[0:len(virgula)-3]+','+virgula[len(virgula)-2:len(virgula)]
    info = [str(chaveAcesso), nome, endereco, bairro, str(cep), cidade, uf, str(cpfj), str(fone), str(valorNota), str(virgula), '\n', data]
    #                0         1       2        3         4       5      6     7          8         9
    escritor.write("Série: "+localArquivotxt[len(localArquivotxt)-8: len(localArquivotxt)]+'\n')
    for i in info:
        # print(str(i))
        escritor.write(str(i))
    escritor.close()

    return info

def impressao(dados):
    print(dados[0]+'\n'+dados[1]+' '+dados[2]+' '+ dados[3]+' '+dados[6]+' '+dados[4]+' '+dados[10]+'\n'+dados[7]+'\n'+dados[8]+' '+dados[9]+'\n')
    return

def cadastrarNota(localArquivo, arqAtual):
    arqAtualtxt = arqAtual[0:len(arqAtual)-3]
    arqAtualtxt = arqAtualtxt+'txt'
    call(['pdf2txt.py', '-o', arqAtualtxt, arqAtual])
    dados = minerarDados(localArquivo)
    # impressao(dados)
    return
    
if __name__ == '__main__':
    arquivos = dirAtual()
    for atual in arquivos:
        ## call(['touch', atual+'.txt'])
		## print('Série:', atual[0:len(atual)-3])
        cadastrarNota(os.getcwd()+'/'+atual, atual)
        ## call(['del', atual+'.pdf'])
    exit

