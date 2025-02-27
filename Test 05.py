# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:21:55 2025

@author: 54bre
"""

# Função para inverter a string
def inverter_string(s):
    # Variável para armazenar a string invertida
    string_invertida = ""
    
    # Laço para percorrer a string de trás para frente
    for i in range(len(s)-1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida

# Entrada de dados
string = input("Digite uma string para inverter: ")

# Chama a função para inverter a string
resultado = inverter_string(string)

# Exibe o resultado
print(f"String invertida: {resultado}")
