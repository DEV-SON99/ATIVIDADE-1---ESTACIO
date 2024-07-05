valor = float(input("digite um número: "))
valor2 = float(input("digite outro número: "))
operacao = input("Qual operação você quer fazer(+, -, * , /) ")

# CONDIÇÃO PARA RECEBER E IMPRIMIR O TIPO DE OPERAÇÃO DENTRO DO PRINT. Assim fica mais compreensivo o tipo de operação que foi efetuado.
if operacao == "+" :
    operador = "Soma"
if operacao == "-" :
    operador = "Subtração"
if operacao == "*" :
    operador = "Multiplicação"
if operacao == "/" :
    operador = "Divisão"


if operacao == "+":
    resultado = valor + valor2
if operacao == "-":
    resultado = valor - valor2
if operacao == "*":
    resultado = valor * valor2
if operacao == "/":
    resultado = valor /valor2

print("O resultado da operação de ", operador + " com os números ", str(valor) + " e " , str(valor2) + " é: " , resultado)