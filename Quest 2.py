'''Escreva um programa que leia uma string e use uma pilha para inverter a ordem das palavras.'''
from pilha import Pilha

def inverter(string):
    p = Pilha()
    for i in string:
        p.inserir(i)
    return p

string = input('Digite uma palavra: ')
palavra_invertida = inverter(string)

while not palavra_invertida.is_empty():
    print(palavra_invertida.remover())