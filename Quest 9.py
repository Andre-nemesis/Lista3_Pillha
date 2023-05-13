'''
Escreva um programa que leia uma string contendo apenas números 
e use uma pilha para verificar se a string é um número de palíndromo
'''
from pilha import Pilha

def polindromo(numeros):
    p = Pilha()
    #string para ser implementada a cada numero da pilha
    num_inv = ""
    #verificação se o que foi colocado na stringo são só numeros
    if numeros.isnumeric():
        for numero in numeros:
            p.inserir(numero)
        while not p.is_empty():
            num_inv += p.remover()
        #verificação se os numeros invertidos obtido da pilha é igual aos números originais
        return num_inv == numeros
    else:
        return IndexError('\nExistem letras junto dos números, por isso tente novamente')
    
    
    

numeros = input("Digite uma sequência de números para ver se eles são polindromos: ")
num_poli = polindromo(numeros)
print(num_poli)