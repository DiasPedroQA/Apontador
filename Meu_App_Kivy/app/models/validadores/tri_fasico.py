# -*- coding: utf-8 -*-
# pylint: disable=line-too-long, missing-module-docstring

import re

from typing import TypedDict

from app.mensagens.mensageiro import MENSAGENS


class Identidade(TypedDict):
    """
        Representa o resultado da identificação
        de um caminho de arquivo ou diretório.

        A estrutura contém o caminho informado,
        o sistema operacional identificado,
        se o caminho é sintaticamente válido
        e uma mensagem explicativa.
    """
    caminho_entrada: str
    sistema_operacional: str
    identificado: bool
    mensagem: str


class ValidadorTriFasico:
    """
        Responsável por identificar e validar caminhos de arquivos/diretórios
        com base em padrões específicos dos sistemas operacionais:
        Windows, Linux e macOS.
    """

    REGRAS = {
        "Windows": {
            "regex": r"^[a-zA-Z]:\\(?:[^\\/:*?\"<>|\r\n]+\\)*[^\\/:*?\"<>|\r\n]*$",
            "caracteres_proibidos": '<>:"/\\|?*',
        },
        "Linux": {
            "regex": r"^/([a-zA-Z0-9._-]+/?)*$",
            "caracteres_proibidos": "\0",
        },
        "Mac": {
            "regex": r"^/([a-zA-Z0-9._ -]+/?)*$",
            "caracteres_proibidos": ":",
        },
    }

    @classmethod
    def identificar_so(cls, caminho: str) -> Identidade:
        """
            Identifica o sistema operacional e valida a estrutura do caminho.

            Args:
                caminho (str): Caminho informado pelo usuário.

            Returns:
                Identidade: Resultado com sistema identificado, validade
                        e mensagem explicativa.
        """
        for sistema, regras in cls.REGRAS.items():
            if any(
                char in caminho
                for char in regras["caracteres_proibidos"]
            ):
                return cls._resultado(
                    caminho,
                    sistema,
                    False,
                    MENSAGENS["validação"]["caracteres_proibidos"].format(
                        caminho=caminho
                    )
                )

            if re.fullmatch(regras["regex"], caminho):
                return cls._resultado(
                    caminho,
                    sistema,
                    True,
                    MENSAGENS["validação"]["caminho_identificado"].format(
                        caminho=caminho
                    )
                )

        return cls._resultado(
            caminho,
            "Desconhecido",
            False,
            MENSAGENS["validação"]["sistema_desconhecido"].format(
                caminho=caminho
            )
        )

    @staticmethod
    def _resultado(
        caminho: str,
        sistema_operacional: str,
        identificado: bool,
        mensagem: str
    ) -> Identidade:
        return {
            "caminho_entrada": caminho,
            "sistema_operacional": sistema_operacional,
            "identificado": identificado,
            "mensagem": mensagem,
        }
