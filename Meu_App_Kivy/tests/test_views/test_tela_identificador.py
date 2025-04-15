import pytest
from unittest.mock import MagicMock
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from app.view.tela_identificador import TelaIdentificador

# -*- coding: utf-8 -*-
"""
Testes para TelaIdentificador.

Este módulo contém os testes para a classe TelaIdentificador.
"""



@pytest.fixture
def mock_controller():
    """
    Fixture para criar um mock do CaminhoController.
    """
    controller = MagicMock()
    controller.identificar.return_value = {
        "caminho_entrada": "/path/to/file",
        "sistema": "Linux",
        "identifico": True,
        "mensagem": "Caminho válido."
    }
    return controller


@pytest.fixture
def tela_identificador(mock_controller):
    """
    Fixture para criar uma instância da TelaIdentificador com mocks.
    """
    tela = TelaIdentificador(controller=mock_controller)
    tela.ids = {
        "entrada_caminho": TextInput(),
        "resultado_label": Label()
    }
    return tela


def test_identificar_caminho_valido(tela_identificador, mock_controller):
    """
    Testa o método identificar_caminho com um caminho válido.
    """
    tela_identificador.ids["entrada_caminho"].text = "/path/to/file"
    tela_identificador.identificar_caminho()

    assert tela_identificador.ids["resultado_label"].text.startswith("[b]Caminho:[/b] /path/to/file")
    mock_controller.identificar.assert_called_once_with(caminho_entrada="/path/to/file")


def test_identificar_caminho_vazio(tela_identificador):
    """
    Testa o método identificar_caminho com um campo de entrada vazio.
    """
    tela_identificador.ids["entrada_caminho"].text = ""
    tela_identificador.identificar_caminho()

    assert "[b]Erro:[/b] O campo de entrada" in tela_identificador.ids["resultado_label"].text


def test_identificar_caminho_invalido(tela_identificador, mock_controller):
    """
    Testa o método identificar_caminho com um caminho inválido.
    """
    mock_controller.identificar.return_value = {
        "caminho_entrada": "/invalid/path",
        "sistema": "Linux",
        "identifico": False,
        "mensagem": "Caminho inválido."
    }
    tela_identificador.ids["entrada_caminho"].text = "/invalid/path"
    tela_identificador.identificar_caminho()

    assert "[b]Caminho:[/b] /invalid/path" in tela_identificador.ids["resultado_label"].text
    assert "[color=ff0000]Não[/color]" in tela_identificador.ids["resultado_label"].text
    mock_controller.identificar.assert_called_once_with(caminho_entrada="/invalid/path")