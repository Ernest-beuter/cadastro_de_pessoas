"""Testes das operações de cadastro."""
import copy
import pytest

from cadastro import CadastroPessoas
from pessoa import Pessoa
from repositorio_pessoas_memoria import (
    RepositorioPessoasMemoria,
)
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

class RepositorioDeCopias(RepositorioPessoasMemoria):
    """Devolve cópias, simulando objetos reconstruídos."""

    def buscar(self, nome):
        pessoa = super().buscar(nome)
        if pessoa is None:
            return None

        return copy.copy(pessoa)

@pytest.mark.parametrize(
    "fabrica",
    [RepositorioPessoasMemoria, RepositorioDeCopias]
)
def testAlterarPersiste(fabrica):
    repositorio = fabrica()
    repositorio.cadastrar(
        Pessoa("Ana Souza", 30, "ana@example.com")
    )
    cadastro = CadastroPessoas(repositorio)
    cadastro.alterar(
        "Ana Souza",
        "Ana Souza",
        31,
        "ana.s@example.com"
    )
    pessoa = repositorio.buscar("Ana Souza")

    assert pessoa is not None
    assert pessoa.getIdade() == 31
    assert pessoa.getEmail() == "ana.s@example.com"
