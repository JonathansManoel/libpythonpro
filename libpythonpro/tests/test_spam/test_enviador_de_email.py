import pytest

from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
['foo@bar.com.br', 'jonathan@python.pro.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'luciano@python.pro.br',
        'Cursos Python Pro',
        'Turma Moacir Modas aberta'
    )
    assert destinatario in resultado