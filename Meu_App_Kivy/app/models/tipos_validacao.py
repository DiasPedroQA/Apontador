# pylint: disable=line-too-long, missing-module-docstring,

# -*- coding: utf-8 -*-

from typing import TypedDict


class ResultadoValidacao(TypedDict):
    """
        Representa o resultado de uma validação de caminho
        de arquivo/diretório.
    """
    caminho_entrada: str       # Caminho informado pelo usuário
    sistema: str               # Sistema identificado (Windows, Mac, Linux, etc.)
    valido: bool               # Indica se o caminho é sintaticamente válido
    mensagem: str              # Mensagem explicativa do resultado da validação
