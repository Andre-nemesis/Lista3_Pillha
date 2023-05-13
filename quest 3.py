from pilha import Pilha

def calcular(valor):
    p_op = Pilha()
    p_num = Pilha()
    p_space = Pilha()
    for caractere in valor:
        if caractere.isnumeric():
            p_num.inserir(caractere)
        #retirando o espaço em branco
        elif caractere.isspace():
            p_space.inserir(caractere)
        #quardando as operações
        else:
            p_op.inserir(caractere)
    
    while not p_op.is_empty():
        if p_op.remover() == '+':
            num2 = p_num.remover()
            num1 = p_num.remover()
            resultado = int(num1) + int(num2)
            p_num.inserir(resultado)
        elif p_op.remover() == '-':
            num2 = p_num.remover()
            num1 = p_num.remover()
            resultado = int(num1) - int(num2)
            p_num.inserir(resultado)
        elif p_op.remover() == '*':
            num2 = p_num.remover()
            num1 = p_num.remover()
            resultado = int(num1) * int(num2)
            p_num.inserir(resultado)
        elif p_op.remover() == '/':
            num2 = p_num.remover()
            num1 = p_num.remover()
            resultado = int(num1) / int(num2)
            p_num.inserir(resultado)

    return p_num

numero = input('Digite uma expressão matematica: ')
res = calcular(numero)
while not res.is_empty():
    print(res.remover(),end=" ")