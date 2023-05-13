'''
Escreva um programa que leia uma string contendo números e 
use uma pilha para converter a string em um número decimal.
'''
from pilha import Pilha

def string_p_int (string):
    p = Pilha()
    for c in string:
        if c.isnumeric():
            p.inserir(int(c))
    return p

string = str(input('Digite um número ou uma sequência de números: '))
num_int = string_p_int(string)
while not num_int.is_empty():
    print(num_int.remover() ,end=" ")