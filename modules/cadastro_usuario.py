from business.usuario import Usuario


def CadastrarUsuario():

    nome = input("Digite o nome de usuário: ").title()
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Digite o CPF (somente números): ")
    print("\nAgora vamos Cadastrar o seu endereço.\n")
    endereco_logradouro = input("Logradouro: ")
    endereco_numero = input("Número da Residência: ")
    endereco_bairro = input("Bairro: ").title()
    endereco_cidade = input("Cidade/Sigla Estado: ")
    try:
        usuario = Usuario(
            nome,
            data_nascimento,
            cpf,
            endereco_logradouro,
            endereco_numero,
            endereco_bairro,
            endereco_cidade,
        )
        return f"Usuário {nome} criado com sucesso!"
    except ValueError as e:
        return e
