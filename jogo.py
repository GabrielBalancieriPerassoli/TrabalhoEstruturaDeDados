from Pilha import Pilha
import random

question = int(input("Quantos números diferentes serão distribuídos entre as pilhas? Escolha de 1 a 7: "))

if question < 1 or question > 7:
    print("Por favor, escolha um número entre 1 e 7.")
else:
    num_pilhas = (question + 2) + 1
    pilhas = {f"p{i}": Pilha(3) for i in range(1, num_pilhas)}

    available_numbers = list(range(1, question + 1)) * 4 

    for p in pilhas.values(): 
        random.shuffle(available_numbers)  
        for i in range(4):
            if available_numbers:
                num = available_numbers.pop()  
                p.Empilha(num)

print("====================================")
print("             JOGO PILHA             ")
print("====================================\n")
print("               AÇÕES                \n")
print("1 - REMOVER ELEMENTO EM UMA PILHA PARA COLOCAR EM OUTRO")
print("2 - VER PILHAS")
print("3 - SAIR\n")

question = None

while question != 3:

    print("====================================")
    print("            JOGO DO COPO            ")
    print("====================================\n")
    print("               AÇÕES                \n")
    print("1 - REMOVER ELEMENTO EM UMA PILHA PARA COLOCAR EM OUTRO")
    print("2 - VER PILHAS")
    print("3 - SAIR\n")
    question = int(input("Qual dessas opções você escolhe? "));

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

    elif question == 2:
        print("\n")
        print("Pilhas:")
        for chave, valor in pilhas.items():
            print("\n")
            print(f"Pilha {chave}:")
            print("\n")
            for i in range(3, -1, -1):
                if i <= valor.topo:
                    elem = valor.elem[i] if valor.elem[i] is not None else " "  # Se o elemento for None, substituímos por um espaço em branco
                    print(f"|   {elem:^3}   |")
                else:
                    print(f"|{' ':^9}|")
            print("+---------+")  # Base da pilha

    else:
        question = 3