'''
Escreva um programa que use uma pilha para verificar se uma expressão aritmética é válida. 
A expressão é válida se para cada parêntese aberto houver um parêntese fechado correspondente e,
para cada operação matemática, houver dois operandos
'''
from pilha import Pilha

def valida_expressao(expressao):
    parent = Pilha()
    num = Pilha()
    for let in expressao:
        if let.isdigit():
            num.inserir(let)
        elif let == '(':
            parent.inserir(let)
        elif let == ')' and parent.topo() == '(':
            parent.inserir(let)
    teste = parent.remover()
    teste2 = parent.remover()
    if teste == ')' and teste2 == '(':
        return True
    else:
        return False

infix = input('Digite uma espressão que contenha dois operadores entre os parênteses: ')
pos = valida_expressao(infix)
print(pos)