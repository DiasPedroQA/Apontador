import pytest
from unittest.mock import MagicMock
from app.models.identificador_sistema import IdentificadorCaminho, Identidade

@pytest.fixture
def identificador():
    """Fixture to create an instance of IdentificadorCaminho with a mocked ValidadorTriFasico."""
    identificador = IdentificadorCaminho()
    identificador.validador = MagicMock()
    return identificador

def test_identificar_sistema_windows(identificador):
    caminho = "C:\\Users\\User\\Documents\\file.txt"
    sistema = identificador.identificar_sistema(caminho)
    assert sistema == "Windows"

def test_identificar_sistema_mac(identificador):
    caminho = "/Users/User/Documents/file.txt"
    sistema = identificador.identificar_sistema(caminho)
    assert sistema == "Mac"

def test_identificar_sistema_linux(identificador):
    caminho = "/home/user/documents/file.txt"
    sistema = identificador.identificar_sistema(caminho)
    assert sistema == "Linux"

def test_identificar_sistema_desconhecido(identificador):
    caminho = "random_path_without_pattern"
    sistema = identificador.identificar_sistema(caminho)
    assert sistema == "desconhecido"

def test_identificar_caminho_valido(identificador):
    caminho = "/home/user/documents/file.txt"
    identificador.validador.validar.return_value = {
        "caminho_entrada": caminho,
        "sistema": "Linux",
        "identifico": True,
        "mensagem": "Caminho válido."
    }
    resultado = identificador.identificar_caminho(caminho)
    assert resultado["caminho_entrada"] == caminho
    assert resultado["sistema"] == "Linux"
    assert resultado["identifico"] is True
    assert resultado["mensagem"] == "Caminho válido."

def test_identificar_caminho_invalido(identificador):
    caminho = "/invalid/path"
    identificador.validador.validar.return_value = {
        "caminho_entrada": caminho,
        "sistema": "Linux",
        "identifico": False,
        "mensagem": "Caminho inválido."
    }
    resultado = identificador.identificar_caminho(caminho)
    assert resultado["caminho_entrada"] == caminho
    assert resultado["sistema"] == "Linux"
    assert resultado["identifico"] is False
    assert resultado["mensagem"] == "Caminho inválido."

def test_identificar_caminho_vazio(identificador):
    caminho = "   "
    resultado = identificador.identificar_caminho(caminho)
    assert resultado["caminho_entrada"] == ""
    assert resultado["sistema"] == "desconhecido"
    assert resultado["identifico"] is False
    assert resultado["mensagem"] == "O caminho está vazio."