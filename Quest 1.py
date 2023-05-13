'''
Escreva um programa que leia uma expressão matemática na forma de string 
e utilize uma pilha para verificar se os parênteses estão balanceados.
'''
from pilha import Pilha
def validacao(valor):
    p = Pilha()

    for op in valor:
        if op == '(':
            p.inserir(op)
        elif op == ')':
            p.inserir(op)
        if not p.is_empty():
            if p.topo() == ')':
                return True
        else:
            return False


expMat = input('Digite uma expressão matemática dentro de parenteses(): ')
if validacao(expMat):
    print('A expressão foi escrita corretamente')
else:
    print('A expressão não foi escrita corretamente')
