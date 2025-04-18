# pylint: disable=C0114, C0115, C0116, R0903


class Mensageiro:
    @staticmethod
    def mensagem_sucesso(nome: str) -> str:
        return f"Bem-vindo(a), {nome}!"
