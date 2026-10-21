from pessoa import Pessoa
import cadastro
def test_cadastrar_pessoa():
    """confere ramazenamento e quantidade"""
    cadastro.cadastrar("ana", 20, "ana@ex.com")

    pessoas =  cadastro.listar()

    assert len(pessoas) == 1
    assert cadastro.pessoas[0].getNome() == "ana"
    assert cadastro.pessoas[0].getIdade() == 20
    assert cadastro.pessoas[0].getEmail() == "ana@ex.com"

def test_busca_por_nome():
    """confere busca por nome"""
    cadastro.cadastrar("pedro", 32, "pedro@ex.com")

    encontrado = cadastro.busca("nome", "pedro")
    pessoas = cadastro.listar()

    assert len(pessoas) == 2
    assert encontrado is not None
    assert encontrado.getNome() == "pedro"
    assert encontrado.getIdade() == 32
    assert encontrado.getEmail() == "pedro@ex.com"
