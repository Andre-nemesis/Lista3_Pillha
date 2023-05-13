'''
Escreva um programa que use uma pilha para verificar se uma string é um palíndromo 
(ou seja, se é igual quando lida de trás para frente).
'''
from pilha import Pilha

def polindromo(palavra):
    p = Pilha()
    #string para ser implementada a cada caractere da pilha
    palavra_inv = ""
    for letra in palavra:
        p.inserir(letra)
    while not p.is_empty():
        palavra_inv += p.remover()
    #verificação se a plavra invertida obtida da pilha é igual á palara original
    return palavra_inv == palavra


palavra = input('Digite uma palavra: ')
poli = polindromo(palavra)
print(poli)
