# =================================  Calculadora | Código fonte  ========================================
# Administração de Sistemas de Informação
# Abordagens para Construção de SI
# Feito por: Manu e Paulo
# Data: 22/10/2024
# =======================================================================================================


def calcula(a, b, operacao):
#1. Validação do tipo número
    try:
        a = float(a)
        b = float(b)

    except ValueError:
        return None             # -> não é número


#2. Tratamento da operação
    # -> Soma
    if operacao == '+': return a + b

    # -> Subtração
    elif operacao == '-': return a - b

    # -> Multiplicação
    elif operacao == '*': return a * b

    # -> Divisão
    elif operacao == '/':
        if b == 0: return None  # Evita divisão por zero
        return a / b
    
    # -> Potência
    elif operacao == '^': return a ** b
    
    # Tipo inválido
    else: return None          
