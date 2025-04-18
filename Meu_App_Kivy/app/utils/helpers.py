# pylint: disable=C0114, C0115, C0116, R0903

def saudacao(nome: str) -> str:
    return f"Olá, {nome}!"


def formatar_nome(nome: str) -> str:
    return nome.strip().title()
