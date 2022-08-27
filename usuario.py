class Usuario:
    def __init__(self, nome, idade, sobrenome):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome


##8.1 Objetos        
class PrimeiraClasse:

    def __init__(self, curso, descricao):
        self.curso = curso
        self.descricao = descricao

if __name__ == "__main__":
    pc = PrimeiraClasse(input(), input())
    
    print(pc.curso)
    print(pc.descricao)