palavra = input("Digite uma palavra: ")

index = len(palavra) - 1
reverso = []

while index >= 0:
    reverso.append(palavra[index])
    index -= 1

reverso = ''.join(reverso)

print(f"\nO inverso da palavra é: {reverso}")