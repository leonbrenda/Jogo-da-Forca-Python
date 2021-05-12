from random import randrange

def jogar():
    imprime_msg_abertura()

    palavra_secreta = carrega_palavra_secreta()
    dica = imprime_msg_dica(palavra_secreta)

    letra_acertada = introduz_letra_acertada(palavra_secreta)
    print(letra_acertada)

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 10

    while not enforcou and not acertou:
        chute = chute_do_jogador()
        if chute in palavra_secreta:
            posiciona_chute_se_correto(chute, letra_acertada, palavra_secreta)
            print(f'Você acertou a letra!')
        else:
            erros += 1
            print(f'Você errou a letra!')
            print(f'Restam {tentativas - erros} tentativas\n')
            desenha_forca(erros)

        enforcou = erros == 10
        acertou = '_' not in letra_acertada

        print(letra_acertada)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def imprime_msg_abertura():
    print(f'{" BEM VINDO AO JOGO DA FORCA ":=^70}')

def imprime_msg_dica(quantidade_letras):
    print(f'\nDica: A palavra é um animal e possui {len(quantidade_letras)} letras\n')

#responsável pela leitura do arquivo e inicialização da palavra secreta
def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    palavra_secreta = palavras[randrange(0, len(palavras))].upper()

    return palavra_secreta

#será responsável por inicializar a lista de letras acertadas
def introduz_letra_acertada(palavra):
    return ['_' for letra in palavra]

def chute_do_jogador():
    chute = str(input('\nDigite uma letra: ')).upper().replace(' ', '')[0]
    return chute

#coloca o chute do usuário na posição correta, dentro da lista
def posiciona_chute_se_correto(chute, letra_acertada, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letra_acertada[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      ( )   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 8):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    if (erros == 9):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |     o      ")
    if (erros == 10):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |     o   o  ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("\nPARABÉNS, VOCÊ GANHOU!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("\nQUE PENA, VOCÊ PERDEU!")
    print(f'A palavra era {palavra_secreta}')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if __name__ == '__main__':
    jogar()
