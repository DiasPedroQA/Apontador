import pytest
from app.models.validadores.tri_fasico import ValidadorMac, ValidadorLinux, ValidadorWindows

# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring


# Mock messages for testing
MENSAGENS = {
    "caracteres_proibidos": "O caminho contém caracteres proibidos.",
    "caminho_valido": "O caminho é válido.",
    "caminho_invalido": "O caminho é inválido.",
}

@pytest.mark.parametrize(
    "validador, caminho, esperado",
    [
        # Testes para ValidadorMac
        (ValidadorMac, "/Users/teste/arquivo.txt", {"valido": True, "mensagem": MENSAGENS["caminho_valido"]}),
        (ValidadorMac, "/Users/teste/arquivo:invalido.txt", {"valido": False, "mensagem": MENSAGENS["caracteres_proibidos"]}),
        (ValidadorMac, "C:\\Users\\teste", {"valido": False, "mensagem": MENSAGENS["caminho_invalido"]}),
        
        # Testes para ValidadorLinux
        (ValidadorLinux, "/home/teste/arquivo.txt", {"valido": True, "mensagem": MENSAGENS["caminho_valido"]}),
        (ValidadorLinux, "/home/teste/arquivo\0invalido.txt", {"valido": False, "mensagem": MENSAGENS["caracteres_proibidos"]}),
        (ValidadorLinux, "C:\\Users\\teste", {"valido": False, "mensagem": MENSAGENS["caminho_invalido"]}),
        
        # Testes para ValidadorWindows
        (ValidadorWindows, "C:\\Users\\teste\\arquivo.txt", {"valido": True, "mensagem": MENSAGENS["caminho_valido"]}),
        (ValidadorWindows, "C:\\Users\\teste\\arquivo<invalido>.txt", {"valido": False, "mensagem": MENSAGENS["caracteres_proibidos"]}),
        (ValidadorWindows, "/home/teste/arquivo.txt", {"valido": False, "mensagem": MENSAGENS["caminho_invalido"]}),
    ],
)
def test_validadores(validador, caminho, esperado, monkeypatch):
    # Mock MENSAGENS
    monkeypatch.setattr("app.models.validadores.tri_fasico.MENSAGENS", MENSAGENS)
    
    resultado = validador.validar(caminho)
    assert resultado["valido"] == esperado["valido"]
    assert resultado["mensagem"] == esperado["mensagem"]