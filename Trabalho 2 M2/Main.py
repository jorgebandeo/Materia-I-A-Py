import numpy as np
import cv2

def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]

def gerar_mensagem(mensagem):
    lista = []
    for m in mensagem:
        val = ord(m)
        bits = bitfield(val)

        if len(bits) < 8:
            for a in range(8-len(bits)):
                bits.insert(0,0)
        lista.append(bits)
    arr = np.array(lista)
    arr = arr.flatten()
    return arr


def converter_mensagem(saida):
    # descarta os bits extras que não cabem em um byte completo
    bits = np.array(saida[:len(saida)-len(saida)%8])
    mensagem_out = ''
    bits = bits.reshape((int(len(bits)/8), 8))
    for b in bits:
        sum = 0
        for i in range(8):
            sum += b[i]*(2**(7-i))
        mensagem_out += chr(sum)
    return mensagem_out

#pre tratamento
imagem = cv2.imread("Python\Trabalho 2 M2\IMG_20220315_112141930.jpg")
with open('Python/Trabalho 2 M2/texto.txt', 'r', encoding='utf-8') as file:
    texto = file.read()
codifaier = gerar_mensagem(texto)
#------------------
#variaveis de relevancia
tamanho = len(codifaier)
#-----------------
#Linearização
matriz_R = imagem[:,:,2]#pega a imagem na escala do vermelho
vetor_linear = matriz_R.flatten()#lineraiza em um vetor a matriz vermelha
#codificação na imagem

if len(vetor_linear)/2 >= tamanho+1:# +1 quer indicar que temos um pexel de parada para verificar
    for i in range(tamanho*2):
        if (i+1)%2 == 0:#pega os numeros pares, seno seu inpar ateriar para calcular a diferença
            vetor_linear[i] = vetor_linear[i-1] + codifaier[0]
            codifaier = np.delete(codifaier, 0)
vetor_linear[(tamanho*2)+2] = vetor_linear[(tamanho*2)+1] + 2

# Converte o vetor linear de volta em uma matriz
matriz_vermelha_modificada = vetor_linear.reshape(matriz_R.shape)        
# Substitui a matriz de cor vermelha na imagem original
imagem[:, :, 2] = matriz_vermelha_modificada
#-------------------
cv2.imwrite("Python/Trabalho 2 M2/trste.jpg", imagem)

#----------- Decodificação -------------------------
veror_recal = []
imagem2 = cv2.imread("Python/Trabalho 2 M2/trste.jpg")
#Linearização
matriz_R = imagem[:,:,2]#pega a imagem na escala do vermelho
vetor_linear = matriz_R.flatten()#lineraiza em um vetor a matriz vermelha
vetor_float = vetor_linear.astype(np.float64)
for i in range(len(vetor_linear)):
    if (i+1)%2 == 0:
        valor = vetor_float[i] - vetor_float[i-1]
        if valor >= 2 :
            break
        veror_recal.append(valor)
print(converter_mensagem( np.array(veror_recal).astype(np.uint8).tolist()))

