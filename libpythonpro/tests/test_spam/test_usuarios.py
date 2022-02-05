from libpythonpro.spam.db import Conexao
from libpythonpro.spam.modelos import Usuario


def concexao():
    return Conexao()


def test_salvar_usuario():
    conexao = concexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome='Jonathan')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuarios():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='Jonathan'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
