nome = input("Qual o seu nome?")
print("Prazer em te conhecer {:^20}!".format(nome))

n1 = int(input("Um Valor: "))
n2 = int(input("Outro Valor: "))

soma = n1 + n2
subtracao = n1 - n2
mult = n1 * n2
div = n1 / n2
potencia = n1 ** n2
divInteira = n1 // n2
modulo = n1 % n2

print("A Soma vale {}".format(soma), end='')
print("A Subtracao vale {}".format(subtracao))
print ("A Multiplicacao vale {}".format(mult))
print("A Divisao vale {}".format(div))
print("A Potencia vale {}".format(potencia))
print("A Divisão inteira vale {}".format(divInteira))
print("O Modulo vale {}".format(modulo))