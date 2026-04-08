# Ítalo Felipe | Rafael de Araujo | Samuel Nunes | João Pedro
from aulagit.operacoesbd import * 
from dotenv import load_dotenv
import os
reclamacoes = []

def mostrar_menu():
    print("\n--- SISTEMA DE OUVIDORIA ---")
    print("1 - Listar reclamações")
    print("2 - Registrar nova reclamação")
    print("3 - Pesquisar reclamação")
    print("4 - Atualizar reclamação")
    print("5 - Remover reclamação")
    print("6 - Quantidade de reclamações")
    print("7 - Sair"


def registrar_reclamacao(conexao):
    texto = input("Digite a reclamação: ")

    sql = 'INSERT INTO equipamentos(reclamação) VALUES (%s)' 
    dados = (texto,)

    insertNoBancoDados(conexao,sql,dados)

    print('Reclamação cadastrada!')

def listar_reclamacoes(conexao):
    sql = 'SELECT * FROM equipamentos'

    resultado = listarBancoDados(conexao,sql)

    for item in resultado:
        print(item)


def pesquisar_reclamacao(conexao):
    codigo_procurado = int(input("Digite o código da reclamação: "))

    sql = 'SELECT * FROM equipamentos WHERE código = (%s)'
    dados = (codigo_procurado,)

    resultado = listarBancoDados(conexao,sql,dados)

    if len(resultado) == 0:
        print('Não há reclamação cadastrada nesse código')
    else:
        for item in resultado:
            print(item)

def atualizar_reclamacao(conexao):
    codigo_procurado = int(input("Digite o código da reclamação: "))
    novo_texto = input("Digite a nova reclamação: ")
    
    sql = 'UPDATE equipamentos SET reclamação = %s WHERE código = %s'
    dados = (novo_texto,codigo_procurado)

    qnt_linhas = atualizarBancoDados(conexao,sql,dados)

    if qnt_linhas == 0:
        print('Nenhuma reclamação registrada com esse código')
    else:
        print('Reclamação Atualizada!')


def remover_reclamacao(conexao):
    codigo_procurado = int(input("Digite o código da reclamação: "))

    sql = 'DELETE FROM equipamentos WHERE código = %s '
    dados = (codigo_procurado,)

    qnt_linhas = excluirBancoDados(conexao,sql,dados)

    if qnt_linhas == 0:
        print('Sem reclamações cadastradas nesse código!')
    else:
        print('Reclamação removida!')


def mostrar_total_reclamacoes(conexao):
    sql = 'SELECT * FROM equipamentos'

    resultado = listarBancoDados(conexao,sql)

    print('Total de reclamações:', len(resultado))


def main():
    load_dotenv()
    conexao = criarConexao(
    os.getenv("DB_HOST"),
    os.getenv("DB_USER"),
    os.getenv("DB_PASSWORD"),
    os.getenv("DB_NAME")
)
    opcao = ""

    while opcao != "7":
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_reclamacoes(conexao)
        elif opcao == "2":
            registrar_reclamacao(conexao)
        elif opcao == "3":
            pesquisar_reclamacao(conexao)
        elif opcao == "4":
            atualizar_reclamacao(conexao)
        elif opcao == "5":
            remover_reclamacao(conexao)
        elif opcao == "6":
            mostrar_total_reclamacoes(conexao)
        elif opcao == "7":
            print("Encerrando sistema...")
        else:
            print("Opção inválida. Tente novamente.")


main()
