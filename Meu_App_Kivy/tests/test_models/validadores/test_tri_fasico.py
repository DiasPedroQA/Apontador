import pytest
from unittest.mock import patch
from app.models.validadores.tri_fasico import ValidadorTriFasico

# -*- coding: utf-8 -*-
# pylint: disable=import-error, line-too-long, too-few-public-methods, no-else-return  # noqa: E501


@pytest.fixture
def mensagens_mock():
    return {
        "validação": {
            "caracteres_proibidos": "O caminho '{caminho}' contém caracteres proibidos.",
            "caminho_identificado": "O caminho '{caminho}' foi identificado com sucesso.",
            "sistema_desconhecido": "O caminho '{caminho}' não corresponde a nenhum sistema operacional conhecido.",
        }
    }

@patch("app.models.validadores.tri_fasico.MENSAGENS", new_callable=lambda: mensagens_mock())
def test_identificar_windows(mock_mensagens):
    caminho = "C:\\Users\\User\\Documents\\file.txt"
    resultado = ValidadorTriFasico.identificar(caminho)
    assert resultado["caminho_entrada"] == caminho
    assert resultado["sistema_operacional"] == "Windows"
    assert resultado["identificado"] is True
    assert resultado["mensagem"] == mock_mensagens["validação"]["caminho_identificado"].format(caminho=caminho)

@patch("app.models.validadores.tri_fasico.MENSAGENS", new_callable=lambda: mensagens_mock())
def test_identificar_linux(mock_mensagens):
    caminho = "/home/user/documents/file.txt"
    resultado = ValidadorTriFasico.identificar(caminho)
    assert resultado["caminho_entrada"] == caminho
    assert resultado["sistema_operacional"] == "Linux"
    assert resultado["identificado"] is True
    assert resultado["mensagem"] == mock_mensagens["validação"]["caminho_identificado"].format(caminho=caminho)

@patch("app.models.validadores.tri_fasico.MENSAGENS", new_callable=lambda: mensagens_mock())
def test_identificar_mac(mock_mensagens):
    caminho = "/Users/user/Documents/file.txt"
    resultado = ValidadorTriFasico.identificar(caminho)
    assert resultado["caminho_entrada"] == caminho
    assert resultado["sistema_operacional"] == "Mac"
    assert resultado["identificado"] is True
    assert resultado["mensagem"] == mock_mensagens["validação"]["caminho_identificado"].format(caminho=caminho)

@patch("app.models.validadores.tri_fasico.MENSAGENS", new_callable=lambda: mensagens_mock())
def test_identificar_caracteres_proibidos(mock_mensagens):
    caminho = "C:\\Users\\User\\Documents\\file<.txt"
    resultado = ValidadorTriFasico.identificar(caminho)
    assert resultado["caminho_entrada"] == caminho
    assert resultado["sistema_operacional"] == "Windows"
    assert resultado["identificado"] is False
    assert resultado["mensagem"] == mock_mensagens["validação"]["caracteres_proibidos"].format(caminho=caminho)

@patch("app.models.validadores.tri_fasico.MENSAGENS", new_callable=lambda: mensagens_mock())
def test_identificar_sistema_desconhecido(mock_mensagens):
    caminho = "invalid_path"
    resultado = ValidadorTriFasico.identificar(caminho)
    assert resultado["caminho_entrada"] == caminho
    assert resultado["sistema_operacional"] == "Desconhecido"
    assert resultado["identificado"] is False
    assert resultado["mensagem"] == mock_mensagens["validação"]["sistema_desconhecido"].format(caminho=caminho)