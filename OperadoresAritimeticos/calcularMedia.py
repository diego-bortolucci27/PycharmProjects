nota1 = float(input('Digite a Primeira Nota do Aluno: '))
nota2 = float(input('Digite a Segunda Nota do Aluno: '))
nota3 = float(input('Digite a Terceira Nota do Aluno: '))

soma = nota1 + nota2 + nota3
media = soma / 3

print("A Soma das Notas foi {} | Média: {:.2f}".format(soma, media))