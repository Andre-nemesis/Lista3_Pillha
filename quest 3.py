'''
Escreva um programa que leia uma string contendo números e operações matemáticas (+, -, *, /) 
e use uma pilha para calcular o resultado da expressão.
'''

from pilha import Pilha

def calcular(valor):
    p_op = Pilha()
    p_num = Pilha()
    for caractere in valor:
        if caractere.isnumeric():
            p_num.inserir(int(caractere))
        #quardando as operações
        elif caractere in '+-*/' :
            p_op.inserir(caractere)
    
    while not p_op.is_empty():
        op = p_op.remover()
        num2 = p_num.remover()
        num1 = p_num.remover()
        if op == '+':
            resultado = num1 + num2
            p_num.inserir(resultado)
        elif op == '-':
            resultado = num2 - num1
            p_num.inserir(resultado)
        if op == '*':
            resultado = num1 * num2
            p_num.inserir(resultado)
        if op == '/':
            resultado = num1 / num2
            p_num.inserir(resultado)

    return p_num.topo()

numero = input('Digite uma expressão matematica: ')
res = calcular(numero)
print(res)