#Escreva um programa que use uma pilha para converter um número decimal para binário.

from pilha import Pilha

def calc_bin(valor):
    p = Pilha()

    while valor > 0:
        resto = valor % 2
        valor = valor // 2
        p.inserir(resto)

    return p

numero = int(input('Digite um número para transforma-lo em binario: '))

resultado_bin = calc_bin(numero)
while not resultado_bin.is_empty():
    print(resultado_bin.remover())