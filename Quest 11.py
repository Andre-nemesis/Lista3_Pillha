'''
Escreva um programa que use uma pilha para ordenar uma lista de inteiros em ordem crescente.
'''
from pilha import Pilha

def ordernar(valor):
    p = Pilha()
    ord = []
    for i in valor:
        ord.append(i)
    #ordenando a lista para passar para a pilha
    ord.sort(reverse=True)
    for i in ord:
        p.inserir(i)
    return p

lista = []
num = int(input('Digite a quantidade de numeros que você quer inserir: '))
for i in range(num):
    lista.append(int(input(f'Digite o {i + 1}° número: ')))
valor_ord = ordernar(lista)
while not valor_ord.is_empty():
    #end para imprimir todos os valores em uma única linha
    print(valor_ord.remover() ,end=" ")