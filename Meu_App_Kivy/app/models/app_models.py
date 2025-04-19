# -*- coding: utf-8 -*-
# pylint: disable=E0401, C0413, C0115, C0116, R0903

"""
4. Model (app/models/)
Responsável pela lógica de negócio e regras de validação.

Contém funções especializadas como:

identificar_tipo_caminho(path) → Literal["arquivo", "pasta", "inválido"]

validar_caminho_arquivo(path) → dict

validar_caminho_pasta(path) → dict

comparar_tipo_sistema(caminho, sistema_atual) → bool

Cada função retorna um dicionário tipado (TypedDict) com:

Status (bool)

Tipo (str)

Mensagem técnica

Informações adicionais para exibição

A Model não conhece a View, nem formata mensagens para o usuário. Apenas analisa e retorna dados brutos ou estruturados.
"""

import os
import sys
from typing import Literal, TypedDict

# Garante que o diretório raiz esteja no sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.app_tools import Ogum  # noqa: E402
from mensagens.app_mensageiro import Exu  # noqa: E402  # Importa o mensageiro Exu


class InfoCaminho(TypedDict):
    caminho_original: str
    caminho_normalizado: str
    sistema: Literal["windows", "posix", "mac", "desconhecido"]
    valido: bool
    nome: str
    extensao: str
    diretorio_pai: str
    mensagem: str


class CaminhoSOModel:
    def __init__(self, caminho: str):
        self._caminho_original = caminho
        self._guia = Ogum()
        self._mensageiro = Exu()
        self._resultado = self._guia.validar(caminho)
        self._sistema = self._identificar_sistema()

    def _identificar_sistema(self) -> Literal["windows", "posix", "mac", "desconhecido"]:
        if ":" in self._caminho_original and "\\" in self._caminho_original:
            return "windows"
        elif self._caminho_original.startswith("/"):
            return "posix"
        return "desconhecido"

    @property
    def caminho_original(self) -> str:
        return self._caminho_original

    @property
    def caminho_normalizado(self) -> str:
        return self._resultado.get("caminho_normalizado", self._caminho_original)

    @property
    def sistema(self) -> Literal["windows", "posix", "mac", "desconhecido"]:
        return self._sistema

    @property
    def valido(self) -> bool:
        return self._resultado.get("valido", False)

    @property
    def nome(self) -> str:
        return self._guia.obter_nome_arquivo(self._caminho_original)

    @property
    def extensao(self) -> str:
        return self._guia.obter_metadados(self._caminho_original)["extensao"]

    @property
    def diretorio_pai(self) -> str:
        return 'self._guia.obter_diretorio_pai(self._caminho_original)'

    @property
    def mensagem(self) -> str:
        if not self._resultado.get("valido"):
            return self._mensageiro.caminho_invalido(self._caminho_original)
        if not self._resultado.get("existe"):
            return self._mensageiro.caminho_nao_encontrado(self._caminho_original)
        if self._resultado.get("permissao_negada"):
            return self._mensageiro.caminho_nao_permitido(self._caminho_original)
        if not self._resultado.get("legivel"):
            return self._mensageiro.caminho_nao_legivel(self._caminho_original)
        return self._mensageiro.caminho_legivel(self._caminho_original)

    def to_dict(self) -> InfoCaminho:
        return {
            "caminho_original": self.caminho_original,
            "caminho_normalizado": self.caminho_normalizado,
            "sistema": self.sistema,
            "valido": self.valido,
            "nome": self.nome,
            "extensao": self.extensao,
            "diretorio_pai": self.diretorio_pai,
            "mensagem": self.mensagem,
        }


if __name__ == "__main__":
    exemplos: list[str] = [
        "/home/pedro-pm-dias/arquivo_teste.txt",
        "/home/pedro-pm-dias/Downloads",
        "/etc/hosts",
        "C:\\Windows\\System32\\cmd.exe",
        "Z:\\caminho\\falso.txt",
    ]

    print("\n🧿 Resultado da modelagem com CaminhoSOModel\n" + "-" * 50)
    for exemplo in exemplos:
        modelo = CaminhoSOModel(exemplo)
        print("\n", modelo.to_dict())
