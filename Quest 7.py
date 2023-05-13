'''
Escreva um programa que use uma pilha para converter um número decimal para octal.
'''
from pilha import Pilha

def calc_octal(valor):
    p = Pilha()
    #dividindo por 8 para gerar o número em octal
    while valor > 0:
        resto = valor % 8
        #número sendo atualizado após a divisão
        valor = valor // 8
        p.inserir(resto)

    return p

valor = int(input('Digite um valor para transforma-lo em octal: '))
valor_oct = calc_octal(valor)
while not valor_oct.is_empty():
    print(valor_oct.remover())