# -*- coding: utf-8 -*-
"""
Módulo responsável pela validação de caminhos de arquivos no sistema operacional macOS.

Este módulo define a classe `ValidadorMac`, que herda de `ValidadorSistemaBase`, e implementa
a lógica de validação sintática de caminhos conforme as regras do macOS. A validação considera
caracteres proibidos e o formato geral esperado para caminhos neste sistema.
"""

# pylint: disable=import-error  # noqa: E501

import re

from mensagens.mensagens import MENSAGENS

from models.tipos_validacao import ResultadoValidacao

from models.validador_base import ValidadorSistemaBase

CAMINHO_REGEX = r"^/([a-zA-Z0-9._ -]+/?)*$"


class ValidadorMac(ValidadorSistemaBase):
    """
    Validador de caminhos para o sistema operacional macOS.

    Verifica se o caminho fornecido está de acordo com as convenções do macOS,
    como ausência de caracteres proibidos (por exemplo, dois-pontos) e se o
    formato geral do caminho é válido conforme expressão regular definida.
    """

    def validar(self, caminho_entrada: str) -> ResultadoValidacao:
        """
        Valida o caminho fornecido conforme as regras do sistema macOS.

        Args:
            caminho_entrada (str): Caminho de arquivo ou diretório a ser validado.

        Returns:
            ResultadoValidacao: Dicionário tipado contendo o resultado da validação,
            incluindo o caminho de entrada, sistema identificado, validade e mensagem.
        """
        if ":" in caminho_entrada:
            return self.resultado(caminho_entrada, False, MENSAGENS["caracteres_proibidos"])

        if re.match(CAMINHO_REGEX, caminho_entrada):
            return self.resultado(caminho_entrada, True, MENSAGENS["caminho_valido"])

        return self.resultado(caminho_entrada, False, MENSAGENS["caminho_invalido"])

    def resultado(self, caminho: str, valido: bool, mensagem: str) -> ResultadoValidacao:
        """
        Gera o dicionário de resultado da validação para o sistema macOS.

        Args:
            caminho (str): Caminho fornecido pelo usuário.
            valido (bool): Indicador se o caminho é válido.
            mensagem (str): Mensagem descritiva do resultado.

        Returns:
            ResultadoValidacao: Dicionário tipado com os dados da validação.
        """
        return {
            "caminho_entrada": caminho,
            "sistema": "Mac",
            "valido": valido,
            "mensagem": mensagem
        }
