# -*- coding: utf-8 -*-
"""
TelaValidador - Tela principal de entrada e validação de caminhos.

Este módulo define a tela gráfica da aplicação onde o usuário pode
inserir e validar caminhos de arquivos ou diretórios com base no sistema
operacional detectado.

Autor: Seu Nome (opcional)
Data: AAAA-MM-DD
"""

# pylint: disable=invalid-name, line-too-long, no-else-return, import-error, too-few-public-methods, too-many-ancestors  # noqa: E501


from controller.caminho_controller import CaminhoController
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file("app/view/tela_validador.kv")


class TelaValidador(MDScreen):
    """
        Tela de Validação de Caminhos.

        Esta tela permite ao usuário inserir um caminho de arquivo ou diretório
        e validar se ele é válido para o sistema operacional atual.
    """
    def __init__(self, controller: CaminhoController, **kwargs):
        """
            Inicializa a tela de validação de caminhos.

            Args:
                controller (CaminhoController): Controlador responsável pela
                    validação de caminhos.
                **kwargs: Argumentos adicionais para a classe pai.
        """
        super().__init__(**kwargs)
        self.controller = controller

    def validar_caminho(self):
        """
            Valida o caminho de entrada fornecido pelo usuário.
        """
        caminho_entrada = self.ids.entrada_caminho.text.strip()

        if not caminho_entrada:
            self.ids.resultado_label.text = (
                "[b]Erro:[/b] O campo de entrada ( "
                f"{str(caminho_entrada)} ) não pode estar vazio."
            )
            return

        resultado = self.controller.validar(caminho_entrada=caminho_entrada)

        cor = "[color=00ff00]" if resultado["valido"] else "[color=ff0000]"
        valido_texto = f"{cor}{'Sim' if resultado['valido'] else 'Não'}[/color]"

        self.ids.resultado_label.text = (
            f"[b]Caminho:[/b] {resultado['caminho_entrada']}\n"
            f"[b]Sistema:[/b] {resultado['sistema']}\n"
            f"[b]Válido:[/b] {valido_texto}\n"
            f"[b]Mensagem:[/b] {resultado['mensagem']}"
        )
