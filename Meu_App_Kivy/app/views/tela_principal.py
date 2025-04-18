# pylint: disable=C0114, C0115, C0116, R0901, R0903, W0221, E0611

from kivymd.uix.screen import MDScreen  # type: ignore
from kivy.lang import Builder  # type: ignore

Builder.load_file("app/views/tela_principal.kv")


class TelaPrincipal(MDScreen):
    def on_pre_enter(self, *args):
        if self.ids.get("nome_input"):
            self.ids.nome_input.text = ""

    def confirmar_nome(self):
        nome = self.ids.nome_input.text
        print(f"Nome digitado: {nome}")
