import pytest
from unittest.mock import patch
from app.models.validadores.tri_fasico import ValidadorTriFasico
from app.mensagens.mensageiro import MENSAGENS

# -*- coding: utf-8 -*-
# pylint: disable=import-error, line-too-long, too-few-public-methods, no-else-return  # noqa: E501


def test_identificar_windows(MENSAGENS):
    caminho = "C:\\Users\\User\\Documents\\file.txt"
    resultado = ValidadorTriFasico.identificar_so(caminho)
    assert resultado["caminho_entrada"] == caminho
    assert resultado["sistema_operacional"] == "Windows"
    assert resultado["identificado"] is True
    assert resultado["mensagem"] == MENSAGENS["validação"]["caminho_identificado"].format(caminho=caminho)

def test_identificar_linux(MENSAGENS):
    caminho = "/home/user/documents/file.txt"
    resultado = ValidadorTriFasico.identificar_so(caminho)
    assert resultado["caminho_entrada"] == caminho
    assert resultado["sistema_operacional"] == "Linux"
    assert resultado["identificado"] is True
    assert resultado["mensagem"] == MENSAGENS["validação"]["caminho_identificado"].format(caminho=caminho)


def test_identificar_mac(MENSAGENS):
    caminho = "/Users/user/Documents/file.txt"
    resultado = ValidadorTriFasico.identificar_so(caminho)
    assert resultado["caminho_entrada"] == caminho
    assert resultado["sistema_operacional"] == "Mac"
    assert resultado["identificado"] is True
    assert resultado["mensagem"] == MENSAGENS["validação"]["caminho_identificado"].format(caminho=caminho)


def test_identificar_caracteres_proibidos(MENSAGENS):
    caminho = "C:\\Users\\User\\Documents\\file<.txt"
    resultado = ValidadorTriFasico.identificar_so(caminho)
    assert resultado["caminho_entrada"] == caminho
    assert resultado["sistema_operacional"] == "Windows"
    assert resultado["identificado"] is False
    assert resultado["mensagem"] == MENSAGENS["validação"]["caracteres_proibidos"].format(caminho=caminho)


def test_identificar_sistema_desconhecido(MENSAGENS):
    caminho = "invalid_path"
    resultado = ValidadorTriFasico.identificar_so(caminho)
    assert resultado["caminho_entrada"] == caminho
    assert resultado["sistema_operacional"] == "Desconhecido"
    assert resultado["identificado"] is False
    assert resultado["mensagem"] == MENSAGENS["validação"]["sistema_desconhecido"].format(caminho=caminho)
