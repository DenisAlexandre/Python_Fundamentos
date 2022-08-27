##4. Operadores de atribuição
nome, idade, sobrenome  = 'João', 25, 'Silva'

print('nome, sobrenome, idade')

print('Olá,', nome, sobrenome,' sua idade é', idade)
print(f'Olá, {nome} {sobrenome}, sua idade é {idade}')

nome2 = input("Digite o seu nome: ")
sobrenome2 = int(input("Digite o seu sobrenome: "))
idade2 = input("Digite sua idade: ")

print(type(idade2))

print(f'Olá, {nome2} {sobrenome2}, sua idade é {idade2}')

##4.1 Operadores de atribuição
linguagem, nivel, companhia = input().split()

print(linguagem)
print(nivel)
print(companhia)




