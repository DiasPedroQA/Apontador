# main.py
# -*- coding: utf-8 -*-

"""
Ponto de entrada da aplicação KivyMD.

Este módulo inicializa a aplicação com base na arquitetura MVC,
carregando a interface gráfica da tela principal e preparando
os componentes necessários.
"""

from kivymd.app import MDApp
from kivy.core.window import Window

from app.view.tela_identificador import TelaIdentificador


class MeuAppKivy(MDApp):
    """
    Classe principal do aplicativo KivyMD.

    Responsável por inicializar o tema da aplicação, carregar a
    tela principal e executar o loop principal do Kivy.
    """

    def build(self):
        self.title = "Validador de Caminhos"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return TelaIdentificador()


if __name__ == "__main__":
    Window.size = (1000, 700)  # Tamanho padrão da janela (ajustável)
    MeuAppKivy().run()
