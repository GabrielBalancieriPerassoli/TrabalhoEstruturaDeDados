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

def center(texto):
    return texto.center(os.get_terminal_size().columns)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

cursor = 0 
selecionado = None 
running = True 
    
def seleciona():
    global selecionado, cursor
    if selecionado is None:
        if not pilhas[cursor].PilhaVazia():
            selecionado = pilhas[cursor].Desempilha()

def guarda():
    global selecionado, cursor
    if selecionado is not None:
        if not pilhas[cursor].PilhaCheia(): 
            if pilhas[cursor].PilhaVazia() or \
                pilhas[cursor].ElementoDoTopo() == selecionado:
                pilhas[cursor].Empilha(selecionado)
                selecionado = None
            else:
                print("A troca não pode ser realizada. As condições não são atendidas.")
        else:
            print("A pilha está cheia. Não é possível inserir mais elementos.")
            # Permitir devolver o elemento para a pilha de origem (OU ERA PRA PERMITIR NÃO ESTÁ FUNCIONANDO)
            pilhas[cursor].Empilha(selecionado)
            selecionado = None

def verificar_vitoria():
    pilhas_vazias = 0
    elementos_iguais = True
    
    for pilha in pilhas:
        if pilha.PilhaVazia():
            pilhas_vazias += 1 # se a pilha estiver vazia, aumenta o contador de pilhas vazias
            continue
        
        elemento_anterior = None

        for i in range(4): # verifica se todos os elementos na pilha são iguais
            elemento = pilha.Pegar(i)
            
            if elemento is None:
                continue
            
            if elemento_anterior is not None and elemento != elemento_anterior:
                elementos_iguais = False
                break
                
            elemento_anterior = elemento
        
        if not elementos_iguais:  # se algum elemento na pilha for diferente, sai do loop
            break
    
    if elementos_iguais and pilhas_vazias == 2: # verifica se todas as pilhas têm elementos iguais e se há exatamente duas pilhas vazias
        return True
    else:
        return False            
        
while running:
    clear()
    print(center("====================================\n"))
    print(center("JOGO PILHA\n"))
    print(center("====================================\n"))
    print("\n")

    linha = ''
    for i in range(len(pilhas)): #printa o numero selecionado a cima das pilhas 
        if i == cursor and selecionado != None:
            linha += f'      {selecionado}      '
        else:
            linha += '             '    
    print(center(linha)) 

    for i in range(3, -1, -1): #printa as pilhas
        linha = ''
        for pilha in pilhas:
            elem = pilha.Pegar(i) if pilha.Pegar(i) is not None else " "  # Se o elemento for None, substituímos por um espaço em branco
            linha += f" |   {elem:^3}   | "
        print(center(linha))

    linha = ''
    linha_cursor = ''
    for i in range(len(pilhas)): #printa o cursor e a base de pilha
        linha += " +---------+ "  # Base da pilha
        if i == cursor:
            linha_cursor += '      ^      '
        else:
            linha_cursor += '             '
    print(center(linha))
    print(center(linha_cursor))

    event = keyboard.read_event()
    key = event.name

    if event.event_type != 'down':
        continue

    if key.isnumeric():
        cursor = (int(key) - 1) % len(pilhas)
    elif key in ['d', 'right']:
        cursor += 1
    
        if cursor >= len(pilhas):
            cursor = 0
    elif key in ['a', 'left']:
        cursor -= 1

        if cursor < 0:
            cursor = len(pilhas)
    elif key in ['w', 'up']:
        seleciona()
    elif key in ['s', 'down']:
        guarda()

        if verificar_vitoria():
            print("Parabéns! Você ganhou!")
            running = False
    elif key in ['enter', 'space']:
        seleciona()
        guarda()
        
        if verificar_vitoria():
            print("Parabéns! Você ganhou!")
            running = False
    elif key == 'esc':
        running = False