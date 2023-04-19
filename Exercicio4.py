faturamento = [
    {
        "estado": "SP", 
        "valor": (67836.43)
    },
    {
        "estado": "RJ", 
        "valor": (36678.66)
    },
    {
        "estado": "MG", 
        "valor": (29229.88)
    },
    {
        "estado": "ES", 
        "valor": (27165.48)
    },
    {
        "estado": "OUTROS", 
        "valor": (19849.53)
    },
]

valores = []

for i in faturamento:
    valores.append(i['valor'])

total = sum(valores)
print(f"\nFaturamento total: {total}\n")

for estado in faturamento:
    percentual = (estado['valor'] / total) * 100

    print(f"{estado['estado']} representa {percentual:.2f}% do valor total")
