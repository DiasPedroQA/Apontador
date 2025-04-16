# -*- coding: utf-8 -*-
# pylint: disable=line-too-long, missing-module-docstring, missing-class-docstring, missing-function-docstring  # noqa: E501

import re

from typing import TypedDict

try:
    from app.mensagens.mensageiro import MENSAGENS
except ImportError:
    MENSAGENS = {
        "validação": {
            "caracteres_proibidos": "O caminho '{caminho}' contém caracteres proibidos.",
            "caminho_identificado": "O caminho '{caminho}' foi identificado com sucesso.",
            "sistema_desconhecido": (
                "Não foi possível identificar o sistema para o caminho '{caminho}'."
            ),
        }
    }


class Identidade(TypedDict):
    caminho_entrada: str
    sistema_operacional: str
    identificado: bool
    mensagem: str


class ValidadorTriFasico:
    REGRAS = {
        "Mac": {
            "regex": r"^/([a-zA-Z0-9._ -]+/?)*$",
            "caracteres_proibidos": ":",
        },
        "Linux": {
            "regex": r"^/([a-zA-Z0-9._-]+/?)*$",
            "caracteres_proibidos": "\0",
        },
        "Windows": {
            "regex": r"^[a-zA-Z]:\\(?:[^\\/:*?\"<>|\r\n]+\\)*[^\\/:*?\"<>|\r\n]*$",
            "caracteres_proibidos": '<>:"/\\|?*',
        },
    }

    @classmethod
    def identificar_so(cls, caminho: str) -> Identidade:
        for sistema, regras in cls.REGRAS.items():
            if re.fullmatch(regras["regex"], caminho):
                if any(char in caminho for char in regras["caracteres_proibidos"]):
                    return cls._resultado(
                        caminho,
                        sistema,
                        False,
                        MENSAGENS["validação"]["caracteres_proibidos"].format(
                            caminho=caminho
                        ),
                    )
                return cls._resultado(
                    caminho,
                    sistema,
                    True,
                    MENSAGENS["validação"]["caminho_identificado"].format(
                        caminho=caminho
                    ),
                )
        # Adiciona retorno caso nenhum sistema reconheça
        return cls._resultado(
            caminho,
            "Desconhecido",
            False,
            MENSAGENS["validação"]["sistema_desconhecido"].format(caminho=caminho),
        )

    @staticmethod
    def _resultado(
        caminho: str, sistema_operacional: str, identificado: bool, mensagem: str
    ) -> Identidade:
        return {
            "caminho_entrada": caminho,
            "sistema_operacional": sistema_operacional,
            "identificado": identificado,
            "mensagem": mensagem,
        }


if __name__ == "__main__":
    caminhos_teste = {
        "Windows": [
            r"C:\\Users\\Pedro\\Documents\\arquivo.txt",  # válido - arquivo absoluto
            r"C:\\Users\\Pedro\\Documents\\",  # válido - diretório absoluto
            r"Users\\Pedro\\Documents\\arquivo.txt",  # inválido - relativo
            r"C:\\Inva|ido\\arquivo.txt",  # inválido - caractere proibido
        ],
        "Linux": [
            "/home/user/documento.txt",  # válido - arquivo absoluto
            "/home/user/docs/",  # válido - diretório absoluto
            "home/user/arquivo",  # inválido - relativo
            "/etc/passwd\0",  # inválido - caractere proibido
        ],
        "Mac": [
            "/Users/Name/Documents/file.txt",  # válido - arquivo absoluto
            "/Users/Name/Documents/",  # válido - diretório absoluto
            "Users/Name/file.txt",  # inválido - relativo
            "/Users/Na:me/file.txt",  # inválido - caractere proibido
        ],
        "Desconhecido": [
            ":::INVALIDO:::",  # inválido para todos
            "arquivo.txt",  # relativo puro
        ],
    }

    for sistema, caminhos in caminhos_teste.items():
        print(f"\n--- Testando caminhos para {sistema} ---")
        for caminho in caminhos:
            resultado = ValidadorTriFasico.identificar_so(caminho)
            print(resultado)
