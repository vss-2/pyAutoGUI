import mss
import cv2
import numpy
import pyautogui
from time import sleep
from subprocess import Popen
from collections import defaultdict

MONITOR = 1
ARQUIVOS = {
    'loading': '',
    'login':   '',
    'ingame':  '',
    'colher':  ''
}

if not all([len(l) for l in ARQUIVOS.values()]):
    print('Favor preencher todos os arquivos de imagem no arquivo \'pageWatchet.py\' a serem comparados!')
    exit()

def getGamePosition() -> None:
    x, y = input().split(' ')
    x2, y2 = input().split(' ')
    Popen(['touch', 'gameposition.txt'])
    Popen(['echo', '\'{} {} {} {}\''.format(x, y, x2, y2), '>', 'gameposition.txt'])
    return

def main() -> None:

    # Captura a tela e manda para o opencv
    with mss.mss() as screen:
        positions = [0,0,0,0]
        try:
            with open('./gameposition.txt', 'r') as arq:
                positions = [int(a) for a in arq.readline().strip().split()]
        except FileNotFoundError:
            print('gameposition.txt não encontrado, tente executar getGamePosition()')
            exit()
        tela = screen.grab({
                            'left': positions[0]+screen.monitors[MONITOR]['left'], 
                            'top': positions[1]+screen.monitors[MONITOR]['left'], 
                            'width': positions[2]-positions[0], 
                            'height': positions[3]-positions[1]
                        })
        cv2.imshow('Tela', numpy.array(tela))
        
        # Remove canal alfa
        tela2 = tela[:,:,:3]

        scores = defaultdict()
        for a in list(ARQUIVOS.keys()):
            scores[a] = cv2.matchTemplate(tela2, ARQUIVOS[a], cv2.TM_CCOEFF_NORMED)

        resultado = ('', 0)
        for s in scores:
            if scores[s] > resultado[1]:
                resultado = (s, scores[s])
        
        if resultado[0] != 'loading':
            Popen(['notify-send', '{} com precisão de {}'.format(resultado[0].capitalize(), resultado[1])])

    return

main()
