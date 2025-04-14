# -*- coding: utf-8 -*-

# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name, line-too-long, no-else-return, invalid-name, import-error  # noqa: E501

from controller.caminho_controller import CaminhoController
from kivymd.app import MDApp
from kivymd.toast import toast
from view.tela_validador import TelaValidador


class ValidadorApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # Tema inicial (pode ser "Light")
        self.theme_cls.primary_palette = "BlueGray"  # Cor predominante
        controller = CaminhoController()
        return TelaValidador(controller=controller)

    def trocar_tema(self):
        # Alterna entre claro e escuro
        novo_tema = "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        self.theme_cls.theme_style = novo_tema

    def mostrar_sobre(self):
        toast("Validador de Caminhos v1.0 - Desenvolvido com KivyMD")


if __name__ == '__main__':
    ValidadorApp().run()
