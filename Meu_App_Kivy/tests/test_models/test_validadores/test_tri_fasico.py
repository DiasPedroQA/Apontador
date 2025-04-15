import pytest
from app.models.identificadores.tri_fasico import IdentificadorMac, IdentificadorLinux, IdentificadorWindows

# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring


# Mock messages for testing
MENSAGENS = {
    "caracteres_proibidos": "O caminho contém caracteres proibidos.",
    "caminho_identifico": "O caminho é válido.",
    "caminho_identificado": "O caminho é inválido.",
}

@pytest.mark.parametrize(
    "identificador, caminho, esperado",
    [
        # Testes para IdentificadorMac
        (
            IdentificadorMac,
            "/Users/teste/arquivo.txt",
            {
                "identifico": True,
                "mensagem": MENSAGENS["caminho_identifico"]
            }
        ),
        (
            IdentificadorMac,
            "/Users/teste/arquivo:identificado.txt",
            {
                "identifico": False,
                "mensagem": MENSAGENS["caracteres_proibidos"]
            }
        ), (
            IdentificadorMac,
            "C:\\Users\\teste",
            {
                "identifico": False,
                "mensagem": MENSAGENS["caminho_identificado"]
            }
        ),
        
        # Testes para IdentificadorLinux
        (
            IdentificadorLinux,
            "/home/teste/arquivo.txt",
            {
                "identifico": True,
                "mensagem": MENSAGENS["caminho_identifico"]
            }
        ), (
            IdentificadorLinux,
            "/home/teste/arquivo\0identificado.txt",
            {
                "identifico": False,
                "mensagem": MENSAGENS["caracteres_proibidos"]
            }
        ), (
            IdentificadorLinux,
            "C:\\Users\\teste",
            {
                "identifico": False,
                "mensagem": MENSAGENS["caminho_identificado"]
            }
        ),

        # Testes para IdentificadorWindows
        (
            IdentificadorWindows,
            "C:\\Users\\teste\\arquivo.txt",
            {
                "identifico": True,
                "mensagem": MENSAGENS["caminho_identifico"]
            }
        ), (
            IdentificadorWindows,
            "C:\\Users\\teste\\arquivo<identificado>.txt",
            {
                "identifico": False,
                "mensagem": MENSAGENS["caracteres_proibidos"]
            }
        ), (
            IdentificadorWindows,
            "/home/teste/arquivo.txt",
            {
                "identifico": False,
                "mensagem": MENSAGENS["caminho_identificado"]
            }
        ),
    ],
)
def test_identificadores(
    identificador,
    caminho,
    esperado,
    monkeypatch
):
    # Mock MENSAGENS
    monkeypatch.setattr(
        "app.models.identificadores.tri_fasico.MENSAGENS",
        MENSAGENS
    )
    
    resultado = identificador.identificar(caminho)
    assert resultado["identifico"] == esperado["identifico"]
    assert resultado["mensagem"] == esperado["mensagem"]
