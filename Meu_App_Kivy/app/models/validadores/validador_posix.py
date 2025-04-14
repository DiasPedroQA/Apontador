# -*- coding: utf-8 -*-
"""
Validador de caminhos de arquivos para sistemas Linux.

Este módulo define a classe `ValidadorLinux`, responsável por verificar se um caminho
está de acordo com a sintaxe válida para sistemas operacionais do tipo Linux/POSIX.
São considerados caracteres proibidos e estrutura de diretórios conforme a convenção Unix.
"""

# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, line-too-long, import-error  # noqa: E501

import re

from mensagens.mensagens import MENSAGENS
from models.tipos_validacao import ResultadoValidacao


class ValidadorLinux:
    """
    Classe responsável pela validação sintática de caminhos em sistemas Linux.

    Utiliza expressões regulares para garantir que os caminhos
    estejam no formato permitido e realiza verificações de caracteres proibidos.
    """

    CAMINHO_REGEX = r"^/([a-zA-Z0-9._-]+/?)*$"

    @classmethod
    def validar(cls, caminho_entrada: str) -> ResultadoValidacao:
        """
        Valida o caminho fornecido de acordo com as regras do sistema Linux.

        Verifica se o caminho possui caracteres proibidos (como o caractere nulo)
        e se está em conformidade com a estrutura esperada definida pela regex.

        Args:
            caminho_entrada (str): Caminho a ser validado.

        Returns:
            ResultadoValidacao: Dicionário tipado contendo o resultado da validação,
            incluindo o caminho de entrada, o sistema identificado, validade e mensagem.
        """
        if "\0" in caminho_entrada:
            return cls.resultado(caminho_entrada, False, MENSAGENS["caracteres_proibidos"])

        if re.match(cls.CAMINHO_REGEX, caminho_entrada):
            return cls.resultado(caminho_entrada, True, MENSAGENS["caminho_valido"])

        return cls.resultado(caminho_entrada, False, MENSAGENS["caminho_invalido"])

    @staticmethod
    def resultado(caminho: str, valido: bool, mensagem: str) -> ResultadoValidacao:
        """
        Constrói o dicionário de resultado da validação com os dados fornecidos.

        Args:
            caminho (str): Caminho que foi validado.
            valido (bool): Indica se o caminho é válido ou não.
            mensagem (str): Mensagem explicativa sobre o resultado da validação.

        Returns:
            ResultadoValidacao: Resultado da validação em formato padronizado.
        """
        return {
            "caminho_entrada": caminho,
            "sistema": "Linux",
            "valido": valido,
            "mensagem": mensagem,
        }
