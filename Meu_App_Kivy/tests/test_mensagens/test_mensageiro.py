import pytest
from app.mensagens.mensageiro import MENSAGENS

@pytest.mark.parametrize(
    "categoria,chave,esperado",
    [
        ("validação", "sistema_desconhecido", "Não foi possível identificar o sistema operacional a partir do caminho fornecido. Verifique se o formato está correto e se o sistema é suportado."),
        ("validação", "caminho_valido", "O caminho \"{caminho}\" é válido para o sistema operacional identificado e pode ser utilizado normalmente."),
        ("validação", "caminho_invalido", "O caminho \"{caminho}\" é inválido para o sistema operacional identificado. Corrija possíveis erros de formatação ou caracteres proibidos."),
        ("api", "sucesso", "Requisição processada com sucesso. Validação concluída."),
        ("api", "erro_404", "Recurso não encontrado."),
        ("interface", "botão_identificar", "Identificar"),
        ("logs", "inicio_validação", "Iniciando identificação do caminho."),
    ],
)
def test_mensagens_contem_chaves_e_valores_corretos(categoria, chave, esperado):
    """
    Testa se o dicionário MENSAGENS contém as categorias, chaves e valores esperados.
    """
    assert categoria in MENSAGENS, f"A categoria '{categoria}' não foi encontrada em MENSAGENS."
    assert chave in MENSAGENS[categoria], f"A chave '{chave}' não foi encontrada na categoria '{categoria}'."
    assert MENSAGENS[categoria][chave] == esperado, f"O valor da chave '{chave}' na categoria '{categoria}' não corresponde ao esperado."


def test_mensagens_estrutura_completa():
    """
    Testa se o dicionário MENSAGENS possui todas as categorias principais.
    """
    categorias_esperadas = {"validação", "api", "interface", "logs"}
    assert set(MENSAGENS.keys()) == categorias_esperadas, "As categorias principais de MENSAGENS não correspondem às esperadas."


def test_mensagens_validação_chaves():
    """
    Testa se todas as chaves dentro da categoria 'validação' possuem mensagens não vazias.
    """
    for chave, mensagem in MENSAGENS["validação"].items():
        assert isinstance(mensagem, str), f"A mensagem para a chave '{chave}' deve ser uma string."
        assert mensagem.strip(), f"A mensagem para a chave '{chave}' não pode estar vazia."


def test_mensagens_api_chaves():
    """
    Testa se todas as chaves dentro da categoria 'api' possuem mensagens não vazias.
    """
    for chave, mensagem in MENSAGENS["api"].items():
        assert isinstance(mensagem, str), f"A mensagem para a chave '{chave}' deve ser uma string."
        assert mensagem.strip(), f"A mensagem para a chave '{chave}' não pode estar vazia."


def test_mensagens_interface_chaves():
    """
    Testa se todas as chaves dentro da categoria 'interface' possuem mensagens não vazias.
    """
    for chave, mensagem in MENSAGENS["interface"].items():
        assert isinstance(mensagem, str), f"A mensagem para a chave '{chave}' deve ser uma string."
        assert mensagem.strip(), f"A mensagem para a chave '{chave}' não pode estar vazia."


def test_mensagens_logs_chaves():
    """
    Testa se todas as chaves dentro da categoria 'logs' possuem mensagens não vazias.
    """
    for chave, mensagem in MENSAGENS["logs"].items():
        assert isinstance(mensagem, str), f"A mensagem para a chave '{chave}' deve ser uma string."
        assert mensagem.strip(), f"A mensagem para a chave '{chave}' não pode estar vazia."