'''
Escreva um programa que use uma pilha para converter um número binário para octal.
'''
from pilha import Pilha

def bin_oct(valor):
    p = Pilha()
    #Variavel para armazenar o número decimal
    decimal = 0
    #Convertendo o número binário para decimal
    for i in range(len(valor)):
        #(len(valor)-i-1) -> valor de exponeciação para calcular o número decimal
        decimal += int(valor[i]) * 2**(len(valor)-i-1)

    while decimal > 0:
        #Inserindo o número octal na pilha
        p.inserir(decimal % 8)
        decimal //= 8

    return p
    

valor_bin = input('Digite um número em binario para converte-lo em octal: ')
valor_oct = bin_oct(valor_bin)
while not valor_oct.is_empty():
    print(valor_oct.remover(),end="")