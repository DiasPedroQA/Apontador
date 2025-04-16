# -*- coding: utf-8 -*-

# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, line-too-long, no-else-return, import-error  # noqa: E501

"""
Módulo utilitário para inspeção completa de caminhos de arquivos e
diretórios usando o módulo pathlib de forma multiplataforma.
"""

import os
import platform
import tempfile
from pathlib import Path
import pytest


@pytest.mark.parametrize(
    "input_path",
    [
        "  ./  ",  # espaços
        ".",  # diretório atual
        str(Path(".")),  # Path obj convertido
    ],
)
def test_normalizar(input_path):
    resultado = InspecionadorCaminho.normalizar(input_path)
    assert isinstance(resultado, Path)
    assert resultado.is_absolute()


@pytest.mark.parametrize(
    "sistema_esperado, caminho",
    [
        (
            "Windows",
            (
                Path("C:/Users/Teste")
                if os.name == "nt"
                else pytest.param(
                    "skip",
                    Path("C:/Users/Teste"),
                    marks=pytest.mark.skip(reason="Somente para Windows"),
                )
            ),
        ),
        (
            "Linux",
            (
                Path("/home/user/teste")
                if os.name != "nt"
                else pytest.param(
                    "skip",
                    Path("/home/user/teste"),
                    marks=pytest.mark.skip(reason="Somente para Linux/Mac"),
                )
            ),
        ),
        ("Desconhecido", Path("algum\\caminho\\relativo")),
    ],
)
def test_identificar_sistema(sistema_esperado, caminho):
    sistema = InspecionadorCaminho.identificar_sistema(caminho)
    # sourcery skip: no-conditionals-in-tests
    if sistema_esperado != "skip":
        assert sistema == sistema_esperado


def test_inspecionar_com_arquivo_temporario():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = Path(tmp.name)

    resultado = InspecionadorCaminho.inspecionar(str(tmp_path))

    assert resultado["caminho_original"] == str(tmp_path)
    assert resultado["existe"] is True
    assert resultado["e_arquivo"] is True
    assert resultado["e_diretório"] is False
    assert resultado["nome"] == tmp_path.name
    assert resultado["pasta_mae"] == str(tmp_path.parent)
    assert resultado["sufixo"] == tmp_path.suffix
    assert resultado["sistema"] in {"Windows", "Linux", "Mac", "Desconhecido"}

    tmp_path.unlink()  # limpa o arquivo


def test_inspecionar_com_diretorio_temporario():
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        resultado = InspecionadorCaminho.inspecionar(str(tmp_path))

        assert resultado["existe"] is True
        assert resultado["e_arquivo"] is False
        assert resultado["e_diretório"] is True
        assert resultado["nome"] == tmp_path.name
        assert resultado["pasta_mae"] == str(tmp_path.parent)
        assert resultado["sufixo"] == ""
        assert resultado["sistema"] in {"Windows", "Linux", "Mac", "Desconhecido"}


def test_inspecionar_com_caminho_inexistente():
    caminho_falso = (
        "/caminho/que/nao/existe"
        if platform.system() != "Windows"
        else "Z:\\caminho\\inexistente"
    )
    resultado = InspecionadorCaminho.inspecionar(caminho_falso)

    assert resultado["existe"] is False
    assert resultado["e_arquivo"] is False
    assert resultado["e_diretório"] is False
    assert resultado["sistema"] in {"Windows", "Linux", "Mac", "Desconhecido"}
