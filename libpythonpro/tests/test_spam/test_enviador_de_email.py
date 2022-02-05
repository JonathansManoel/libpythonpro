from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None

def test_remetente():
    enviador= Enviador()
    resultado=enviador.enviar(
        'jonathan@python.pro.br',
        'luciano@python.pro.br',
        'Cursos Python Pro',
        'Turma Moacir Modas aberta'
    )
    assert 'jonathan@python.pro.br' in resultado