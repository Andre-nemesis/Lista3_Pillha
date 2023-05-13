'''
Escreva um programa que leia uma string contendo caracteres (, ), {, }, [ e ], 
e use uma pilha para verificar se os caracteres estão balanceados.
'''
from pilha import Pilha

def validacao(valor):
    p = Pilha()

    if valor[0] == '(':
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
    if valor[0] == '[':
        for op in valor:
            if op == '[':
                p.inserir(op)
            elif op == ']':
                p.inserir(op)
            if not p.is_empty():
                if p.topo() == ']':
                    return True
            else:
                return False
            
    if valor[0] == '{':
        for op in valor:
            if op == '{':
                p.inserir(op)
            elif op == '}':
                p.inserir(op)
            if not p.is_empty():
                if p.topo() == '}':
                    return True
            else:
                return False

palavra = input('digite uma palavra ou frase entre () ou [] , ou {}: ')
palavra_vali = validacao(palavra)
print(palavra_vali)