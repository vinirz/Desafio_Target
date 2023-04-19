def fibonacci(limite): #calcula a sequencia de fibonacci
    fib = [0, 1] # Inicia a sequência com os valores 0 e 1

    while fib[-1] < limite: # Continua adicionando números à sequência até que o último valor seja maior ou igual ao limite informado
        fib.append(fib[-1] + fib[-2]) # Adiciona o próximo valor da sequência como a soma dos dois valores anteriores

    return fib

# Pede para o usuário informar um número
numero = int(input("Digite um número: "))

# Chama a função para calcular a sequência até o numero desejado
sequencia = fibonacci(numero)

print(f"\n>> {sequencia}\n")

# Verifica se o número informado pertence à sequência de Fibonacci
if numero in sequencia:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")