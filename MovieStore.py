import sqlite3
banco = sqlite3.connect('filmes.db')
sql = banco.cursor()
sair = 'n'


def TodosFilmes():
    sql.execute("SELECT * FROM filmes")
    print('Esses são todos os filmes cadastrados:')
    for row in sql.fetchall():
        print('ID:', row[0])
        print('Nome:',row[1])
        print('Duração:',row[2])
        print('Status:',row[3])
        print('===============================')


def MostrarFilmesN():
    sql.execute("SELECT * FROM filmes WHERE status = 'Não assistido'")
    print('Aqui estão os filmes que ainda não foram assistidos:')
    for row in sql.fetchall():
        print('ID:',row[0])
        print('Nome:',row[1])
        print('Duração:',row[2])
        print('===============================')


while sair == 'n':
    print("""###Store Filmes###
    O que deseja fazer?
    [1] - Cadastrar um novo filme;
    [2] - Ver os filmes não assistidos;
    [3] - Informar um filme já assistido;
    [4] - Ver todos os filmes;
    [5] - Remover um filme.
    """)
    escolha = input('Opção: ')
    if escolha == '1':
        nome = input('Qual o nome do filme? ')
        duracao = int(input('Qual a sua duração (em minutos)? '))
        sql.execute(f"INSERT INTO filmes (nome, tempo, status) VALUES ('{nome}', {duracao}, 'Não assistido')")
        banco.commit()
        input('Filme cadastrado com sucesso! Enter para continuar.')
    elif escolha == '2':
        MostrarFilmesN()
        input('Pressione Enter para continuar.')
    elif escolha == '3':
        MostrarFilmesN()
        ID = int(input('Qual o ID do filme assistido? '))
        sql.execute(f"UPDATE filmes SET status = 'Assistido' WHERE id = {ID}")
        input('Filme atualizado! Enter para continuar.')
    elif escolha == '4':
        TodosFilmes()
        input('Pressione Enter para continuar.')
    elif escolha == '5':
        TodosFilmes()
        ID = int(input('Qual o ID do filme para remoção? '))
        sql.execute(f'DELETE FROM filmes WHERE id = {ID}')
        print('Filme deletado com sucesso! Enter para continuar.')
    else:
        print('Opção Invalida')






