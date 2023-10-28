import pygame
from random import choice
banco_de_palavras = ['pedra', 'arroz', 'sorvete', 'minecraft', 'feijão', 'terra', 'suco']
tent = 3
letras_descobertas = []
letras_usadas = []
palavra = choice(banco_de_palavras).upper()
palavra_secreta = list(palavra)
quant_de_letras = len(palavra_secreta)
cores = {'limpa': '\033[m',
         'cinza': '\033[0;30m',
         'azul': '\033[1;31m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'roxo': '\033[0;35m'}


def vitoria():
    while True:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("musicas/winneris.wav")
        pygame.mixer.music.play()
        pygame.event.wait()
        visual()
        print(' \n' * 2)
        print(f'{cores["cinza"]}-=-{cores["limpa"]}' * 5, f'{cores["verde"]}VOCÊ GANHOU!{cores["limpa"]}',
              f'{cores["cinza"]}-=-{cores["limpa"]}' * 5)
        print(f'{cores["roxo"]}Palavra secreta:{cores["limpa"]} {palavra_secreta}')
        print(' \n' * 6)


def derrota():
    while True:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("musicas/game_over_bad_chest.wav")
        pygame.mixer.music.play()
        pygame.event.wait()
        visual()
        print(f'{cores["cinza"]}-=-{cores["limpa"]}' * 5+f'{cores["vermelho"]}VOCÊ PERDEU!{cores["limpa"]}'+
              f'{cores["cinza"]}-=-{cores["limpa"]}' * 5)
        print(f'{cores["roxo"]}Palavra secreta:{cores["limpa"]} {palavra_secreta}')
        print(' \n' * 8)


def visual():
    print(
        f'{cores["cinza"]}-=-{cores["limpa"]}' * 5 + f'{cores["vermelho"]}JOGO DA FORCA{cores["limpa"]}' + f'{cores["cinza"]}-=-{cores["limpa"]}' * 5)
    print(f'\033[1;97mVocê só tem\033[m {cores["azul"]}{tent}{cores["limpa"]} \033[1;97mtentativas!\033[m')
    for x in range(0, quant_de_letras):
        print(f'{cores["roxo"]}{letras_descobertas[x]}{cores["limpa"]}')


for i in range(0, quant_de_letras):
    letras_descobertas.append('-')
print('\033[0;33mSeja Bem-Vindo ao Jogo da Forca! Vamos ver se você consegue adivinhar a palavra certa...\033[m')
while True:
    visual()
    letra = input('Digite uma letra: ').upper()
    if letra in palavra_secreta:
        for i in range(0, quant_de_letras):
            if letra == palavra_secreta[i]:
                letras_descobertas[i] = letra
        letras_usadas.append(letra)
        if letras_usadas.count(letra) > 1:
            tent = tent - 1
    else:
        tent = tent - 1
    if tent == 0:
        visual()
        derrota()
        break
    if letras_descobertas == palavra_secreta:
        vitoria()
        break
