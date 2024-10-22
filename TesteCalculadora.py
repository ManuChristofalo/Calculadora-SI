# ====================================  Calculadora | Testes  ===========================================
# Administração de Sistemas de Informação
# Abordagens para Construção de SI
# Feito por: Manu e Paulo
# Data: 22/10/2024
# =======================================================================================================


from Calculadora import calcula

def teste_soma():
    assert calcula(5, 3, '+') == 8
    assert calcula(-5, 3, '+') == -2
    assert calcula(5.5, 2.5, '+') == 8

def teste_subatracao():
    assert calcula(5, 3, '-') == 2
    assert calcula(-5, -3, '-') == -2
    assert calcula(5.5, 2.5, '-') == 3

def teste_multiplicacao():
    assert calcula(5, 3, '*') == 15
    assert calcula(-5, 3, '*') == -15
    assert calcula(5.5, 2, '*') == 11

def teste_divisao():
    assert calcula(6, 3, '/') == 2
    assert calcula(6.0, 3.0, '/') == 2
    assert calcula(-6, 3, '/') == -2
    assert calcula(6, 0, '/') == None  # Teste de divisão por zero

def teste_potencia():
    assert calcula(2, 3, '^') == 8
    assert calcula(5, 0, '^') == 1
    assert calcula(-2, 3, '^') == -8

def teste_opInvalida():
    assert calcula(5, 3, '%') == None  # Operação inválida
    assert calcula(5, 3, '&') == None  # Operação inválida

def teste_naoNumero():
    assert calcula("a", 3, '+') == None  # Entrada inválida
    assert calcula(5, "b", '*') == None  # Entrada inválida
    assert calcula(5, 3, 'Tipos inválidos') == None  # Operação inválida
