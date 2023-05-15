'''
Escreva um programa que use uma pilha para converter um número binário para decimal.
'''
from pilha import Pilha

def bin_p_dec(valor):
    p = Pilha()
    decimal = 0
    #Convertendo o número binário para decimal
    for i in range(len(valor)):
        #(len(valor)-i-1) -> valor de exponeciação para calcular o número decimal
        decimal += int(valor[i]) * 2**(len(valor)-i-1)

    while decimal > 0:
        #Inserindo o número decimal na pilha
        p.inserir(decimal % 10)
        decimal //= 10
    return p

num_bin = input('Digite um número em binario para ser convertido em decimal: ')
num_dec = bin_p_dec(num_bin)
while not num_dec.is_empty():
    print(num_dec.remover(),end="")