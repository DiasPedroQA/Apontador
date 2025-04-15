# -*- coding: utf-8 -*-
"""
TelaIdentificador - Tela principal de entrada e identificação de caminhos.

Este módulo define a tela gráfica da aplicação onde o usuário pode
inserir e identificar caminhos de arquivos ou diretórios com base no sistema
operacional detectado.

Autor: Pedro P. M. Dias
Data: 2025-01-01
"""

# pylint: disable=line-too-long, no-else-return, import-error, too-few-public-methods, too-many-ancestors  # noqa: E501


from app.controller.caminho_controller import CaminhoController
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file("app/view/tela_identificador.kv")


class TelaIdentificador(MDScreen):
    """
        Tela de Identificação de Caminhos.

        Esta tela permite ao usuário inserir um caminho de arquivo ou diretório
        e identificar se ele é válido para o sistema operacional atual.
    """
    def __init__(self, controller: CaminhoController, **kwargs):
        """
            Inicializa a tela de identificação de caminhos.

            Args:
                controller (CaminhoController): Controlador responsável pela
                    identificação de caminhos.
                **kwargs: Argumentos adicionais para a classe pai.
        """
        super().__init__(**kwargs)
        self.controller = controller

    def identificar_caminho(self):
        """
            Identifica o caminho de entrada fornecido pelo usuário.
        """
        caminho_entrada = self.ids.entrada_caminho.text.strip()

        if not caminho_entrada:
            self.ids.resultado_label.text = (
                "[b]Erro:[/b] O campo de entrada ( "
                f"{str(caminho_entrada)} ) não pode estar vazio."
            )
            return

        resultado = self.controller.identificar(caminho_entrada=caminho_entrada)

        cor = "[color=00ff00]" if resultado["identifico"] else "[color=ff0000]"
        identifico_texto = f"{cor}{'Sim' if resultado['identifico'] else 'Não'}[/color]"

        self.ids.resultado_label.text = (
            f"[b]Caminho:[/b] {resultado['caminho_entrada']}\n"
            f"[b]Sistema:[/b] {resultado['sistema']}\n"
            f"[b]Válido:[/b] {identifico_texto}\n"
            f"[b]Mensagem:[/b] {resultado['mensagem']}"
        )
