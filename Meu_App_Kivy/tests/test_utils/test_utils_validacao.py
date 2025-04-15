import pytest
from pathlib import Path
from app.utils.utils_validacao import (
    InspecionadorCaminho,
    DadosCaminho
)

# -*- coding: utf-8 -*-



@pytest.mark.parametrize(
    "caminho_entrada, esperado",
    [
        (
            "/tmp/teste.txt",
            {
                "existe": False,
                "e_arquivo": False,
                "e_diretório": False,
                "sistema": "Linux"
            }
        ),
        (
            "C:\\Windows\\System32",
            {
                "existe": Path("C:\\Windows\\System32").exists(),
                "e_arquivo": False,
                "e_diretório": True,
                "sistema": "Windows"
            }
        ),
        (
            "/home/user",
            {
                "existe": Path("/home/user").exists(),
                "e_arquivo": False,
                "e_diretório": True,
                "sistema": "Linux"
            }
        ),
        (
            "invalid_path",
            {
                "existe": False,
                "e_arquivo": False,
                "e_diretório": False,
                "sistema": "Desconhecido"
            }
        ),
    ],
)
def test_inspecionar(caminho_entrada, esperado):
    resultado = InspecionadorCaminho.inspecionar(caminho_entrada)

    assert resultado["caminho_original"] == caminho_entrada
    assert resultado["caminho_normalizado"] == str(
        Path(caminho_entrada).resolve()
    )
    assert resultado["existe"] == esperado["existe"]
    assert resultado["e_arquivo"] == esperado["e_arquivo"]
    assert resultado["e_diretório"] == esperado["e_diretório"]
    assert resultado["sistema"] == esperado["sistema"]
    assert isinstance(resultado["nome"], str)
    assert isinstance(resultado["pasta_mae"], str)
    assert isinstance(resultado["sufixo"], str)


def test_normalizar():
    caminho = "  /tmp/teste.txt  "
    resultado = InspecionadorCaminho.normalizar(caminho)
    assert resultado == Path("/tmp/teste.txt").resolve()


@pytest.mark.parametrize(
    "caminho, sistema_esperado",
    [
        (Path("C:\\Windows\\System32"), "Windows"),
        (Path("/home/user"), "Linux"),
        (Path("invalid_path"), "Desconhecido"),
    ],
)
def test_identificar_sistema(caminho, sistema_esperado):
    resultado = InspecionadorCaminho.identificar_sistema(caminho)
    assert resultado == sistema_esperado