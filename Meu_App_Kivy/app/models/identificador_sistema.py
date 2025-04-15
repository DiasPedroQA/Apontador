# -*- coding: utf-8 -*-
"""
Módulo de identificação de caminhos de arquivos
com base no sistema operacional identificado.

Este módulo define a classe `IdentificadorCaminho`,
que utiliza o validador central `ValidadorTriFasico`
para identificar e validar o caminho fornecido.
"""

import re
from typing import Literal, TypedDict
from app.models.validadores.tri_fasico import ValidadorTriFasico

# Tipos possíveis de sistema operacional
Sistema = Literal["Windows", "Linux", "Mac", "desconhecido"]

class Identidade(TypedDict):
    """
        Representa o resultado da identificação de um caminho.

        Atributos:
            caminho_entrada (str): Caminho informado pelo usuário.
            sistema (Sistema): Sistema operacional identificado.
            identifico (bool): Se o caminho é sintaticamente válido.
            mensagem (str): Explicação da identificação.
    """
    caminho_entrada: str
    sistema: Sistema
    identifico: bool
    mensagem: str


class IdentificadorCaminho:
    """
        Classe central para identificação de caminhos com base
        no sistema operacional inferido a partir do padrão do caminho.
    """

    def __init__(self):
        self.validador = ValidadorTriFasico()

    def identificar_sistema(self, caminho: str) -> Sistema:
        """
            Identifica o sistema operacional a partir do padrão do caminho.

            Args:
                caminho (str): Caminho a ser avaliado.

            Returns:
                Sistema: Literal representando o sistema inferido.
        """
        if re.match(r"^[a-zA-Z]:\\", caminho):
            return "Windows"
        elif re.match(r"^/(Users|Volumes|System/Volumes/Data)", caminho):
            return "Mac"
        elif re.match(r"^/(?!Users|Volumes|System/Volumes/Data)", caminho):
            return "Linux"
        return "desconhecido"

    def identificar_caminho(self, caminho_entrada: str) -> Identidade:
        """
            Identifica e valida o caminho utilizando o `ValidadorTriFasico`.

            Args:
                caminho_entrada (str): Caminho informado pelo usuário.

            Returns:
                Identidade: Resultado detalhado da identificação.
        """
        caminho = caminho_entrada.strip()
        sistema = self.identificar_sistema(caminho)

        if not caminho:
            return self._resultado(caminho, sistema, False, "O caminho está vazio.")

        resultado = self.validador.validar(caminho, sistema)
        return resultado

    def _resultado(
        self,
        caminho: str,
        sistema: Sistema,
        identifico: bool,
        mensagem: str
    ) -> Identidade:
        """
            Constrói um dicionário padronizado com os dados da identificação.

            Args:
                caminho (str): Caminho analisado.
                sistema (Sistema): Sistema identificado.
                identifico (bool): Resultado da validação.
                mensagem (str): Justificativa ou descrição.

            Returns:
                Identidade: Objeto tipado com os dados do processo.
        """
        return {
            "caminho_entrada": caminho,
            "sistema": sistema,
            "identifico": identifico,
            "mensagem": mensagem
        }
