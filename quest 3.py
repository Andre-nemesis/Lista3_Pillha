'''
Escreva um programa que leia uma string contendo números e operações matemáticas (+, -, *, /) 
e use uma pilha para calcular o resultado da expressão.
'''

from pilha import Pilha
def infixa_para_posfixa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    posfixa = []
    numeros = '0123456789'
    for caracter in expressao:
        if caracter in numeros:
            posfixa.append(caracter)
        elif caracter == '(':
            operadores.inserir(caracter)
        elif caracter == ')':
            while operadores.topo() != '(':
                posfixa.append(operadores.remover())
            operadores.remover()
        elif caracter in precedencia:
            while not operadores.is_empty()  \
                and operadores.topo() != '(' \
                and precedencia[caracter] <= precedencia[operadores.topo()]:
                posfixa.append(operadores.remover())
            operadores.inserir(caracter)
    while not operadores.is_empty():
        posfixa.append(operadores.remover())
    return ''.join(posfixa)

def calcular(valor):
    p_op = Pilha()
    p_num = Pilha()
    for caractere in valor:
        if caractere.isdigit():
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
res = infixa_para_posfixa(numero)
calc_res = calcular(res)
print(calc_res)