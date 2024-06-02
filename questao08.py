n1 = int(input("Me diga um número"))
operacao = input("Digite uma operação")
n2 = int(input("Me diga outro número"))
if operacao == '+':
    resultado = n1 + n2
elif operacao == '-':
    resultado = n1 - n2
elif operacao == '/':
    resultado = n1 / n2
elif operacao == '*':
    resultado = n1 * n2
else:
    resultado = "Operação não reconhecida"
print(f'{resultado} é o resultado da sua operação')
