import json
import os
from cliente import Cadastro
from horario import Horarios

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar cliente")
        print("2. Listar horarios")
        print("3. Retirar cliente")
        print("4. Catálogo de cortes")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastro = Cadastro()
            cadastro.adicionar_cliente()
        elif opcao == "2":
            horarios = Horarios()
            horarios.mostrar_horarios(Cadastro.carregar_dados(Cadastro.ARQUIVO))
        elif opcao == "3":
            nome_cliente = input("Digite o nome do cliente: ").lower().capitalize()
            Cadastro.excluir_cliente(nome_cliente)
        elif opcao == "4":
            print("Catálogo de cortes:")
            print("1. Corte de cabelo -- R$ 25,00")
            print("2. Corte de barba -- R$ 10,00")
            print("3. Sobrancelha -- R$ 5,00")
            print("4. Corte de cabelo e barba -- R$ 35,00")
            print("5. Corte de cabelo e sobrancelha  -- R$ 30,00")
            print("6. Corte de cabelo e cabelo com descoloração -- R$ 70,00")
            print("7. Corte de cabelo, cabelo com descoloração e barba -- R$ 80,00")
            print("8. Corte de cabelo, cabelo com descoloração e sobrancelha -- R$ 100,00")
            print("9. Corte de cabelo, cabelo com descoloração, barba e sobrancelha -- R$ 105,00")
            print("")
        elif opcao == "0":
            break
        
if __name__ == "__main__":
    menu()
