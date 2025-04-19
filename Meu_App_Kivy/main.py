# -*- coding: utf-8 -*-
# pylint: disable=R0903

"""
main.py

Módulo principal da aplicação Kivy/KivyMD.

Este módulo é responsável por iniciar o aplicativo, carregando os arquivos de layout (.kv),
instanciando os modelos e utilitários necessários, e exibindo a tela inicial por meio
do gerenciador de telas.

A arquitetura segue o padrão MVC, e este ponto de entrada conecta a interface gráfica
à lógica de controle e dados.
"""

from kivy.core.window import Window  # type: ignore
from kivy.lang import Builder
from kivymd.app import MDApp  # type: ignore

from app.views.app_gerenciador_telas import GerenciadorTelas
from app.models.app_models import CaminhoSOModel
from app.utils.app_tools import Ogum

# Carregamento das interfaces gráficas (.kv)
Builder.load_file("app/views/telas/tela_inicial.kv")
Builder.load_file("app/views/telas/tela_principal.kv")


class MeuApp(MDApp):
    """
    Classe principal da aplicação.

    Herda de MDApp e define o comportamento de inicialização do app,
    incluindo tema, tamanho da janela e tela inicial.

    Attributes:
        model (CaminhoSOModel): Instância inicial da Model com dados do caminho.
        caminho (dict): Representação do estado inicial do caminho.
    """

    def __init__(self, **kwargs):
        """
        Inicializa a aplicação.

        Define o modelo de caminho inicial, prepara variáveis de estado
        e executa uma validação de teste com o utilitário Ogum.
        """
        super().__init__(**kwargs)

        # Instância da Model com caminho nulo
        self.model = CaminhoSOModel(caminho="/home/")
        self.caminho = self.model.to_dict()

        # Execução de validação inicial (pode ser substituído por logging)
        saudador = Ogum()
        print(saudador.validar(caminho='/home/'))  # Debug temporário

    def build(self) -> GerenciadorTelas:
        """
        Constrói e retorna a interface principal da aplicação.

        Define configurações visuais como paleta de cores e tamanho da janela,
        e retorna o gerenciador de telas que inicia a navegação da interface.

        Returns:
            GerenciadorTelas: ScreenManager com a tela inicial carregada.
        """
        self.theme_cls.primary_palette = "Green"
        Window.size = (600, 800)

        return GerenciadorTelas()


if __name__ == "__main__":
    MeuApp().run()
