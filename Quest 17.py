'''
Escreva um programa que use uma pilha para converter um número octal para decimal.
'''

from pilha import Pilha

def oct_dec(valor):
    p = Pilha()
    #usando o segundo parametro da função int, pode-se passar a base do número para ser convertido em decimal
    p.inserir(int(valor,8))

    return p.topo()

valor_oct = input('Digite um número em octal: ')
valor_dec = oct_dec(valor_oct)
print(valor_dec)
