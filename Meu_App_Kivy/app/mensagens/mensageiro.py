# pylint disable: line-too-long
# flake8: noqa E501
# app/mensagens/mensagens.py

"""
    Este módulo define um dicionário chamado `MENSAGENS`
    que contém mensagens relacionadas à validação de caminhos de arquivos e diretórios.
    As mensagens cobrem uma ampla gama de cenários, como:
    - Caminhos inválidos ou não encontrados.
    - Problemas de permissões e formatos inválidos.
    - Mensagens de erro para interação com o sistema e o usuário.
"""

MENSAGENS = {
    "validacao": {
        "sistema_desconhecido": (
            "O sistema de caminho não foi identificado. "
            "Certifique-se de que o sistema operacional é suportado e tente novamente."
        ),
        "caminho_valido": (
            "O caminho fornecido é válido para o sistema e pode ser utilizado sem problemas."
        ),
        "caminho_invalido": (
            "O caminho fornecido é inválido para o sistema. "
            "Verifique se há erros de digitação ou inconsistências."
        ),
        "caracteres_proibidos": (
            "O caminho contém caracteres proibidos que não são permitidos pelo sistema. "
            "Remova ou substitua esses caracteres."
        ),
        "caminho_nao_encontrado": (
            "O caminho especificado não foi encontrado. "
            "Verifique se ele existe e se foi digitado corretamente."
        ),
        "permissao_negada": (
            "Permissão negada para acessar o caminho especificado. "
            "Verifique as permissões do sistema e tente novamente."
        ),
        "caminho_muito_longo": (
            "O caminho especificado excede o comprimento máximo permitido pelo sistema. "
            "Reduza o comprimento do caminho e tente novamente."
        ),
        "diretorio_nao_existe": (
            "O diretório especificado não existe. Certifique-se de que o "
            "caminho está correto e que o diretório foi criado."
        ),
        "arquivo_nao_existe": (
            "O arquivo especificado não existe no caminho fornecido. "
            "Verifique se o arquivo foi movido, excluído ou renomeado."
        ),
        "caminho_reservado": (
            "O caminho especificado é reservado pelo sistema e não pode ser utilizado. "
            "Escolha um caminho diferente."
        ),
        "formato_invalido": (
            "O formato do caminho fornecido é inválido. "
            "Verifique se ele segue o padrão esperado pelo sistema."
        ),
        "caminho_vazio": (
            "O caminho não pode estar vazio. Forneça um caminho válido e tente novamente."
        ),
        "caminho_relativo": (
            "Caminhos relativos não são permitidos. Use um caminho absoluto para evitar problemas."
        ),
        "caminho_inacessivel": (
            "Caminho inacessível. Verifique se o caminho está acessível e "
            "se você tem as permissões necessárias."
        ),
        "caminho_nao_especificado": (
            "Nenhum caminho foi especificado. Certifique-se de fornecer um caminho antes de prosseguir."
        ),
    },
    "api": {
        "erro_404": "Recurso não encontrado.",
        "erro_500": "Erro interno do servidor.",
        "sucesso": "Requisição processada com sucesso.",
    },
    "interface": {
        "botao_validar": "Validar",
        "campo_placeholder": "Digite o caminho do arquivo...",
        "titulo": "Validador de Caminhos",
    },
    "logs": {
        "inicio_validacao": "Iniciando validação do caminho.",
        "fim_validacao": "Validação concluída.",
        "erro_validacao": "Erro durante a validação do caminho.",
    },
}
