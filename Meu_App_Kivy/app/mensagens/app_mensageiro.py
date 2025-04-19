# -*- coding: utf-8 -*-
"""
6. Mensagens (app/mensagens/)
Contém o módulo centralizado de mensagens de feedback para a View.

Organiza mensagens por contexto:

Erros (ex: CAMINHO_INVALIDO, TIPO_INCOMPATIVEL, ARQUIVO_INEXISTENTE)

Sucessos (ex: CAMINHO_VALIDO, PASTA_ANALISADA)

Avisos ou logs informativos

A Controller solicita a mensagem correta conforme o código ou status retornado pela Model.
"""


class Exu:
    """
    Mensageiro das validações, retorna mensagens semânticas sobre estados de caminhos.

    Métodos estáticos que geram mensagens consistentes para diferentes situações
    relacionadas à validação de caminhos no sistema de arquivos.

    Padrão de mensagens:
        - ✅/❌/📁/🔒 Emojis indicativos
        - Mensagem clara e autoexplicativa
        - Caminho sempre entre aspas simples
    """

    __EMOJI_MAP = {
        'invalido': '❌',
        'nao_encontrado': '📁',
        'encontrado': '✅',
        'nao_permitido': '🔒',
        'legivel': '🔓',
        'tipo': '📦',
        'arquivo_vazio': '🗒️',
        'diretorio_vazio': '📂',
        'valido': '🎯'
    }

    @staticmethod
    def caminho_invalido(caminho: str) -> str:
        """
        Retorna mensagem indicando caminho inválido (vazio ou malformado).

        Args:
            caminho: Caminho que será analisado.

        Returns:
            Mensagem formatada indicando caminho inválido.
        """
        return (
            f"{Exu.__EMOJI_MAP['invalido']} Caminho inválido: "
            f"'{caminho}' está vazio ou malformado."
        )

    @staticmethod
    def caminho_nao_encontrado(caminho: str) -> str:
        """
        Retorna mensagem informando que o caminho não foi encontrado.

        Args:
            caminho: Caminho que será analisado.

        Returns:
            Mensagem formatada indicando caminho não encontrado.
        """
        return (
            f"{Exu.__EMOJI_MAP['nao_encontrado']} Caminho não encontrado:"
            f" '{caminho}' não existe."
        )

    @staticmethod
    def caminho_encontrado(caminho: str) -> str:
        """
        Retorna mensagem confirmando a localização do caminho.

        Args:
            caminho: Caminho identificado.

        Returns:
            Mensagem formatada confirmando localização.
        """
        return f"{Exu.__EMOJI_MAP['encontrado']} Caminho localizado: '{caminho}'."

    @staticmethod
    def caminho_nao_permitido(caminho: str) -> str:
        """
        Retorna mensagem de acesso negado ao caminho.

        Args:
            caminho: Caminho analisado.

        Returns:
            Mensagem formatada de permissão negada.
        """
        return f"{Exu.__EMOJI_MAP['nao_permitido']} Permissão negada para acessar: '{caminho}'."

    @staticmethod
    def caminho_nao_legivel(caminho: str) -> str:
        """
        Retorna mensagem indicando falta de permissão de leitura.

        Args:
            caminho: Caminho analisado.

        Returns:
            Mensagem formatada de permissão de leitura negada.
        """
        return f"{Exu.__EMOJI_MAP['nao_permitido']} Caminho sem permissão de leitura: '{caminho}'."

    @staticmethod
    def caminho_legivel(caminho: str) -> str:
        """
        Retorna mensagem confirmando permissão de leitura no caminho.

        Args:
            caminho: Caminho analisado.

        Returns:
            Mensagem formatada de permissão concedida.
        """
        return f"{Exu.__EMOJI_MAP['legivel']} Caminho acessível: '{caminho}'."

    @staticmethod
    def tipo_identificado(caminho: str, tipo: str) -> str:
        """
        Retorna mensagem informando o tipo de entidade identificada.

        Args:
            caminho: Caminho analisado.
            tipo: Tipo identificado ('arquivo', 'diretório' etc).

        Returns:
            Mensagem formatada com o tipo detectado.
        """
        return f"{Exu.__EMOJI_MAP['tipo']} Tipo detectado para '{caminho}': {tipo}."

    @staticmethod
    def tipo_nao_suportado(caminho: str) -> str:
        """
        Retorna mensagem indicando tipo não suportado.

        Args:
            caminho: Caminho analisado.

        Returns:
            Mensagem formatada de tipo não suportado.
        """
        return f"❗ Tipo desconhecido ou não suportado: '{caminho}'."

    @staticmethod
    def arquivo_vazio(caminho: str) -> str:
        """
        Retorna mensagem indicando arquivo vazio.

        Args:
            caminho: Caminho do arquivo.

        Returns:
            Mensagem formatada sobre arquivo vazio.
        """
        return f"{Exu.__EMOJI_MAP['arquivo_vazio']} Arquivo vazio: '{caminho}'."

    @staticmethod
    def diretorio_vazio(caminho: str) -> str:
        """
        Retorna mensagem indicando diretório vazio.

        Args:
            caminho: Caminho do diretório.

        Returns:
            Mensagem formatada sobre diretório vazio.
        """
        return f"{Exu.__EMOJI_MAP['diretorio_vazio']} Diretório vazio: '{caminho}'."

    @staticmethod
    def caminho_valido(caminho: str) -> str:
        """
        Retorna mensagem confirmando validade do caminho.

        Args:
            caminho: Caminho verificado.

        Returns:
            Mensagem formatada de validação bem-sucedida.
        """
        return f"{Exu.__EMOJI_MAP['valido']} Caminho válido e utilizável: '{caminho}'."

# from typing import Callable
# def testar_exu() -> None:
#     """
#     Executa testes em todos os métodos da classe Exu.

#     Mostra exemplos de saída para cada tipo de mensagem implementada.
#     """
#     caminho_teste: str = "/home/pedro-pm-dias/inexistente/arquivo.txt"
#     print("\n🧪 Testando métodos da classe Exu com o caminho de teste:\n" + "-" * 60)

#     metodos_exu: list[tuple[str, Callable[[str], str]]] = [
#         ("caminho_invalido", Exu.caminho_invalido),
#         ("caminho_nao_encontrado", Exu.caminho_nao_encontrado),
#         ("caminho_encontrado", Exu.caminho_encontrado),
#         ("caminho_nao_permitido", Exu.caminho_nao_permitido),
#         ("caminho_legivel", Exu.caminho_legivel),
#         ("tipo_identificado", lambda c: Exu.tipo_identificado(c, "arquivo")),
#         ("tipo_nao_suportado", Exu.tipo_nao_suportado),
#         ("arquivo_vazio", Exu.arquivo_vazio),
#         ("diretorio_vazio", Exu.diretorio_vazio),
#         ("caminho_valido", Exu.caminho_valido),
#     ]

#     for nome, funcao in metodos_exu:
#         try:
#             print(f"{nome}: {funcao(caminho_teste)}")
#         except ValueError as erro:
#             print(f"⚠️ Erro ao chamar '{nome}': {erro}")


# if __name__ == "__main__":
#     testar_exu()
