import re

usuarios = {}


class Usuario:
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        if not re.match(r"\d{2}/\d{2}/\d{4}", data_nascimento):
            raise ValueError("Data de nascimento inválida")
        if not re.match(r"\d{11}", cpf):
            raise ValueError("CPF inválido")
        if not re.match(r".+, \d+ - .+ - .+/\w{2}", endereco):
            raise ValueError("Endereço inválido")
        if cpf in usuarios:
            raise ValueError("CPF já cadastrado")
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas: list = []
        usuarios[cpf] = self