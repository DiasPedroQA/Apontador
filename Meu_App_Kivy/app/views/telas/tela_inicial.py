# pylint: disable=C0114, C0115, C0116, R0903

from kivy.uix.screenmanager import Screen

class TelaInicial(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_press_comecar(self):
        # Navega para a tela principal quando o botão "Começar" for pressionado
        self.manager.current = "tela_principal"
