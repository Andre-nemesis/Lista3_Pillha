'''
Escreva um programa que leia uma string contendo números 
e use uma pilha para converter a string em um número binário.
'''
from pilha import Pilha

def num_bin(valor):
    p = Pilha()
    #transformando o valor str para int e calculando seu número binario
    while int(valor) > 0:
        resto = int(valor) % 2
        valor = int(valor) // 2
        p.inserir(resto)

    return p

num = input('Digite um número: ')
numbin = num_bin(num)
while not numbin.is_empty():
    print(numbin.remover())