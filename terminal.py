import sys
import io

# Garantir que o terminal use UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

FILE_PATH = 'filmes_series.txt'

def menu():
    print("\nMenu Principal:")
    print("1. Incluir Filme/Série")
    print("2. Alterar Filme/Série")
    print("3. Excluir Filme/Série")
    print("4. Relatório Geral")
    print("5. Pesquisa Parcial")
    print("6. Sair")
    return input("Escolha uma opcao: ")

def incluir():
    with open(FILE_PATH, 'a', encoding='utf-8') as file:  # Certifique-se que a codificação é UTF-8
        titulo = input("Título: ")
        ano = input("Ano de Lançamento: ")
        genero = input("Gênero: ")
        status = input("Status (Assistido/Não Assistido): ")
        nota = input("Nota (1 a 5): ")
        comentarios = input("Comentários: ")
        file.write(f"{titulo},{ano},{genero},{status},{nota},{comentarios}\n")
    print("Filme/Série incluído com sucesso!")

def alterar():
    titulo = input("Digite o título do filme/série que deseja alterar: ")
    encontrado = False
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        for linha in linhas:
            dados = linha.strip().split(',')
            if dados[0] == titulo:
                print(f"Encontrado: {linha.strip()}")
                novo_titulo = input("Novo Título: ")
                novo_status = input("Novo Status (Assistido/Não Assistido): ")
                nova_nota = input("Nova Nota (1 a 5): ")
                novos_comentarios = input("Novos Comentários: ")
                file.write(f"{dados[0]},{dados[1]},{dados[2]},{novo_status},{novo_titulo},{nova_nota},{novos_comentarios}\n")
                encontrado = True
                print("Registro alterado com sucesso!")
            else:
                file.write(linha)
    if not encontrado:
        print("Filme/Série não encontrado.")

def excluir():
    titulo = input("Digite o título do filme/série que deseja excluir: ")
    encontrado = False
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        for linha in linhas:
            if linha.startswith(titulo):
                encontrado = True
                print("Registro excluído com sucesso!")
            else:
                file.write(linha)
    if not encontrado:
        print("Filme/Série não encontrado.")

def relatorio_geral():
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        print("\nRelatório Geral:")
        for linha in file:
            dados = linha.strip().split(',')
            print(f"Título: {dados[0]}, Ano: {dados[1]}, Gênero: {dados[2]}, Status: {dados[3]}, Nota: {dados[4]}, Comentários: {dados[5]}")

def pesquisa_parcial():
    termo = input("Digite o termo para pesquisa (título ou gênero): ")
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        print("\nResultados da Pesquisa:")
        for linha in file:
            if termo.lower() in linha.lower():
                dados = linha.strip().split(',')
                print(f"Título: {dados[0]}, Ano: {dados[1]}, Gênero: {dados[2]}, Status: {dados[3]}, Nota: {dados[4]}, Comentários: {dados[5]}")

# Loop principal
while True:
    opcao = menu()
    if opcao == '1':
        incluir()
    elif opcao == '2':
        alterar()
    elif opcao == '3':
        excluir()
    elif opcao == '4':
        relatorio_geral()
    elif opcao == '5':
        pesquisa_parcial()
    elif opcao == '6':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
