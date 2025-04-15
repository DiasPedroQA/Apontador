# tests/test_mensagens.py

from app.mensagens.mensageiro import MENSAGENS

# Testando as mensagens de identificação
def test_mensagens_identificacao_existem():
    chaves_esperadas = [
        "sistema_desconhecido",
        "caminho_identifico",
        "caminho_identificado",
        "caracteres_proibidos",
        "caminho_nao_encontrado",
        "permissao_negada",
        "caminho_muito_longo",
        "diretorio_nao_existe",
        "arquivo_nao_existe",
        "caminho_reservado",
        "formato_identificado",
        "caminho_vazio", 
        "caminho_relativo",
        "caminho_inacessivel",
        "caminho_nao_especificado"
    ]
    for chave in chaves_esperadas:
        assert chave in MENSAGENS["identificacao"]
        assert isinstance(MENSAGENS["identificacao"][chave], str)

# Testando as mensagens de API
def test_mensagens_api_existem():
    chaves_esperadas = ["erro_404", "erro_500", "sucesso"]
    for chave in chaves_esperadas:
        assert chave in MENSAGENS["api"]
        assert isinstance(MENSAGENS["api"][chave], str)

# Testando as mensagens de interface
def test_mensagens_interface_existem():
    chaves_esperadas = [
        "botao_identificar",
        "campo_placeholder",
        "titulo"
    ]
    for chave in chaves_esperadas:
        assert chave in MENSAGENS["interface"]
        assert isinstance(MENSAGENS["interface"][chave], str)

# Testando as mensagens de logs
def test_mensagens_logs_existem():
    chaves_esperadas = [
        "inicio_identificacao",
        "fim_identificacao",
        "erro_identificacao"
    ]
    for chave in chaves_esperadas:
        assert chave in MENSAGENS["logs"]
        assert isinstance(MENSAGENS["logs"][chave], str)
