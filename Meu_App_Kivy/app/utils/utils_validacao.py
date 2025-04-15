# -*- coding: utf-8 -*-

# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, line-too-long, no-else-return, import-error  # noqa: E501

# -*- coding: utf-8 -*-

"""
Módulo utilitário para inspeção completa de caminhos de arquivos e diretórios
usando o módulo pathlib de forma multiplataforma.
"""

from pathlib import Path
from typing import Union, TypedDict


class DadosCaminho(TypedDict):
    caminho_original: str
    caminho_normalizado: str
    existe: bool
    e_arquivo: bool
    e_diretorio: bool
    nome: str
    pasta_mae: str
    sufixo: str
    sistema: str


class InspecionadorCaminho:
    """
    Classe responsável por analisar e extrair informações de um caminho
    utilizando pathlib, com suporte a arquivos e diretórios.
    """

    @staticmethod
    def normalizar(caminho: Union[str, Path]) -> Path:
        return Path(str(caminho).strip()).resolve()

    @staticmethod
    def identificar_sistema(path: Path) -> str:
        if path.drive:
            return "Windows"
        if str(path).startswith("/"):
            return "Linux" if ":" not in str(path) else "Mac"
        return "Desconhecido"

    @classmethod
    def inspecionar(cls, caminho_entrada: str) -> DadosCaminho:
        caminho = cls.normalizar(caminho_entrada)

        return {
            "caminho_original": caminho_entrada,
            "caminho_normalizado": str(caminho),
            "existe": caminho.exists(),
            "e_arquivo": caminho.is_file(),
            "e_diretório": caminho.is_dir(),
            "nome": caminho.name,
            "pasta_mae": str(caminho.parent),
            "sufixo": caminho.suffix,
            "sistema": cls.identificar_sistema(caminho)
        }
