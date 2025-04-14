# pylint disable: line-too-long
# flake8: noqa E501

"""
    Este módulo define um dicionário chamado `MENSAGENS`
    que contém mensagens de erro e validação relacionadas
    a caminhos de arquivos e diretórios. 

    Cada chave no dicionário representa um identificador
    único para uma mensagem específica, enquanto o valor
    associado é a mensagem descritiva correspondente.

    As mensagens cobrem uma ampla gama de cenários, como:
        - Caminhos inválidos ou não encontrados.
        - Problemas de permissões.
        - Caracteres proibidos em caminhos.
        - Restrições de formato ou comprimento de caminhos.
        - Uso de caminhos relativos ou vazios.

    Este dicionário pode ser utilizado em aplicações para
    fornecer mensagens de erro consistentes
    e localizadas ao usuário.
"""


MENSAGENS = {
    "sistema_desconhecido": (
        "O sistema de caminho não foi identificado."
        " Certifique-se de que o sistema operacional é suportado e tente novamente."
    ), "caminho_valido": (
        "O caminho fornecido é válido para o sistema e pode ser utilizado sem problemas."
    ), "caminho_invalido": (
        "O caminho fornecido é inválido para o sistema."
        " Verifique se há erros de digitação ou inconsistências."
    ), "caracteres_proibidos": (
        "O caminho contém caracteres proibidos que não são permitidos pelo sistema."
        " Remova ou substitua esses caracteres."
    ), "caminho_nao_encontrado": (
        "O caminho especificado não foi encontrado."
        " Verifique se ele existe e se foi digitado corretamente."
    ), "permissão_negada": (
        "Permissão negada para acessar o caminho especificado."
        " Verifique as permissões do sistema e tente novamente."
    ), "caminho_muito_longo": (
        "O caminho especificado excede o comprimento máximo permitido pelo sistema."
        " Reduza o comprimento do caminho e tente novamente."
    ), "diretório_nao_existe": (
        "O diretório especificado não existe. Certifique-se de que o"
        " caminho está correto e que o diretório foi criado."
    ), "arquivo_nao_existe": (
        "O arquivo especificado não existe no caminho fornecido."
        " Verifique se o arquivo foi movido, excluído ou renomeado."
    ), "caminho_reservado": (
        "O caminho especificado é reservado pelo sistema e não pode ser utilizado."
        " Escolha um caminho diferente."
    ), "formato_invalido": (
        "O formato do caminho fornecido é inválido."
        " Verifique se ele segue o padrão esperado pelo sistema."
    ), "caminho_vazio": (
        "O caminho não pode estar vazio. Forneça um caminho válido e tente novamente."
    ), "caminho_relativo": (
        "Caminhos relativos não são permitidos. Use um caminho absoluto para evitar problemas."
    ), "caminho_inacessível": (
        "Caminho inacessível. Verifique se o caminho está acessível e"
        " se você tem as permissões necessárias."
    ), "caminho_nao_especificado": (
        "Nenhum caminho foi especificado. Certifique-se de fornecer um caminho antes de prosseguir."
    ),
}
