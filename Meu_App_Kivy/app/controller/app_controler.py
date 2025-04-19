# -*- coding: utf-8 -*-
# pylint: disable=C0114, C0115, C0116, R0903

"""
app_controler.py

3. Controller (app/controller/)
Responsável por orquestrar o fluxo da aplicação com base na interação do usuário.

Funções principais:
- Receber dados da View (por exemplo, uma string de caminho ou nome).
- Processar os dados por meio de utilitários e modelos.
- Interagir com a camada de mensagens para gerar feedback apropriado.
- Devolver os resultados à View para exibição ao usuário.

Este controller exemplifica um fluxo de tratamento de nome, formatando-o,
executando uma lógica associada e retornando mensagens personalizadas.
"""

from app.models.app_models import AppModel
from app.utils.app_tools import formatar_nome
from app.mensagens.app_mensageiro import Exu


class AppController:
    """
    Controlador principal da aplicação.

    Executa os fluxos principais do sistema a partir das entradas da View,
    coordenando interações com Modelos, Utilitários e Mensagens.
    """

    def processar_nome(self, nome: str) -> dict:
        nome_formatado = formatar_nome(nome)
        mensagem = AppModel().executar_logica(nome_formatado)
        mensagem_sucesso = Exu.mensagem_sucesso(nome_formatado)

        return {
            "nome_formatado": nome_formatado,
            "mensagem_sucesso": mensagem_sucesso,
            "mensagem_execucao": mensagem
        }
