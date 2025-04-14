# -*- coding: utf-8 -*-
"""
Módulo central para a validação de caminhos de arquivos
conforme o sistema operacional identificado.

Este módulo define a classe `ValidadorCaminho`,
responsável por identificar o sistema operacional
a partir do caminho fornecido e delegar a validação
ao validador específico (Windows, Linux ou macOS).
"""

# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, line-too-long, import-error, no-else-return, too-few-public-methods  # noqa: E501

from models.identificador_sistema import identificar_sistema
from models.tipos_validacao import ResultadoValidacao
from models.validadores.validador_linux import ValidadorLinux
from models.validadores.validador_mac import ValidadorMac
from models.validadores.validador_windows import ValidadorWindows


class ValidadorCaminho:
    """
    Classe responsável por coordenar a validação de caminhos de arquivos,
    identificando o sistema operacional correspondente e utilizando o validador adequado.
    """

    def __init__(self):
        """
        Inicializa os validadores específicos para cada sistema operacional suportado.
        """
        self.validadores = {
            "Windows": ValidadorWindows(),
            "Linux": ValidadorLinux(),
            "Mac": ValidadorMac()
        }

    def validar_caminho(self, caminho_entrada: str) -> ResultadoValidacao:
        """
        Valida um caminho de arquivo ou diretório, identificando o sistema operacional
        com base no formato do caminho e utilizando o validador correspondente.

        Args:
            caminho_entrada (str): Caminho a ser validado.

        Returns:
            ResultadoValidacao: Dicionário tipado contendo o resultado da validação,
            incluindo o caminho de entrada, o sistema identificado, validade e mensagem.
        """
        caminho = caminho_entrada.strip()
        sistema = identificar_sistema(caminho)

        if not caminho:
            return {
                "caminho_entrada": caminho,
                "sistema": sistema,
                "valido": False,
                "mensagem": "O caminho está vazio."
            }

        validador = self.validadores.get(sistema)
        if validador:
            return validador.validar(caminho)
        else:
            return {
                "caminho_entrada": caminho,
                "sistema": sistema,
                "valido": False,
                "mensagem": "Formato de caminho desconhecido."
            }
