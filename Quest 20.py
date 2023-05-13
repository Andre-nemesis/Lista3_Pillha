'''
Escreva um programa que use uma pilha para converter um número binário para hexadecimal.
'''
from pilha import Pilha

def bin_hex(valor):
    p = Pilha()
    dec = 0
    for i in range(len(valor)):
        #(len(valor)-i-1) -> valor de exponeciação para calcular o número decimal
        dec += int(valor[i]) * 2**(len(valor)-i-1)

    while dec > 0:
        resto = dec % 16
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
        #Inserindo o número octal na pilha
        else:
            p.inserir(resto)
        dec //= 16

    return p.topo()

valor_bin = input('Digite um valor em binário para converte-lo em hexadecimal: ')
valor_hex = bin_hex(valor_bin)
print(valor_hex)