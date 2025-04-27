# 📚 Sistema de Gerenciamento de Biblioteca

## Sobre o Projeto

Este projeto é um sistema de gerenciamento de biblioteca feito em **Python**, utilizando princípios de **Programação Orientada a Objetos (POO)**.  
Ele permite o cadastro de livros e usuários, controle de empréstimos e devoluções, consultas e geração de relatórios simples através de um menu interativo no console.

## Funcionalidades

- **Cadastro de Livros**
  - Título, autor, ano de publicação e número de cópias.
- **Cadastro de Usuários**
  - Nome, ID do usuário e contato.
- **Empréstimo de Livros**
  - Verificação de disponibilidade antes do empréstimo.
  - Atualização automática das cópias disponíveis.
- **Devolução de Livros**
  - Devolução de livros e atualização do estoque.
- **Consulta de Livros**
  - Pesquisa por título, autor ou ano de publicação.
- **Relatórios**
  - Livros disponíveis.
  - Livros emprestados.
  - Usuários cadastrados.

## Tecnologias Utilizadas

- **Python 3.12**
- Programação Orientada a Objetos (POO)
- Interface baseada em console (CLI)

## Como Executar

1. Certifique-se de ter o Python instalado.
2. Baixe o arquivo `sistema_biblioteca.py`.
3. No terminal, execute:

```bash
python sistema_biblioteca.py
```

4. Navegue pelas opções do menu.

## Estrutura do Projeto

- `Livro` → Classe para livros (título, autor, ano, cópias).
- `Usuario` → Classe para usuários da biblioteca (nome, ID, contato).
- `Biblioteca` → Classe principal que gerencia livros, usuários e empréstimos.
- `menu()` → Função que exibe o menu interativo.

## Boas Práticas Aplicadas

- Código modular e organizado.
- Tratamento de erros e validações.
- Facilmente expansível para novas funcionalidades.
- Código comentado para facilitar a manutenção.

## Futuras Melhorias

- Persistência de dados (armazenamento em arquivos JSON ou CSV).
- Sistema de multas para atrasos nas devoluções.
- Controle de histórico de empréstimos.
- Interface gráfica (GUI) utilizando Tkinter ou frameworks web.

## Autor

Desenvolvido por Maicon Leal ✨
