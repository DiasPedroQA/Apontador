# main.py
# -*- coding: utf-8 -*-

"""
Ponto de entrada da aplicação Kivy.

Este módulo inicializa a aplicação com base na arquitetura MVC,
carregando a interface gráfica da tela principal e preparando
os componentes necessários.
"""

from kivy.app import App
from kivy.core.window import Window

from app.view.tela_identificador import TelaIdentificador


class MeuAppKivy(App):
    """
    Classe principal do aplicativo Kivy.

    Responsável por carregar a tela principal e executar o loop
    principal do Kivy.
    """

    def build(self):
        self.title = "Validador de Caminhos"
        return TelaIdentificador()


if __name__ == "__main__":
    Window.size = (1000, 700)  # Tamanho padrão da janela (ajustável)
    MeuAppKivy().run()
