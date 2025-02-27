{
  "faturamento_diario": [2000, 1500, 0, 3000, 1000, 0, 7000, 0, 4000, 0, 6000, 2300, 5000, 2700, 3200, 0, 800, 1000, 4500, 3800, 2900, 0, 1300, 2100, 1800, 5000, 600, 1700, 3000, 1500]
}

import json

def calcular_faturamento(faturamento_diario):
    # Remove dias com faturamento zero (dias sem faturamento)
    faturamento_valido = [dia for dia in faturamento_diario if dia > 0]
    
    # Calcula menor, maior e média do faturamento
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)
    
    # Conta os dias acima da média
    dias_acima_media = sum(1 for dia in faturamento_valido if dia > media_mensal)
    
    # Retorna os resultados
    return menor_faturamento, maior_faturamento, dias_acima_media

def ler_faturamento_json(caminho_arquivo):
    # Abre o arquivo JSON e carrega os dados
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados['faturamento_diario']

# Lê os dados do arquivo JSON
faturamento_diario = ler_faturamento_json('faturamento.json')

# Chama a função e recebe os resultados
menor_faturamento, maior_faturamento, dias_acima_media = calcular_faturamento(faturamento_diario)

# Exibe os resultados
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
