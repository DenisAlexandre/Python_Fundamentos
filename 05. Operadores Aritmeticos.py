##5. Operadores Aritméticos
nome, idade, sobrenome  = 'João', 25, 'Silva'

print('nome, sobrenome, idade')

print('Olá,', nome, sobrenome,' sua idade é', idade)
print(f'Olá, {nome} {sobrenome}, sua idade é {idade}')

nome2 = input("Digite o seu nome: ")
sobrenome2 = input("Digite o seu sobrenome: ")
idade2 = int(input("Digite sua idade: "))

print(type(idade2))

print(f'Olá, {nome2} {sobrenome2}, sua idade é {idade2}')

soma_idades = idade + idade2
print(f'A soma das idade é: {soma_idades}')

subtracao_idades = idade - idade2
print(f'A soma das idade é: {subtracao_idades}')

multiplicao_idades = idade * idade2
print(f'A soma das idade é: {multiplicao_idades}')

media_idades = (idade + idade2)/2
print(f'A soma das idade é: {media_idades}')


##5. Operadores Aritméticos

var1 = int(input())
var2 = int(input())

print(var1 + var2)
print(var1 - var2)
print(var1 * var2)