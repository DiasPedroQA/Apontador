# -*- coding: utf-8 -*-
# pylint: disable=C0114, C0115, C0116, R0903

"""
app_gerenciador_telas.py

Gerenciador de telas (ScreenManager) da aplicação Kivy.

Este módulo é responsável por gerenciar a navegação entre telas da aplicação.
Carrega e registra as views (telas) no gerenciador, utilizando nomes únicos
para cada tela a fim de permitir a transição de forma dinâmica.

O módulo segue o padrão MVC, estando na camada de `View`.
"""

from kivy.uix.screenmanager import ScreenManager
from app.views.telas.tela_inicial import TelaInicial
from app.views.telas.tela_principal import TelaPrincipal


class GerenciadorTelas(ScreenManager):
    """
    Gerenciador central de telas da aplicação.

    Herda de ScreenManager e registra as telas iniciais no momento da inicialização.

    Attributes:
        tela_inicial (TelaInicial): Tela de entrada onde o usuário insere o caminho.
        tela_principal (TelaPrincipal): Tela principal que exibe os resultados.
    """

    def __init__(self, **kwargs):
        """
        Inicializa o GerenciadorTelas com as telas disponíveis no app.
        """
        super().__init__(**kwargs)

        # Cria instâncias das telas
        self.tela_inicial = TelaInicial(name="tela_inicial")
        self.tela_principal = TelaPrincipal(name="tela_principal")

        # Adiciona as telas ao gerenciador
        self.add_widget(self.tela_inicial)
        self.add_widget(self.tela_principal)
