# pylint: disable=C0114, C0115, C0116, R0903

from app.models.app_model import AppModel
from app.utils.helpers import formatar_nome
from app.mensagens.mensageiro import Mensageiro


class AppController:
    def processar_nome(self, nome: str) -> None:
        nome_formatado = formatar_nome(nome)
        mensagem = AppModel().executar_logica(nome_formatado)
        print(Mensageiro.mensagem_sucesso(nome_formatado))
        print(mensagem)
