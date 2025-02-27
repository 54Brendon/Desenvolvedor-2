# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:01:11 2025

@author: 54bre
"""

def is_fibonacci(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

# Solicita um número ao usuário
numero = int(input("Informe um número: "))

# Verifica se o número informado pertence à sequência de Fibonacci
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
