# -*- coding: utf-8 -*-
"""
Validador de caminhos de arquivos para sistemas Windows.

Este módulo define a classe `ValidadorWindows`, que realiza a validação sintática
de caminhos com base nas regras do sistema operacional Windows. Ele verifica se o caminho
segue o formato esperado e se não contém caracteres proibidos pelo sistema.
"""

# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, line-too-long, import-error  # noqa: E501

import re

from mensagens.mensagens import MENSAGENS
from models.tipos_validacao import ResultadoValidacao


class ValidadorWindows:
    """
    Classe responsável por validar caminhos de arquivos em sistemas Windows.

    A validação considera a estrutura padrão de caminhos no Windows, incluindo unidade
    (como 'C:\\') e separadores de diretórios com barras invertidas, além de garantir que
    não haja caracteres inválidos como `<>:"/\\|?*`.
    """

    CAMINHO_REGEX = r"^[a-zA-Z]:\\(?:[^\\/:*?\"<>|\r\n]+\\)*[^\\/:*?\"<>|\r\n]*$"
    CARACTERES_PROIBIDOS = r'[<>:"/\\|?*]'

    @classmethod
    def validar(cls, caminho_entrada: str) -> ResultadoValidacao:
        """
        Valida o caminho fornecido conforme as regras do sistema Windows.

        Verifica se o caminho contém caracteres proibidos ou se está em conformidade
        com a estrutura esperada por meio de expressões regulares.

        Args:
            caminho_entrada (str): Caminho de arquivo a ser validado.

        Returns:
            ResultadoValidacao: Estrutura tipada contendo o caminho original,
            o sistema identificado, se é válido ou não e uma mensagem descritiva.
        """
        if re.search(cls.CARACTERES_PROIBIDOS, caminho_entrada):
            return cls.resultado(caminho_entrada, False, MENSAGENS["caracteres_proibidos"])

        if re.match(cls.CAMINHO_REGEX, caminho_entrada):
            return cls.resultado(caminho_entrada, True, MENSAGENS["caminho_valido"])

        return cls.resultado(caminho_entrada, False, MENSAGENS["caminho_invalido"])

    @staticmethod
    def resultado(caminho: str, valido: bool, mensagem: str) -> ResultadoValidacao:
        """
        Gera o resultado padronizado da validação do caminho.

        Args:
            caminho (str): Caminho validado.
            valido (bool): Indica se o caminho é válido ou não.
            mensagem (str): Mensagem associada ao resultado da validação.

        Returns:
            ResultadoValidacao: Dicionário contendo os detalhes da validação.
        """
        return {
            "caminho_entrada": caminho,
            "sistema": "Windows",
            "valido": valido,
            "mensagem": mensagem,
        }
