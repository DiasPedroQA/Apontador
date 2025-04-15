# -*- coding: utf-8 -*-
# pylint: disable=line-too-long, missing-module-docstring

import re
from abc import ABC, abstractmethod
from typing import TypedDict

from mensagens.mensagens import MENSAGENS


class ResultadoValidacao(TypedDict):
    """
    Representa o resultado de uma validação de caminho de arquivo/diretório.
    """
    caminho_entrada: str  # Caminho informado pelo usuário
    sistema: str          # Sistema identificado (Windows, Mac, Linux, etc.)
    valido: bool          # Indica se o caminho é sintaticamente válido
    mensagem: str         # Mensagem explicativa do resultado da validação


class ValidadorSistemaBase(ABC):
    """
    Classe base abstrata para validadores de caminhos por sistema operacional.
    Cada classe filha deve definir:
    - Nome do sistema (`NOME_SISTEMA`)
    - Regex de validação de caminhos (`REGEX_CAMINHO`)
    - Caracteres proibidos (`CARACTERES_PROIBIDOS`)
    """

    NOME_SISTEMA: str
    REGEX_CAMINHO: str
    CARACTERES_PROIBIDOS: str = ""

    @classmethod
    def validar(cls, caminho: str) -> ResultadoValidacao:
        """
        Valida um caminho com base nas regras do sistema específico.

        1. Verifica caracteres proibidos.
        2. Verifica correspondência com a regex do sistema.
        3. Retorna mensagem adequada com o resultado.

        Args:
            caminho (str): Caminho a ser validado.

        Returns:
            ResultadoValidacao: Resultado com informações da validação.
        """
        if any(char in caminho for char in cls.CARACTERES_PROIBIDOS):
            return cls._resultado(caminho, False, MENSAGENS["caracteres_proibidos"])

        if re.match(cls.REGEX_CAMINHO, caminho):
            return cls._resultado(caminho, True, MENSAGENS["caminho_valido"])

        return cls._resultado(caminho, False, MENSAGENS["caminho_invalido"])

    @classmethod
    def _resultado(cls, caminho: str, valido: bool, mensagem: str) -> ResultadoValidacao:
        """
        Monta o dicionário do resultado da validação.
        """
        return {
            "caminho_entrada": caminho,
            "sistema": cls.NOME_SISTEMA,
            "valido": valido,
            "mensagem": mensagem,
        }


class ValidadorMac(ValidadorSistemaBase):
    """
    Validador de caminhos para o sistema macOS.
    """
    NOME_SISTEMA = "Mac"
    REGEX_CAMINHO = r"^/([a-zA-Z0-9._ -]+/?)*$"
    CARACTERES_PROIBIDOS = ":"


class ValidadorLinux(ValidadorSistemaBase):
    """
    Validador de caminhos para o sistema Linux.
    """
    NOME_SISTEMA = "Linux"
    REGEX_CAMINHO = r"^/([a-zA-Z0-9._-]+/?)*$"
    CARACTERES_PROIBIDOS = "\0"  # NULL byte


class ValidadorWindows(ValidadorSistemaBase):
    """
    Validador de caminhos para o sistema Windows.
    """
    NOME_SISTEMA = "Windows"
    REGEX_CAMINHO = r"^[a-zA-Z]:\\(?:[^\\/:*?\"<>|\r\n]+\\)*[^\\/:*?\"<>|\r\n]*$"
    CARACTERES_PROIBIDOS = '<>:"/\\|?*'
