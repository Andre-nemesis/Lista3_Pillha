'''
Escreva um programa que use uma pilha para converter um número decimal para hexadecimal.
'''
from pilha import Pilha

def calc_hex(valor):
    p = Pilha()

    while valor > 0:
        #calculo padrão para encontrar o número em hexadecimal
        resto = valor % 16

        if resto == 10:
            p.inserir('A')
        elif resto == 11:
            p.inserir('B')
        elif resto == 12:
            p.inserir('C')
        elif resto == 13:
            p.inserir('D')
        elif resto == 14:
            p.inserir('E')
        elif resto == 15:
            p.inserir('F')
        #calcular proximo numero    
        valor = valor // 16

        #caso padrão
        if resto < 10:    
            p.inserir(resto)

    return p

valor = int(input('Digite um valor para ser convertido para hexadecimal: '))
valor_hex = calc_hex(valor)
while not valor_hex.is_empty():
    print(valor_hex.remover())