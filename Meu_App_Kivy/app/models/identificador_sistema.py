# -*- coding: utf-8 -*-

"""
    validador_caminho.py

    Módulo unificado para validação de caminhos
    de arquivos ou diretórios.

    Este módulo oferece uma estrutura centralizada para:
        - Identificar o sistema operacional
        com base no formato do caminho;
        - Validar o caminho conforme as
        regras sintáticas do sistema
        operacional identificado;
        - Retornar um objeto estruturado
        contendo os resultados da análise.

    Classes:
        - ValidadorCaminho: Classe com
        funcionalidades integradas de identificação
        e validação de caminhos para
        Windows, Linux e macOS.

    Tipos:
        - Sistema: Literal para identificar
        sistemas conhecidos.
        - ResultadoValidacao: TypedDict com
        resultado da validação.
"""

# pylint: disable=no-else-return,  # noqa: E501

import re
from typing import Literal, TypedDict

Sistema = Literal["Windows", "Linux", "Mac", "desconhecido"]


class ResultadoValidacao(TypedDict):
    """
    Representa o resultado de uma validação de caminho.

    Atributos:
        caminho_entrada (str): Caminho informado pelo usuário.
        sistema (Sistema): Sistema operacional identificado.
        valido (bool): Se o caminho é sintaticamente válido.
        mensagem (str): Explicação da validação.
    """
    caminho_entrada: str
    sistema: Sistema
    valido: bool
    mensagem: str


class ValidadorCaminho:
    """
    Classe responsável por identificar o sistema e validar caminhos
    conforme regras específicas de cada sistema operacional.
    """

    def __init__(self):
        self.regex_windows = (
            r"^[a-zA-Z]:\\(?:[^\\/:*?\"<>|\r\n]+\\)*[^\\/:*?\"<>|\r\n]*$"
        )
        self.regex_mac = r"^/([a-zA-Z0-9._ -]+/?)*$"
        self.regex_linux = r"^/([a-zA-Z0-9._-]+/?)*$"
        self.caracteres_proibidos_windows = r'[<>:"/\\|?*]'
        self.caracteres_proibidos_linux = r'\0'
        self.caracteres_proibidos_mac = r':'

    def identificar_sistema(self, caminho_entrada: str) -> Sistema:
        """
        Identifica o sistema operacional com base no formato do caminho.

        Args:
            caminho_entrada (str): Caminho de arquivo ou diretório a ser analisado.

        Returns:
            Sistema: Um dos seguintes valores:
                - "Windows": Se o caminho for do Windows.
                - "Linux": Se o caminho for do Linux.
                - "Mac": Se o caminho for do macOS.
                - "desconhecido": Se o sistema não puder ser identificado.
        """
        if re.match(r"^[a-zA-Z]:\\", caminho_entrada):
            return "Windows"
        elif re.match(r"^/(Users|Volumes|System/Volumes/Data)", caminho_entrada):
            return "Mac"
        elif re.match(r"^/(?!Users|Volumes|System/Volumes/Data)", caminho_entrada):
            return "Linux"
        return "desconhecido"

    def validar_caminho(self, caminho_entrada: str) -> ResultadoValidacao:
        """
        Valida um caminho de acordo com o sistema operacional detectado.

        Args:
            caminho_entrada (str): Caminho informado.

        Returns:
            ResultadoValidacao: Estrutura com detalhes da validação.
        """
        caminho = caminho_entrada.strip()
        sistema = self.identificar_sistema(caminho)

        if not caminho:
            return self._resultado(
                caminho, sistema, False, "O caminho está vazio."
            )

        if sistema == "Windows":
            return self._validar_windows(caminho)
        elif sistema == "Mac":
            return self._validar_mac(caminho)
        elif sistema == "Linux":
            return self._validar_linux(caminho)
        else:
            return self._resultado(
                caminho, sistema, False, "Formato de caminho desconhecido."
            )

    def _validar_windows(self, caminho_entrada: str) -> ResultadoValidacao:
        """
        Valida um caminho específico para Windows.

        Args:
            caminho_entrada (str): Caminho de arquivo ou diretório a ser validado.

        Returns:
            ResultadoValidacao: Resultado da validação.
        """
        if re.search(self.caracteres_proibidos_windows, caminho_entrada):
            return self._resultado(
                caminho_entrada,
                "Windows",
                False,
                "Caminho contém caracteres proibidos."
            )

        if re.match(self.regex_windows, caminho_entrada):
            return self._resultado(
                caminho_entrada, "Windows", True, "Caminho válido."
            )

        return self._resultado(
            caminho_entrada, "Windows", False, "Caminho inválido."
        )

    def _validar_mac(self, caminho_entrada: str) -> ResultadoValidacao:
        """
        Valida um caminho específico para macOS.

        Args:
            caminho_entrada (str): Caminho de arquivo ou diretório a ser validado.

        Returns:
            ResultadoValidacao: Resultado da validação.
        """
        if re.search(self.caracteres_proibidos_mac, caminho_entrada):
            return self._resultado(
                caminho_entrada,
                "Mac",
                False,
                "Caminho contém caracteres proibidos."
            )

        if re.match(self.regex_mac, caminho_entrada):
            return self._resultado(
                caminho_entrada, "Mac", True, "Caminho válido."
            )

        return self._resultado(
            caminho_entrada, "Mac", False, "Caminho inválido."
        )

    def _validar_linux(self, caminho_entrada: str) -> ResultadoValidacao:
        """
        Valida um caminho específico para Linux.

        Args:
            caminho_entrada (str): Caminho de arquivo ou diretório a ser validado.

        Returns:
            ResultadoValidacao: Resultado da validação.
        """
        if re.search(self.caracteres_proibidos_linux, caminho_entrada):
            return self._resultado(
                caminho_entrada,
                "Linux",
                False,
                "Caminho contém caracteres proibidos."
            )

        if re.match(self.regex_linux, caminho_entrada):
            return self._resultado(
                caminho_entrada, "Linux", True, "Caminho válido."
            )

        return self._resultado(
            caminho_entrada, "Linux", False, "Caminho inválido."
        )

    def _resultado(
        self,
        caminho: str,
        sistema: Sistema,
        valido: bool,
        mensagem: str
    ) -> ResultadoValidacao:
        """
        Gera a estrutura padronizada de resultado de validação.

        Args:
            caminho (str): Caminho informado.
            sistema (Sistema): Sistema identificado.
            valido (bool): Resultado da validação.
            mensagem (str): Explicação.

        Returns:
            ResultadoValidacao: Resultado estruturado.
        """
        return {
            "caminho_entrada": caminho,
            "sistema": sistema,
            "valido": valido,
            "mensagem": mensagem
        }
