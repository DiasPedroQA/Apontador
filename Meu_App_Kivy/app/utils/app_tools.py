# -*- coding: utf-8 -*-
# pylint: disable=E0401, C0413
"""
5. Utils (app/utils/)
Biblioteca de funções reutilizáveis e auxiliares, que não possuem lógica de negócio direta.

Exemplos:

Normalização e sanitização de caminhos

Regex de identificação de sistema

Geração de hashes, logs, strings formatadas

Manipulação com pathlib, os, re etc.

Pode ser usada tanto pela Model quanto pela Controller, conforme o escopo.
"""

import os
from pathlib import Path
from typing import Literal, TypedDict
import sys

# Garante que o diretório raiz esteja no sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mensagens.app_mensageiro import Exu  # noqa: E402


class ResultadoValidacao(TypedDict):
    """
    Estrutura de retorno para validações de caminhos.

    Atributos:
        caminho (str): Caminho analisado
        legivel (bool): Se o caminho tem permissão de leitura
        valido (bool): Se o caminho é válido e existente
        tipo (Literal): Tipo do caminho ('arquivo', 'diretorio' ou 'desconhecido')
        vazio (bool): Se o caminho está vazio (arquivo 0 bytes ou diretório sem itens)
        mensagem (str): Mensagem semântica do status (gerada por Exu)
    """
    caminho: str
    legivel: bool
    valido: bool
    tipo: Literal["arquivo", "diretorio", "desconhecido"]
    vazio: bool
    mensagem: str


class Ogum:
    """
    Ferreiro das validações - Valida caminhos com precisão divina.

    Oferece métodos estáticos para verificar existência, permissões, tipo e conteúdo
    de caminhos no sistema de arquivos, seguindo os princípios da mitologia africana.

    Métodos principais:
        validar: Realiza validação completa do caminho
        _existe: Verifica existência do caminho
        _eh_legivel: Verifica permissões de leitura
        _tipo_caminho: Identifica o tipo da entidade
        _eh_vazio: Verifica se está vazio
    """

    @staticmethod
    def validar(caminho: str) -> ResultadoValidacao:
        """
            Realiza validação completa de um caminho no sistema de arquivos.

            Args:
                caminho: Caminho absoluto ou relativo a ser validado

            Returns:
                Dicionário contendo:
                - Validade do caminho
                - Permissões de leitura
                - Tipo (arquivo/diretório)
                - Status de vazio
                - Mensagem semântica do Exu
        """
        resultado: ResultadoValidacao = {
            "caminho": caminho,
            "valido": False,
            "legivel": False,
            "tipo": "desconhecido",
            "vazio": False,
            "mensagem": Exu.caminho_invalido(caminho)  # Mensagem padrão inicial
        }

        # Validação em etapas com curto-circuito
        if not caminho or not caminho.strip():
            return resultado

        resultado["valido"] = Ogum._existe(caminho)
        if not resultado["valido"]:
            resultado["mensagem"] = Exu.caminho_nao_encontrado(caminho)
            return resultado

        resultado["legivel"] = Ogum._eh_legivel(caminho)
        if not resultado["legivel"]:
            resultado["mensagem"] = Exu.caminho_nao_legivel(caminho)
            return resultado

        resultado["tipo"] = Ogum._tipo_caminho(caminho)

        # Verificação de conteúdo apenas para tipos conhecidos
        if resultado["tipo"] in ("arquivo", "diretorio"):
            resultado["vazio"] = Ogum._eh_vazio(caminho)
            resultado["mensagem"] = Ogum._gerar_mensagem_final(
                caminho,
                resultado["tipo"],
                resultado["vazio"]
            )
        else:
            resultado["mensagem"] = Exu.tipo_nao_suportado(caminho)

        return resultado

    @staticmethod
    def _gerar_mensagem_final(caminho: str, tipo: str, vazio: bool) -> str:
        """Seleciona a mensagem final apropriada baseada no tipo e status."""
        if tipo == "arquivo" and vazio:
            return Exu.arquivo_vazio(caminho)
        if tipo == "diretorio" and vazio:
            return Exu.diretorio_vazio(caminho)
        return Exu.caminho_valido(caminho)

    @staticmethod
    def _existe(caminho: str) -> bool:
        """Verifica existência do caminho com mensagem semântica."""
        existe = Path(caminho).exists()
        print(Exu.caminho_encontrado(caminho) if existe else Exu.caminho_nao_encontrado(caminho))
        return existe

    @staticmethod
    def _eh_legivel(caminho: str) -> bool:
        """Verifica permissão de leitura no caminho."""
        return os.access(caminho, os.R_OK)

    @staticmethod
    def obter_nome_arquivo(caminho: str) -> str:
        """~"""
        return caminho

    @staticmethod
    def _eh_vazio(caminho: str) -> bool:
        """Verifica se o caminho está vazio (arquivo ou diretório)."""
        path = Path(caminho)
        try:
            if path.is_file():
                return path.stat().st_size == 0
            if path.is_dir():
                return not any(path.iterdir())
        except OSError:
            return True  # Considera como vazio se não puder verificar
        return False

    @staticmethod
    def _eh_arquivo(caminho: str) -> bool:
        """Verifica se o caminho é um arquivo."""
        return Path(caminho).is_file()

    @staticmethod
    def _eh_diretorio(caminho: str) -> bool:
        """Verifica se o caminho é um diretório."""
        return Path(caminho).is_dir()

    @staticmethod
    def _tipo_caminho(caminho: str) -> Literal["arquivo", "diretorio", "desconhecido"]:
        """Identifica o tipo do caminho com fallback para desconhecido."""
        return ("arquivo" if Ogum._eh_arquivo(caminho) else
                "diretorio" if Ogum._eh_diretorio(caminho) else
                "desconhecido")

    @staticmethod
    def obter_metadados(caminho: str) -> dict:
        """Obtém metadados básicos do caminho (nome, extensão, diretório pai)."""
        path = Path(caminho)
        return {
            "nome": path.stem,
            "extensao": path.suffix or "",
            "diretorio_pai": str(path.parent)
        }


def testar_ogum(caminhos: list[str]) -> None:
    """
    Testa a classe Ogum com uma lista de caminhos.

    Args:
        caminhos: Lista de caminhos para teste
    """
    print("\n⚒️ Testando o Ferreiro Ogum com diversos caminhos\n" + "-" * 60)
    for caminho in caminhos:
        resultado = Ogum.validar(caminho)
        print(f"\n🔍 Caminho: {resultado['caminho']}")
        print(f"  ✅ Válido: {resultado['valido']}")
        print(f"  📖 Legível: {resultado['legivel']}")
        print(f"  📦 Tipo: {resultado['tipo']}")
        print(f"  🌀 Vazio: {resultado['vazio']}")
        print(f"  ✉️ Mensagem: {resultado['mensagem']}")


if __name__ == "__main__":
    caminhos_teste = [
        "/home/usuario/arquivo_teste.txt",
        "/home/usuario/Documentos",
        "",
        "   ",
        "/caminho/inexistente/arquivo.txt",
        "/root/arquivo_secreto.txt",
    ]
    testar_ogum(caminhos_teste)
