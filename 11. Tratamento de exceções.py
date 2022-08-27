##9. Modulos
from usuario import Usuario
#import usuario
 
continuar = 1   
lista_usuarios = []

while continuar != 0:
    try:
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite sua idade: "))
        sobrenome = input("Digite o seu sobrenome: ")
        usuario = Usuario(nome, idade, sobrenome)
        
        lista_usuarios.append(usuario)
        
        if usuario.idade == 99:
            break
        
        if usuario.idade == 98:
            continue

        print(f'Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}')

        if usuario.idade <= 17:
            print(f"{usuario.nome} é adolescente") 
        elif usuario.idade >= 18 and usuario.idade <= 50:
            print(f"{usuario.nome} é adulto")
        else:
            print(f"{usuario.nome} é idoso")
        continuar = int(input("Deseja continuar cadastrando? 0 - Sair 1 - Continuar : "))
    except ValueError:
        print("Você deve informar um número válido")
else:
    print("Lista de Usuarios cadastrados")
    for x in lista_usuarios:
         print(f"Nome completo: {x.nome} {x.sobrenome} - Idade {x.idade}")
         
##10. Listas
t = int(input())
for i in range(0,t):
    a, b, n = input().split()
        
    result = []
    for j in range(0,int(n)):
        result.insert(j, int(a))
        
        for k in range(0,j+1):
            exp = pow(2, k)
            result[j] += exp * int(b);
            
    for r in result:
        print(r, end = ' ')
        
    print('')

##10. Listas
n = int(input())

lista = []
for i in range(0, n):
    values = input().split()

    if len(values) == 3:
        acao, i, e = values
    elif len(values) == 2:
        acao, e = values
    else:
        acao = values.pop()
    
    if acao == "insert":
        lista.insert(int(i), int(e))
    elif acao == "print":
        print(lista)
    elif acao == "remove":
        lista.remove(int(e))
    elif acao == "append":
        lista.append(int(e))
    elif acao == "sort":
        lista.sort()
    elif acao == "pop":
        lista.pop()
    elif acao == "reverse":
        lista.reverse()
        
    ##11. Exceções
