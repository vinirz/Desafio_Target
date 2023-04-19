import json
import statistics
import operator

jsonData = open('dados.json')
data = json.load(jsonData)

dados = []

for i in data:
    if i['valor'] != 0.0:
        dados.append(i)

# Menor valor de faturamento ocorrido em um dia do mês
menor_valor = min(dado['valor'] for dado in dados)
print(f"Menor valor de faturamento: {menor_valor}")

# Maior valor de faturamento ocorrido em um dia do mês
maior_valor = max(dado['valor'] for dado in dados)
print("Maior valor de faturamento:", maior_valor)

# Média mensal de faturamento
media_mensal = sum(dado['valor'] for dado in dados) / len(dados)

# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal
dias_acima_media = sum(1 for dado in dados if dado['valor'] > media_mensal)
print("Dias em que o valor de faturamento diário foi superior à média mensal:", dias_acima_media)
