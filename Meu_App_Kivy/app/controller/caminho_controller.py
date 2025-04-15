# -*- coding: utf-8 -*-
"""
    Módulo responsável por controlar a lógica de
    validação de caminhos de arquivos ou diretórios
    com base no sistema operacional identificado.

    Este módulo define a classe `CaminhoController`,
    que roteia o caminho informado para o validador
    adequado (Windows, Linux/POSIX ou macOS),
    retornando o resultado padronizado com base nas
    regras específicas de cada sistema.
"""

# pylint: disable=import-error, line-too-long, too-few-public-methods, too-many-ancestors, no-else-return  # noqa: E501

from mensagens.mensagens import MENSAGENS

from models.identificador_sistema import identificar_sistema

from models.tipos_validacao import ResultadoValidacao

from models.validadores import (
    validador_mac,
    validador_posix,
    validador_windows
)


class CaminhoController:
    """
        Classe responsável por validar caminhos de arquivos e diretórios
        em diferentes sistemas operacionais.
    """

    def validar(self, caminho_entrada: str) -> ResultadoValidacao:
        """
            Valida o caminho de entrada com base no
            sistema operacional identificado.

            A função utiliza identificadores e validadores
            específicos para os sistemas Windows,
            Linux (POSIX) e macOS, retornando um dicionário
            com o resultado.

            Args:
                caminho_entrada (str): Caminho do sistema
                de arquivos a ser analisado.

            Returns:
                ResultadoValidacao: Dicionário contendo
                o caminho analisado, o sistema operacional
                identificado, se o caminho é válido,
                e uma mensagem associada ao resultado.
        """
        sistema = identificar_sistema(caminho_entrada)

        if sistema == "Windows":
            return validador_windows.validar(caminho_entrada)
        elif sistema == "Linux":
            return validador_posix.validar(caminho_entrada)
        elif sistema == "Mac":
            return validador_mac.validar(caminho_entrada)
        else:
            return {
                "caminho_entrada": str(caminho_entrada),
                "sistema": "desconhecido",
                "valido": False,
                "mensagem": MENSAGENS["sistema_desconhecido"]
            }
