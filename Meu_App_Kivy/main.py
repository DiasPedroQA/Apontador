# -*- coding: utf-8 -*-

# pylint: disable=C0114, C0115, C0116, R0903

"""
Ponto de entrada da aplicação Kivy.

Este módulo inicializa a aplicação com base na arquitetura MVC,
carregando a interface gráfica da tela principal e preparando
os componentes necessários.

┌────────────┐
│  main.py   │
└────┬───────┘
     │
     ▼
┌────────────────────────────┐
│ TelaPrincipal (View)       │
│ tela_principal.py          │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────────┐
│ app_controller.py (Controller) │
└───────────┬────────────────────┘
            │
     ┌──────├────────┐
     ▼               ▼
┌──────────────┐ ┌──────────────┐
│ app_model.py │ │ helpers.py   │
│ (Model)      │ │ (Utils)      │
└──────────────┘ └──────────────┘
     │                   │
     ▼                   ▼
┌────────────────────────────┐
│ mensageiro.py (Messages)   │
└────────────────────────────┘

"""

from kivy.core.window import Window  # type: ignore
from kivymd.app import MDApp  # type: ignore
from app.views.tela_principal import TelaPrincipal  # Import da view (Tela Principal)
# from app.controller.app_controller import AppController  # Import do controlador
from app.models.app_model import AppModel  # Import do modelo
from app.utils.helpers import saudacao  # Import de funções utilitárias
# from app.mensagens.mensageiro import Mensageiro  # Import de mensagens


class MeuApp(MDApp):
    """
    Classe principal do aplicativo Kivy. Inicializa a aplicação e carrega a tela principal.
    A comunicação entre a interface, controlador e modelo é feita nesta classe.
    """

    def __init__(self, **kwargs):
        """
        Inicializa a aplicação, configurando o controlador, modelo e mensageiro.
        """
        super().__init__(**kwargs)
        self.model = AppModel()  # Inicializa o modelo
        # self.controller = AppController(self.model)  # Inicializa o controlador
        # self.mensageiro = Mensageiro()  # Inicializa o sistema de mensagens

    def build(self) -> TelaPrincipal:
        """
        Configura a interface gráfica da aplicação, retornando a tela principal.
        """
        self.theme_cls.primary_palette = "Green"
        Window.size = (500, 500)
        print(saudacao)
        return TelaPrincipal()  # Passa o controlador para a view
        # return TelaPrincipal(self.controller)  # Passa o controlador para a view


if __name__ == "__main__":
    MeuApp().run()
