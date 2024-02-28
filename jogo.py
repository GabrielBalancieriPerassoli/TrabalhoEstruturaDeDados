from Pilha import Pilha
import random
import os
import keyboard
import time

question = int(input("Quantos números diferentes serão distribuídos entre as pilhas? Escolha de 1 a 7: "))

if question < 1 or question > 7:
    print("Por favor, escolha um número entre 1 e 7.")
else:
    num_pilhas = (question + 2) + 1
    pilhas = [Pilha(3) for i in range(1, num_pilhas)]

    available_numbers = list(range(1, question + 1)) * 4 

    for p in pilhas: 
        random.shuffle(available_numbers)  
        for i in range(4):
            if available_numbers:
                num = available_numbers.pop()  
                p.Empilha(num)


question = None


def center(texto):
    return texto.center(os.get_terminal_size().columns)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

cursor = 0 
    
def frame(cursor):
    
    clear()
    print(center("====================================\n"))
    print(center("JOGO PILHA\n"))
    print(center("====================================\n"))
    print("\n")

    for i in range(3, -1, -1):
        linha = ''
        for pilha in pilhas:
            elem = pilha.elem[i] if pilha.elem[i] is not None else " "  # Se o elemento for None, substituímos por um espaço em branco
            linha += f" |   {elem:^3}   | "
        print(center(linha))

    linha = ''
    linha_cursor = ''
    for i in range(len(pilhas)):
        linha += " +---------+ "  # Base da pilha
        if i == cursor:
            linha_cursor += '      ^      '
        else:
            linha_cursor += '             '
    print(center(linha))
    print(center(linha_cursor))

    key = keyboard.read_key()

    if key == 'd':
        cursor += 1

        if cursor >= len(pilhas):
            cursor = 0

    if key == 'a':
        cursor -= 1

    frame(cursor)

    if question == 1:

        pilha_remover = input(f"De qual pilha você quer remover um elemento? p1 a p{num_pilhas}: ")

        if pilha_remover in pilhas and not pilhas[pilha_remover].PilhaVazia():

            pilha_inserir = input(f"Em qual pilha você quer inserir o elemento removido? p1 a p{num_pilhas}: ")

            if pilha_inserir in pilhas and not pilhas[pilha_inserir].PilhaCheia():

                if pilhas[pilha_inserir].PilhaVazia():

                    x = pilhas[pilha_remover].ElementoDoTopo()
                    pilhas[pilha_remover].Desempilha()

                    pilhas[pilha_inserir].Empilha(x)
                    print(f"Elemento {x} inserido na pilha {pilha_inserir}.")

                elif pilhas[pilha_remover].ElementoDoTopo() == pilhas[pilha_inserir].ElementoDoTopo():

                    x = pilhas[pilha_remover].ElementoDoTopo()
                    pilhas[pilha_remover].Desempilha()

                    pilhas[pilha_inserir].Empilha(x)
                    print(f"Elemento {x} inserido na pilha {pilha_inserir}.")

                else:
                    print(f"Elemento do Topo da Pilha de Origem não é o mesmo da Destino.")
            else:
                print(f"A pilha {pilha_inserir} está cheia. Não é possível inserir mais elementos.")         
        else:
            print("A pilha selecionada não existe ou está vazia.")
frame(cursor)
