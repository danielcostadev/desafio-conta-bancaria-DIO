from modules.cadastro_usuario import CadastrarUsuario
from modules.cadastro_conta import CadastrarConta
from modules.listar_usuario import ListarUsuarios
from modules.listar_conta import ListarContas
from business.deposito import realizarDeposito

menu = """
[cu] Cadastrar Usuário
[cc] Cadastrar Conta
[lu] Listar usuários
[lc] Listar contas de um usuário
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

while True:

    opcao = input(menu).lower()

    match opcao:
        case "cu":
            print(CadastrarUsuario())
        case "cc":
            print(CadastrarConta())
        case "lu":
            print(ListarUsuarios())
        case "lc":
            print(ListarContas())
        case "d":
            print(realizarDeposito())
        case "s":
            print(realizarDeposito())
        case "e":
            print(realizarDeposito())
        case "q":
            break
        case _:
            print("Operação inválida!")
