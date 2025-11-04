numero = int(input("Digite um numero para ver a sua tabuada: "))
i = 0
while i < 11:
    resultado = numero * i
    print("{} x {} = {}".format(numero, i, resultado))
    i = i + 1

