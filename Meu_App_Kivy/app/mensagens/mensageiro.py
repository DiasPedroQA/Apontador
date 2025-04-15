# pylint: disable=line-too-long
# flake8: noqa E501
# app/mensagens/mensagens.py

"""
    Este módulo define um dicionário chamado `MENSAGENS`
    que contém mensagens relacionadas à identificação de caminhos de arquivos e diretórios.
    As mensagens são organizadas por categorias e abrangem:
    - Validações de caminhos.
    - Erros e respostas de API.
    - Textos para interface gráfica.
    - Mensagens para registro em logs.
"""

MENSAGENS = {
    "validação": {
        "sistema_desconhecido": (
            "Não foi possível identificar o sistema operacional a partir do caminho fornecido. "
            "Verifique se o formato está correto e se o sistema é suportado."
        ),
        "caminho_valido": (
            "O caminho \"{caminho}\" é válido para o sistema operacional identificado e pode ser utilizado normalmente."
        ),
        "caminho_invalido": (
            "O caminho \"{caminho}\" é inválido para o sistema operacional identificado. "
            "Corrija possíveis erros de formatação ou caracteres proibidos."
        ),
        "caracteres_proibidos": (
            "O caminho \"{caminho}\" contém caracteres proibidos que não são permitidos pelo sistema. "
            "Remova ou substitua esses caracteres."
        ),
        "caminho_nao_encontrado": (
            "O caminho \"{caminho}\" não foi encontrado. "
            "Verifique se ele existe e se foi digitado corretamente."
        ),
        "permissão_negada": (
            "Permissão negada para acessar o caminho \"{caminho}\". "
            "Verifique as permissões do sistema e tente novamente."
        ),
        "caminho_muito_longo": (
            "O caminho \"{caminho}\" excede o comprimento máximo permitido pelo sistema. "
            "Reduza o comprimento e tente novamente."
        ),
        "diretorio_nao_existe": (
            "O diretório \"{caminho}\" não existe. Certifique-se de que o caminho está correto e que o diretório foi criado."
        ),
        "arquivo_nao_existe": (
            "O arquivo \"{caminho}\" não existe. "
            "Verifique se ele foi movido, excluído ou renomeado."
        ),
        "caminho_reservado": (
            "O caminho \"{caminho}\" é reservado pelo sistema e não pode ser utilizado. "
            "Escolha um caminho diferente."
        ),
        "formato_invalido": (
            "O formato do caminho \"{caminho}\" é inválido ou não segue os padrões exigidos pelo sistema operacional."
        ),
        "caminho_vazio": (
            "O caminho não pode estar vazio. Forneça um caminho válido e tente novamente."
        ),
        "caminho_relativo": (
            "Caminhos relativos como \"{caminho}\" não são suportados nesta operação. Use um caminho absoluto."
        ),
        "caminho_inacessível": (
            "O caminho \"{caminho}\" está inacessível. Verifique permissões e disponibilidade."
        ),
        "caminho_nao_especificado": (
            "Nenhum caminho foi especificado. Certifique-se de fornecer um caminho antes de prosseguir."
        ),
        "tipo_invalido": (
            "O valor fornecido para o caminho \"{caminho}\" é inválido. Espera-se uma string representando um caminho de arquivo ou diretório."
        ),
        "diretorio_esperado": (
            "Esperava-se um diretório, mas foi fornecido um arquivo: \"{caminho}\". Verifique e tente novamente."
        ),
        "arquivo_esperado": (
            "Esperava-se um arquivo, mas foi fornecido um diretório: \"{caminho}\". Verifique e tente novamente."
        ),
    },
    "api": {
        "sucesso": "Requisição processada com sucesso. Validação concluída.",
        "erro_400": "Requisição inválida. Verifique os dados enviados.",
        "erro_404": "Recurso não encontrado.",
        "erro_422": "Erro de validação. Os dados fornecidos não atendem aos requisitos esperados.",
        "erro_500": "Erro interno do servidor.",
        "parâmetro_ausente": "Parâmetro obrigatório ausente: 'caminho'.",
    },
    "interface": {
        "botão_identificar": "Identificar",
        "campo_placeholder": "Digite o caminho do arquivo...",
        "titulo": "Identificador de Caminhos",
        "descrição_resultado": "Resultado da validação do caminho:",
        "mensagem_aguarde": "Validando caminho, por favor aguarde...",
    },
    "logs": {
        "inicio_validação": "Iniciando identificação do caminho.",
        "fim_validação": "Identificação concluída com sucesso.",
        "erro_validação": "Erro durante a identificação do caminho.",
        "caminho_recebido": "Caminho recebido para validação: {caminho}",
        "sistema_detectado": "Sistema identificado a partir do caminho: {sistema}",
    },
}
