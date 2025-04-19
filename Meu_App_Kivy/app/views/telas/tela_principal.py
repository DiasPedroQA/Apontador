# pylint: disable=C0114, C0115, C0116, R0901, R0903, W0221, E0611

from kivy.uix.screenmanager import Screen


class TelaPrincipal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_press_voltar(self):
        # Navega de volta para a tela inicial quando o botão "Voltar" for pressionado
        self.manager.current = "tela_inicial"
