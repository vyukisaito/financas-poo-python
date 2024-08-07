from categoria import Categoria
from transacao import Transacao

LISTA_CATEGORIAS = []
LISTA_TRANSACAO = []


def cadastrar_categoria(nome):
    nova_categoria = Categoria(nome=nome)

    LISTA_CATEGORIAS.append(nova_categoria)

    return nova_categoria


def cadastrar_transacao(descricao, valor, categoria):
    nova_transacao = Transacao(descrição=descricao, valor=valor, categoria=categoria)
    
    LISTA_TRANSACAO.append(nova_transacao)

    return nova_transacao


def saldo_total():
    total = 0

    for t in LISTA_TRANSACAO:
        total += t.valor

    return total
