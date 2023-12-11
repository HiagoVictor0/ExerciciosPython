class Livro:
    def __init__(self, titulo, autor, data_publicacao, preco_alvo):
        self.titulo = titulo
        self.autor = autor
        self.data_publicacao = data_publicacao
        self.preco_alvo = preco_alvo

class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def exibir_livros(self):
        for i, livro in enumerate(self.livros):
            print(f"{i+1}. {livro.titulo}")
        
        opcao = input("Digite o número do livro que deseja visualizar (ou '0' para sair): ")
        
        while opcao != '0':
            try:
                indice = int(opcao) - 1
                livro = self.livros[indice]
                print(f"Título: {livro.titulo}")
                print(f"Autor: {livro.autor}")
                print(f"Data de publicação: {livro.data_publicacao}")
                print(f"Preço-alvo: {livro.preco_alvo}")
            except (ValueError, IndexError):
                print("Opção inválida.")
            
            opcao = input("Digite o número do livro que deseja visualizar (ou '0' para sair): ")

biblioteca = Biblioteca()

num_livros = int(input("Quantos livros deseja adicionar à biblioteca? "))

for i in range(num_livros):
    titulo = input("Título: ")
    autor = input("Autor: ")
    data_publicacao = input("Data de publicação: ")
    preco_alvo = float(input("Preço-alvo: "))
    
    livro = Livro(titulo, autor, data_publicacao, preco_alvo)
    biblioteca.adicionar_livro(livro)

biblioteca.exibir_livros()