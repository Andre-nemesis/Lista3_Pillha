'''
Escreva um programa que leia uma expressão matemática na forma de string 
e utilize uma pilha para calcular o resultado da expressão na notação polonesa reversa.
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
    p = Pilha()
    for caractere in valor:
        if caractere.isdigit():
            p.inserir(caractere)
        else:
            num2 = p.remover()
            num1 = p.remover()
            if caractere == '^':
                resultado = float(num1) ** float(num2)
                p.inserir(str(resultado))
            elif caractere == '/':
                resultado = float(num1) / float(num2)
                p.inserir(str(resultado))
            elif caractere == '*':
                resultado = float(num1) * float(num2)
                p.inserir(str(resultado))
            elif caractere == '-':
                resultado = float(num1) - float(num2)
                p.inserir(str(resultado))
            elif caractere == '+':
                resultado = float(num1) + float(num2)
                p.inserir(str(resultado))

    return p.remover()

expressao = str(input('Digite uma expressão matemática: '))
posf = infixa_para_posfixa(expressao)
posf_calc = calcular(posf)
print(posf_calc)