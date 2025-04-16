# -*- coding: utf-8 -*-
"""
    Testes para o módulo `caminho_controller`.
"""

from unittest.mock import MagicMock
import pytest
from app.controller.caminho_controller import CaminhoController
from app.mensagens.mensageiro import MENSAGENS


@pytest.fixture
def caminho_controller():
    """
    Fixture para instanciar o CaminhoController
    com um IdentificadorCaminho mockado.
    """
    controller = CaminhoController()
    controller.identificador = MagicMock()
    return controller


def test_identificar_caminho_vazio(caminho_controller):
    """
    Testa o caso em que o caminho de entrada está vazio.
    """
    caminho_entrada = ""
    resultado = caminho_controller.identificar_so(caminho_entrada)

    assert resultado["caminho_entrada"] == caminho_entrada
    assert resultado["sistema"] == "desconhecido"
    assert not resultado["identifico"]
    assert resultado["mensagem"] == MENSAGENS["validação"]["caminho_vazio"]


def test_identificar_caminho_valido(caminho_controller):
    """
    Testa o caso em que o caminho de entrada é válido.
    """
    caminho_entrada = "/caminho/valido"
    caminho_controller.identificador.identificar_caminho.return_value = {
        "caminho_entrada": caminho_entrada,
        "sistema": "linux",
        "identifico": True,
        "mensagem": "Caminho identificado com sucesso.",
    }

    resultado = caminho_controller.identificar_so(caminho_entrada)

    assert resultado["caminho_entrada"] == caminho_entrada
    assert resultado["sistema"] == "linux"
    assert resultado["identifico"]
    assert resultado["mensagem"] == "Caminho identificado com sucesso."


def test_identificar_caminho_invalido(caminho_controller):
    """
    Testa o caso em que o caminho de entrada é inválido.
    """
    caminho_entrada = "/caminho/invalido"
    caminho_controller.identificador.identificar_caminho.return_value = {
        "caminho_entrada": caminho_entrada,
        "sistema": "desconhecido",
        "identifico": False,
        "mensagem": "Caminho inválido.",
    }

    resultado = caminho_controller.identificar_so(caminho_entrada)

    assert resultado["caminho_entrada"] == caminho_entrada
    assert resultado["sistema"] == "desconhecido"
    assert not resultado["identifico"]
    assert resultado["mensagem"] == "Caminho inválido."
