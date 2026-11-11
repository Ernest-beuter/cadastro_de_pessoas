"""Testes das operações de cadastro."""
from cadastro import CadastroPessoas

def test_cadastrar_pessoa():
    """confere ramazenamento e quantidade"""
    cadastro = CadastroPessoas()
    cadastro.cadastrar("ana", 20, "ana@ex.com")

    pessoas =  cadastro.listar()

    assert len(pessoas) == 1
    assert pessoas[0].getNome() == "ana"
    assert pessoas[0].getIdade() == 20
    assert pessoas[0].getEmail() == "ana@ex.com"

def test_busca_por_nome():
    """confere busca por nome"""
    
    cadastro = CadastroPessoas()
    cadastro.cadastrar("pedro", 32, "pedro@ex.com")

    encontrado = cadastro.buscarPorNome("pedro")
    pessoas = cadastro.listar()

    assert len(pessoas) == 1
    assert encontrado is not None
    assert encontrado.getNome() == "pedro"
    assert encontrado.getIdade() == 32
    assert encontrado.getEmail() == "pedro@ex.com"
