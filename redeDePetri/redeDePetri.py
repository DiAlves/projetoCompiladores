import cv2
import numpy as np
import random as rd

# Verificar se ja existe um lugar no espaco randomizado
def verificaPosicaoLugar(nX, nY, preenchido):
    cond = True
    
    # Verifica x
    for i in range(0, len(preenchido), 2):
        aux = preenchido[i][0]
        for j in range(aux, aux+60):
            if(nX == j):
                cond = False
    # Verifica y
    for i in range(1, len(preenchido), 2):
        aux = preenchido[i][0]
        for j in range(aux, aux+60):
            if(nY == j):
                cond = False
    return cond

# Verificar se ja existe um evento no espaco randomizado
def verificaPosicaoEvento(nX, nY, preenchido):
    cond = True
    
    # Verifica x
    for i in range(0, len(preenchido), 2):
        aux = preenchido[i][0]
        for j in range(aux, aux+60):
            if(nX == j):
                cond = False
    # Verifica y
    for i in range(1, len(preenchido), 2):
        aux = preenchido[i][0]
        for j in range(aux, aux+44):
            if(nY == j):
                cond = False
    return cond

# Colar o lugar na imagem
def colarLugar(atual, img, preenchido):
    
    lugar = cv2.imread("Formas/lugar.png", 0)
    auxCoordenadas = []
    
    #Criar o lugar
    caminho = "Formas/" + atual + ".png"
    l = cv2.imread(caminho, 0)
    aux = lugar
    aux[10:49, 16:42] = l
    
    #Sorteia um lugar na imagem para colar o lugar 
    
    while(True):
        nX = rd.randint(0, 940)
        nY = rd.randint(0, 940)
        posicaoValidaL = verificaPosicaoLugar(nX, nY, preenchido)
        posicaoValidaE = verificaPosicaoEvento(nX, nY, preenchido)
        
        
        if(posicaoValidaL == True and posicaoValidaE == True):
            auxCoordenadas = [nX, nY+29, nX+29, nY+59, nX+59, nY+29, nX+29, nY]
            posicaoX = [nX, nX+60]
            posicaoY = [nY, nY+60]
            preenchido.append(posicaoX)
            preenchido.append(posicaoY)
            img[posicaoX[0]:posicaoX[1], posicaoY[0]:posicaoY[1]] = aux
            break
    
    return img, preenchido, auxCoordenadas

# Colar o evento na imagem
def colarEvento(atual, img, preenchido):
    
    evento = cv2.imread("Formas/evento.png", 0)
    auxCoordenadas = []
    
    #Criar o Evento
    caminho = "Formas/" + atual + ".png"
    l = cv2.imread(caminho, 0)
    aux = evento
    aux[10:53, 10:36] = l
    
    #Sorteia um lugar na imagem para colar o lugar
    while(True):
        nX = rd.randint(0, 940)
        nY = rd.randint(0, 940)
        posicaoValidaE = verificaPosicaoEvento(nX, nY, preenchido)
        posicaoValidaL = verificaPosicaoLugar(nX, nY, preenchido)
        
        if(posicaoValidaE == True and posicaoValidaL == True):
            auxCoordenadas = [nX, nY+21, nX+29, nY+43, nX+59, nY+21, nX+29, nY]
            posicaoX = [nX, nX+60]
            posicaoY = [nY, nY+44]
            preenchido.append(posicaoX)
            preenchido.append(posicaoY)
            img[posicaoX[0]:posicaoX[1], posicaoY[0]:posicaoY[1]] = aux
            break

    return img, preenchido, auxCoordenadas

# Criar e colar na imagem os lugares e transicoes 
def criarLugarEvento(rede):
 
    img = np.ones((1000, 1000), 'uint8')
    img = img*255
    
    preenchido = []
    auxLugaresEvento = []
    coordenadas = {}
    
    for i in range (len(rede)):
        atual = rede[i]
        
        if(len(atual) == 7):
            
            if(atual[0] not in auxLugaresEvento):
                
                #Adiciona na lista de lugares e eventos feitos
                auxLugaresEvento.append(atual[0])
                
                #Chama a funcao de colar o lugar
                img, preenchido, coordenadasAux = colarLugar(atual[0], img, preenchido)
                
                # Adicionar no dicionario as coordenadas
                coordenadas[atual[0]] = coordenadasAux 
                
            if(atual[3] not in auxLugaresEvento):
                
                #Adiciona na lista de lugares e eventos feitos
                auxLugaresEvento.append(atual[3])
                
                #Chamar a funcao de colar o Evento
                img, preenchido, coordenadasAux = colarEvento(atual[3], img, preenchido)

                #Adicionar no dicionario as coordenadas
                coordenadas[atual[3]] = coordenadasAux 

            if(atual[6] not in auxLugaresEvento):
                
                #Adiciona na lista de lugares e eventos feitos
                auxLugaresEvento.append(atual[6])
                
                #Chama a funcao de colar o lugar
                img, preenchido, coordenadasAux = colarLugar(atual[6], img, preenchido)
                
                #Adicionar no dicionario as coordenadas
                coordenadas[atual[6]] = coordenadasAux 
                    
        if(len(atual) == 4):
            
            # Saber se eh lugar -> evento ou evento -> lugar
            v = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
            
            if(ord(atual[0]) in v):
                
                if(atual[0] not in auxLugaresEvento):
                        
                    #Adiciona na lista de lugares e eventos feitos
                    auxLugaresEvento.append(atual[0])
                    
                    #Chamar a funcao de colar o Evento
                    img, preenchido, coordenadasAux = colarEvento(atual[0], img, preenchido)

                    #Adicionar no dicionario as coordenadas
                    coordenadas[atual[0]] = coordenadasAux 
                    
                    
                if(atual[3] not in auxLugaresEvento):
                
                    #Adiciona na lista de lugares e eventos feitos
                    auxLugaresEvento.append(atual[3])
                    
                    #Chama a funcao de colar o lugar
                    img, preenchido, coordenadasAux = colarLugar(atual[3], img, preenchido)
                
                    # Adicionar no dicionario as coordenadas
                    coordenadas[atual[3]] = coordenadasAux 
           
            else:
                if(atual[0] not in auxLugaresEvento):
                    
                    #Adiciona na lista de lugares e eventos feitos
                    auxLugaresEvento.append(atual[0])
                    
                    #Chama a funcao de colar o lugar
                    img, preenchido, coordenadasAux = colarLugar(atual[0], img, preenchido)
                    
                    #Adicionar no dicionario as coordenadas
                    coordenadas[atual[0]] = coordenadasAux 
                        
                
                if(atual[3] not in auxLugaresEvento):
                    #Adiciona na lista de lugares e eventos feitos
                    auxLugaresEvento.append(atual[3])
                    
                    #Chamar a funcao de colar o Evento
                    img, preenchido, coordenadasAux = colarEvento(atual[3], img, preenchido)
                    
                    #Adicionar no dicionario as coordenadas
                    coordenadas[atual[3]] = coordenadasAux 
                                    
    return img, coordenadas, preenchido

# Calcular a ditancia entre pontos
def distanciaPonto(i, j):
    return ((i[0] - j[0])**2 + (i[1] - j[1])**2)**0.5

def encontrarPontoProximo(p1, p2):
    y, x = p1
    pontos = [(y-1,x-1), (y-1, x), (y-1, x+1), 
              (y, x-1), p1, (y, x+1),
              (y+1, x-1), (y+1, x),(y+1, x+1)]

    nextP = p1
    distanciaMinima = float('inf')
    for p in pontos:
        current_distance = distanciaPonto(p, p2)
        if current_distance < distanciaMinima:
            distanciaMinima = current_distance
            nextP = p

    return nextP

def desenharLinhas(point_list, image):
    
    p1, p2 = point_list
    img = np.array(image)
    pontosExplorados = []

    while(True):
        ponto_temp = encontrarPontoProximo(p1, p2)
        img[ponto_temp[0], ponto_temp[1]] = 0
        p1 = ponto_temp
        pontosExplorados.append(p1)
        if (ponto_temp[0] == p2[0]) and (ponto_temp[1] == p2[1]):
            return img, pontosExplorados

def desenharTriangulo(explorados, img):
    ultima = explorados[-1]
    penultima = explorados[-2]
    
    r = (ultima[0] - penultima[0], ultima[1] - penultima[1])
    
    if(r == (-1, 1)):
        img[ultima[0]+1, ultima[1]] = 0
        img[ultima[0]+2, ultima[1]] = 0
        img[ultima[0]+3, ultima[1]] = 0
        img[ultima[0]+4, ultima[1]] = 0
        img[ultima[0]+5, ultima[1]] = 0
        img[ultima[0]+6, ultima[1]] = 0
        img[ultima[0]+7, ultima[1]] = 0
        img[ultima[0]+8, ultima[1]] = 0
        img[ultima[0]+9, ultima[1]] = 0
        img[ultima[0]+10, ultima[1]] = 0
        img[ultima[0], ultima[1]-1] = 0
        img[ultima[0], ultima[1]-2] = 0
        img[ultima[0], ultima[1]-3] = 0
        img[ultima[0], ultima[1]-4] = 0
        img[ultima[0], ultima[1]-5] = 0
        img[ultima[0], ultima[1]-6] = 0
        img[ultima[0], ultima[1]-7] = 0
        img[ultima[0], ultima[1]-8] = 0
        img[ultima[0], ultima[1]-9] = 0
        img[ultima[0], ultima[1]-10] = 0
        img, e = desenharLinhas([[ultima[0]+10, ultima[1]], [ultima[0], ultima[1]-10]], img)
        
    if(r == (-1, 0)):
        img[ultima[0]+1, ultima[1]+1] = 0
        img[ultima[0]+2, ultima[1]+2] = 0
        img[ultima[0]+3, ultima[1]+3] = 0
        img[ultima[0]+4, ultima[1]+4] = 0
        img[ultima[0]+5, ultima[1]+5] = 0
        img[ultima[0]+6, ultima[1]+6] = 0
        img[ultima[0]+7, ultima[1]+7] = 0
        img[ultima[0]+8, ultima[1]+8] = 0
        img[ultima[0]+9, ultima[1]+9] = 0
        img[ultima[0]+10, ultima[1]+10] = 0
        img[ultima[0]+1, ultima[1]-1] = 0
        img[ultima[0]+2, ultima[1]-2] = 0
        img[ultima[0]+3, ultima[1]-3] = 0
        img[ultima[0]+4, ultima[1]-4] = 0
        img[ultima[0]+5, ultima[1]-5] = 0
        img[ultima[0]+6, ultima[1]-6] = 0
        img[ultima[0]+7, ultima[1]-7] = 0
        img[ultima[0]+8, ultima[1]-8] = 0
        img[ultima[0]+9, ultima[1]-9] = 0
        img[ultima[0]+10, ultima[1]-10] = 0
        img, e = desenharLinhas([[ultima[0]+10, ultima[1]+10], [ultima[0]+10, ultima[1]-10]], img)


    if(r == (-1, -1)):
        img[ultima[0], ultima[1]+1] = 0
        img[ultima[0], ultima[1]+2] = 0
        img[ultima[0], ultima[1]+3] = 0
        img[ultima[0], ultima[1]+4] = 0
        img[ultima[0], ultima[1]+5] = 0
        img[ultima[0], ultima[1]+6] = 0
        img[ultima[0], ultima[1]+7] = 0
        img[ultima[0], ultima[1]+8] = 0
        img[ultima[0], ultima[1]+9] = 0
        img[ultima[0], ultima[1]+10] = 0
        img[ultima[0]+1, ultima[1]] = 0
        img[ultima[0]+2, ultima[1]] = 0
        img[ultima[0]+3, ultima[1]] = 0
        img[ultima[0]+4, ultima[1]] = 0
        img[ultima[0]+5, ultima[1]] = 0
        img[ultima[0]+6, ultima[1]] = 0
        img[ultima[0]+7, ultima[1]] = 0
        img[ultima[0]+8, ultima[1]] = 0
        img[ultima[0]+9, ultima[1]] = 0
        img[ultima[0]+10, ultima[1]] = 0
        img, e = desenharLinhas([[ultima[0], ultima[1]+10], [ultima[0]+10, ultima[1]]], img)
        
    if(r == (0, -1)):
        img[ultima[0]-1, ultima[1]+1] = 0
        img[ultima[0]-2, ultima[1]+2] = 0
        img[ultima[0]-3, ultima[1]+3] = 0
        img[ultima[0]-4, ultima[1]+4] = 0
        img[ultima[0]-5, ultima[1]+5] = 0
        img[ultima[0]-6, ultima[1]+6] = 0
        img[ultima[0]-7, ultima[1]+7] = 0
        img[ultima[0]-8, ultima[1]+8] = 0
        img[ultima[0]-9, ultima[1]+9] = 0
        img[ultima[0]-10, ultima[1]+10] = 0
        img[ultima[0]+1, ultima[1]+1] = 0
        img[ultima[0]+2, ultima[1]+2] = 0
        img[ultima[0]+3, ultima[1]+3] = 0
        img[ultima[0]+4, ultima[1]+4] = 0
        img[ultima[0]+5, ultima[1]+5] = 0
        img[ultima[0]+6, ultima[1]+6] = 0
        img[ultima[0]+7, ultima[1]+7] = 0
        img[ultima[0]+8, ultima[1]+8] = 0
        img[ultima[0]+9, ultima[1]+9] = 0
        img[ultima[0]+10, ultima[1]+10] = 0
        img, e = desenharLinhas([[ultima[0]-10, ultima[1]+10], [ultima[0]+10, ultima[1]+10]], img)
        
    if(r == (1, -1)):
        img[ultima[0]-1, ultima[1]] = 0
        img[ultima[0]-2, ultima[1]] = 0
        img[ultima[0]-3, ultima[1]] = 0
        img[ultima[0]-4, ultima[1]] = 0
        img[ultima[0]-5, ultima[1]] = 0
        img[ultima[0]-6, ultima[1]] = 0
        img[ultima[0]-7, ultima[1]] = 0
        img[ultima[0]-8, ultima[1]] = 0
        img[ultima[0]-9, ultima[1]] = 0
        img[ultima[0]-10, ultima[1]] = 0
        img[ultima[0], ultima[1]+1] = 0
        img[ultima[0], ultima[1]+2] = 0
        img[ultima[0], ultima[1]+3] = 0
        img[ultima[0], ultima[1]+4] = 0
        img[ultima[0], ultima[1]+5] = 0
        img[ultima[0], ultima[1]+6] = 0
        img[ultima[0], ultima[1]+7] = 0
        img[ultima[0], ultima[1]+8] = 0
        img[ultima[0], ultima[1]+9] = 0
        img[ultima[0], ultima[1]+10] = 0
        img, e = desenharLinhas([[ultima[0]-10, ultima[1]], [ultima[0], ultima[1]+10]], img)

    if(r == (1, 0)):
        img[ultima[0]-1, ultima[1]-1] = 0
        img[ultima[0]-2, ultima[1]-2] = 0
        img[ultima[0]-3, ultima[1]-3] = 0
        img[ultima[0]-4, ultima[1]-4] = 0
        img[ultima[0]-5, ultima[1]-5] = 0
        img[ultima[0]-6, ultima[1]-6] = 0
        img[ultima[0]-7, ultima[1]-7] = 0
        img[ultima[0]-8, ultima[1]-8] = 0
        img[ultima[0]-9, ultima[1]-9] = 0
        img[ultima[0]-10, ultima[1]-10] = 0
        img[ultima[0]-1, ultima[1]+1] = 0
        img[ultima[0]-2, ultima[1]+2] = 0
        img[ultima[0]-3, ultima[1]+3] = 0
        img[ultima[0]-4, ultima[1]+4] = 0
        img[ultima[0]-5, ultima[1]+5] = 0
        img[ultima[0]-6, ultima[1]+6] = 0
        img[ultima[0]-7, ultima[1]+7] = 0
        img[ultima[0]-8, ultima[1]+8] = 0
        img[ultima[0]-9, ultima[1]+9] = 0
        img[ultima[0]-10, ultima[1]+10] = 0
        img, e = desenharLinhas([[ultima[0]-10, ultima[1]-10], [ultima[0]-10, ultima[1]+10]], img)

    if(r == (1, 1)):
        img[ultima[0]-1, ultima[1]] = 0
        img[ultima[0]-2, ultima[1]] = 0
        img[ultima[0]-3, ultima[1]] = 0
        img[ultima[0]-4, ultima[1]] = 0
        img[ultima[0]-5, ultima[1]] = 0
        img[ultima[0]-6, ultima[1]] = 0
        img[ultima[0]-7, ultima[1]] = 0
        img[ultima[0]-8, ultima[1]] = 0
        img[ultima[0]-9, ultima[1]] = 0
        img[ultima[0]-10, ultima[1]] = 0
        img[ultima[0], ultima[1]-1] = 0
        img[ultima[0], ultima[1]-2] = 0
        img[ultima[0], ultima[1]-3] = 0
        img[ultima[0], ultima[1]-4] = 0
        img[ultima[0], ultima[1]-5] = 0
        img[ultima[0], ultima[1]-6] = 0
        img[ultima[0], ultima[1]-7] = 0
        img[ultima[0], ultima[1]-8] = 0
        img[ultima[0], ultima[1]-9] = 0
        img[ultima[0], ultima[1]-10] = 0
        img, e = desenharLinhas([[ultima[0]-10, ultima[1]], [ultima[0], ultima[1]-10]], img)

    if(r == (0, 1)):
        img[ultima[0]-1, ultima[1]-1] = 0
        img[ultima[0]-2, ultima[1]-2] = 0
        img[ultima[0]-3, ultima[1]-3] = 0
        img[ultima[0]-4, ultima[1]-4] = 0
        img[ultima[0]-5, ultima[1]-5] = 0
        img[ultima[0]-6, ultima[1]-6] = 0
        img[ultima[0]-7, ultima[1]-7] = 0
        img[ultima[0]-8, ultima[1]-8] = 0
        img[ultima[0]-9, ultima[1]-9] = 0
        img[ultima[0]-10, ultima[1]-10] = 0
        img[ultima[0]+1, ultima[1]-1] = 0
        img[ultima[0]+2, ultima[1]-2] = 0
        img[ultima[0]+3, ultima[1]-3] = 0
        img[ultima[0]+4, ultima[1]-4] = 0
        img[ultima[0]+5, ultima[1]-5] = 0
        img[ultima[0]+6, ultima[1]-6] = 0
        img[ultima[0]+7, ultima[1]-7] = 0
        img[ultima[0]+8, ultima[1]-8] = 0
        img[ultima[0]+9, ultima[1]-9] = 0
        img[ultima[0]+10, ultima[1]-10] = 0
        img, e = desenharLinhas([[ultima[0]-10, ultima[1]-10], [ultima[0]+10, ultima[1]-10]], img)
        
    return img

# Ligar lugares e transicoes
def ligar(img, coordenadas, rede):
    menorD = 1000
    melhorCoordenada = []
    pL1 = []
    pE = []
    pL2 = []
    
    for i in range (len(rede)):
        atual = rede[i]
        menorD = 1000
        
        if(len(atual) == 7):

            l1 = coordenadas[atual[0]]
            e = coordenadas[atual[3]]
            l2 = coordenadas[atual[6]]
            
            # Calcula a menor distancia 
            for i in range (0, len(l1), 2):
                pL1.append(l1[i])
                pL1.append(l1[i+1])
                
                for j in range (0, len(e), 2):
                    pE.append(e[j])
                    pE.append(e[j+1])
                    d = distanciaPonto(pL1, pE)
                    if(d < menorD):
                        melhorCoordenada = []
                        melhorCoordenada.append(pL1)
                        melhorCoordenada.append(pE)
                        menorD = d
                    pE = []
                pL1 = []
                
            menorD = 1000
            # liga os ponto melhorCoordenada[0] e [1]
            #print(melhorCoordenada)
            img, explorados = desenharLinhas(melhorCoordenada, img)
            img = desenharTriangulo(explorados, img)
            
            # Calcula a menor distancia 
            for x in range (0, len(e), 2):
                pE.append(e[x])
                pE.append(e[x+1])
                
                for y in range (0, len(l2), 2):
                    pL2.append(l2[y])
                    pL2.append(l2[y+1])
                    d = distanciaPonto(pE, pL2)
                    if(d < menorD):
                        melhorCoordenada = []
                        melhorCoordenada.append(pE)
                        melhorCoordenada.append(pL2)
                        menorD = d
                    pL2 = []
                pE = []
    
            # liga os ponto melhorCoordenada[0] e [1]
            #print(melhorCoordenada)
            img, explorados = desenharLinhas(melhorCoordenada, img)
            img = desenharTriangulo(explorados, img)
            
        if(len(atual) == 4):
            menorD = 1000
            l1 = coordenadas[atual[0]]
            l2 = coordenadas[atual[3]]
            
            # Calcula a menor distancia 
            for m in range (0, len(l1), 2):
                pL1.append(l1[m])
                pL1.append(l1[m+1])
                
                for l in range (0, len(l2), 2):
                    pL2.append(l2[l])
                    pL2.append(l2[l+1])
                    d = distanciaPonto(pL1, pL2)
                    if(d < menorD):
                        melhorCoordenada = []
                        melhorCoordenada.append(pL1)
                        melhorCoordenada.append(pL2)
                        menorD = d
                    pL2 = []
                pL1 = []
            #print(melhorCoordenada)
            img, explorados = desenharLinhas(melhorCoordenada, img)
            img = desenharTriangulo(explorados, img)
            
    return img, melhorCoordenada, explorados

exp = open('exp.txt', 'r')
exp = exp.read()
exp = exp.split()

img, coordenadas, preenchido = criarLugarEvento(exp)
img, melhorCoordenada, explorados = ligar(img, coordenadas, exp)

#plotar imagem
cv2.imshow("imagem", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#salvar imagem
salvar = "Resultados/imgResult.png"
cv2.imwrite(salvar, img)
