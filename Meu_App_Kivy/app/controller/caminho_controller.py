# -*- coding: utf-8 -*-
"""
    Módulo responsável por controlar a lógica de
    identificação de caminhos de arquivos ou diretórios,
    com base no sistema operacional identificado.

    Este módulo define a classe `CaminhoController`,
    que utiliza o `IdentificadorCaminho` para identificar
    e validar caminhos, retornando um resultado padronizado.
"""

# pylint: disable=import-error, line-too-long, too-few-public-methods, no-else-return  # noqa: E501

from app.mensagens.mensageiro import MENSAGENS
from app.models.identificador_sistema import (
    IdentificadorCaminho,
    Identidade
)


class CaminhoController:
    """
        Classe responsável por controlar a identificação de caminhos de
        arquivos e diretórios em diferentes sistemas operacionais.
    """

    def __init__(self) -> None:
        self.identificador = IdentificadorCaminho()

    def identificar_so(self, caminho_entrada: str) -> Identidade:
        """
            Identifica e valida um caminho informado, retornando os dados
            padronizados de identificação.

            Args:
                caminho_entrada (str): Caminho do sistema de arquivos a ser analisado.

            Returns:
                Identidade: Dicionário contendo o caminho analisado, o sistema
                identificado, a validade e a mensagem associada.
        """
        if not caminho_entrada.strip():
            return {
                "caminho_entrada": caminho_entrada,
                "sistema": "desconhecido",
                "identifico": False,
                "mensagem": MENSAGENS["validação"]["caminho_vazio"]
            }

        return self.identificador.identificar_caminho(caminho_entrada)
