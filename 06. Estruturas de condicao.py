##6. Estrutura de condição
nome, idade, sobrenome  = 'João', 10, 'Silva'

print(f'Olá, {nome} {sobrenome}, sua idade é {idade}')

nome2 = input("Digite o seu nome: ")
idade2 = int(input("Digite sua idade: "))
sobrenome2 = input("Digite o seu sobrenome: ")

print(f'Olá, {nome2} {sobrenome2}, sua idade é {idade2}')

media_idades = (idade + idade2)/2
print(f'A soma das idade é: {media_idades}')

if idade >= 18:
    print(f"{nome} é maior de idade") 
else:
    print(f"{nome} é menor de idade") 
    
if idade2 <= 17:
    print(f"{nome2} é adolescente") 
elif idade2 <= 18 and idade2 <= 50:
    print(f"{nome2} é adulto")
else:
    print(f"{nome2} é idoso")
    
##6.1 de Estrutura de condição
n = int(input())
if(n % 2 == 0):
    print("Par")
else:
    print("Ímpar")

##6.2 de Estrutura de condição
n = int(input())
        
if(n % 2 != 0):
    print("Estranho")
else:
    if(n < 10):
        print("Não é estranho")
    elif(n >= 10 and n <= 20):
        print("Estranho")
    else:
        print("Não é estranho")

    