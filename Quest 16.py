'''
Escreva um programa que use uma pilha para converter um número hexadecimal para decimal.
'''
from pilha import Pilha

def hex_dec(valor):
    p = Pilha()
    #usando o segundo parametro da função int, pode-se passar a base do número para ser convertido em decimal
    p.inserir(int(valor,16))

    return p.topo()

valor_hex = input('Digite um número em hexadecimal: ')
valor_dec = hex_dec(valor_hex)
print(valor_dec)
