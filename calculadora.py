import os

print("Calculadora Simples - Python")

continuar = "s"

while continuar == "s":
    valor_1 = int(input("\nDigite o 1° número: "))
    valor_2 = int(input("Digite o 2° número: "))

    print("\nOperações: + (Soma), - (Subtração), * (Multiplicação), / (Divisão)")

    operacao = input("\nEscolha a operação (digite o símbolo): ")

    # Soma
    if operacao == "+":
        resultado = valor_1 + valor_2
        print("\nO valor da soma é: ", resultado)
        continuar = input("Gostaria de continuar (s/n)? ")

    # Subtração
    elif operacao == "-":
        resultado = valor_1 - valor_2
        print("\nO valor da subtração é: ", resultado)
        continuar = input("Gostaria de continuar (s/n)? ")

    # Multiplicação
    elif operacao == "*":
        resultado = valor_1 * valor_2
        print("\nO valor da multiplicação é: ", resultado)
        continuar = input("Gostaria de continuar (s/n)? ")

    # Divisão
    elif operacao == "/":
        resultado = valor_1 / valor_2
        print("\nO valor da divisão é: ", resultado)
        continuar = input("Gostaria de continuar (s/n)? ")
    else:
        print("\nOperação inválida")
        continuar = input("Gostaria de continuar (s/n)? ")

os.system("pause")
