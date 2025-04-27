# sistema_biblioteca.py

class Livro:
    def __init__(self, titulo, autor, ano_publicacao, copias_disponiveis):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.copias_disponiveis = copias_disponiveis

    def __str__(self):
        return f'"{self.titulo}" por {self.autor} ({self.ano_publicacao}) - {self.copias_disponiveis} cópias disponíveis'


class Usuario:
    def __init__(self, nome, id_usuario, contato):
        self.nome = nome
        self.id_usuario = id_usuario
        self.contato = contato

    def __str__(self):
        return f'{self.nome} (ID: {self.id_usuario}, Contato: {self.contato})'


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = {}  # id_usuario -> lista de livros emprestados

    # Cadastro de Livro
    def cadastrar_livro(self, titulo, autor, ano, copias):
        livro = Livro(titulo, autor, ano, copias)
        self.livros.append(livro)
        print("Livro cadastrado com sucesso!")

    # Cadastro de Usuário
    def cadastrar_usuario(self, nome, id_usuario, contato):
        if any(u.id_usuario == id_usuario for u in self.usuarios):
            print("Erro: ID de usuário já cadastrado.")
            return
        usuario = Usuario(nome, id_usuario, contato)
        self.usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

    # Empréstimo de Livro
    def emprestar_livro(self, id_usuario, titulo):
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            print("Usuário não encontrado.")
            return
        livro = self.buscar_livro(titulo)
        if not livro:
            print("Livro não encontrado.")
            return
        if livro.copias_disponiveis < 1:
            print("Não há cópias disponíveis para empréstimo.")
            return
        livro.copias_disponiveis -= 1
        self.emprestimos.setdefault(id_usuario, []).append(livro)
        print(f'Livro "{livro.titulo}" emprestado para {usuario.nome}.')

    # Devolução de Livro
    def devolver_livro(self, id_usuario, titulo):
        usuario = self.buscar_usuario(id_usuario)
        if not usuario:
            print("Usuário não encontrado.")
            return
        emprestimos_usuario = self.emprestimos.get(id_usuario, [])
        for livro in emprestimos_usuario:
            if livro.titulo.lower() == titulo.lower():
                livro.copias_disponiveis += 1
                emprestimos_usuario.remove(livro)
                print(f'Livro "{livro.titulo}" devolvido com sucesso.')
                return
        print("Este livro não foi emprestado para este usuário.")

    # Consulta de Livros
    def consultar_livros(self, criterio, valor):
        resultados = []
        for livro in self.livros:
            if criterio == "titulo" and valor.lower() in livro.titulo.lower():
                resultados.append(livro)
            elif criterio == "autor" and valor.lower() in livro.autor.lower():
                resultados.append(livro)
            elif criterio == "ano" and str(livro.ano_publicacao) == str(valor):
                resultados.append(livro)

        if resultados:
            print("Livros encontrados:")
            for livro in resultados:
                print(livro)
        else:
            print("Nenhum livro encontrado com esse critério.")

    # Relatórios
    def listar_livros_disponiveis(self):
        print("\nLivros disponíveis:")
        for livro in self.livros:
            if livro.copias_disponiveis > 0:
                print(livro)

    def listar_livros_emprestados(self):
        print("\nLivros emprestados:")
        for id_usuario, livros in self.emprestimos.items():
            usuario = self.buscar_usuario(id_usuario)
            for livro in livros:
                print(f'Livro: "{livro.titulo}" | Usuário: {usuario.nome}')

    def listar_usuarios(self):
        print("\nUsuários cadastrados:")
        for usuario in self.usuarios:
            print(usuario)

    # Funções Auxiliares
    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None


def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n===== MENU BIBLIOTECA =====")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Empréstimo de Livro")
        print("4. Devolução de Livro")
        print("5. Consultar Livros")
        print("6. Relatórios")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano de Publicação: ")
            copias = int(input("Número de cópias disponíveis: "))
            biblioteca.cadastrar_livro(titulo, autor, ano, copias)

        elif opcao == "2":
            nome = input("Nome: ")
            id_usuario = input("ID do Usuário: ")
            contato = input("Contato: ")
            biblioteca.cadastrar_usuario(nome, id_usuario, contato)

        elif opcao == "3":
            id_usuario = input("ID do Usuário: ")
            titulo = input("Título do Livro: ")
            biblioteca.emprestar_livro(id_usuario, titulo)

        elif opcao == "4":
            id_usuario = input("ID do Usuário: ")
            titulo = input("Título do Livro: ")
            biblioteca.devolver_livro(id_usuario, titulo)

        elif opcao == "5":
            criterio = input("Consultar por (titulo/autor/ano): ").lower()
            valor = input("Digite o valor da busca: ")
            biblioteca.consultar_livros(criterio, valor)

        elif opcao == "6":
            print("\n===== RELATÓRIOS =====")
            print("1. Livros Disponíveis")
            print("2. Livros Emprestados")
            print("3. Usuários Cadastrados")
            subopcao = input("Escolha uma opção: ")

            if subopcao == "1":
                biblioteca.listar_livros_disponiveis()
            elif subopcao == "2":
                biblioteca.listar_livros_emprestados()
            elif subopcao == "3":
                biblioteca.listar_usuarios()
            else:
                print("Opção inválida!")

        elif opcao == "0":
            print("Saindo do sistema... Até logo!")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
