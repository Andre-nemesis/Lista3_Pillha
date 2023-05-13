'''
Escreva um programa que use uma pilha para converter um número binário para decimal.
'''
from pilha import Pilha

def bin_p_dec(valor):
    p = Pilha()
    
    

num_bin = int(input('Digite um número em binario para ser convertido em decimal: '))
num_dec = bin_p_dec(num_bin)
print(num_dec)