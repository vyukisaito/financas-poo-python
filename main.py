from utilitarios import cadastrar_categoria, cadastrar_transacao, saldo_total

# categorias
categoria_receitas = cadastrar_categoria("Receitas")
categoria_contas = cadastrar_categoria("Contas Fixas")
categoria_lazer = cadastrar_categoria("Lazer")
categoria_viagens = cadastrar_categoria("Viagens")

# transacoes
print("TRANSACAO")
repetir = 's'
while repetir == 's':
    decricao_transacao = input("Cadastrar descrição: ")
    valor_transacao = float(input("Valor: "))
    categoria_transacao = input("Categoria: ")
    repetir = input("Deseja cadastrar um novo item? [S/N] ")
    print(' ')

    cadastrar_transacao(
        descricao=decricao_transacao,
        valor=valor_transacao,
        categoria=globals()[f'categoria_{categoria_transacao.lower()}']
    )


# cadastrar_transacao(
#     descricao="Salário Jan/2024",
#     valor=3500.0,
#     categoria=categoria_receitas
# )

# cadastrar_transacao(
#     descricao="Mesadinha",
#     valor=50.0,
#     categoria=categoria_receitas
# )

# cadastrar_transacao(
#     descricao="Cinema",
#     valor=-50,
#     categoria=categoria_lazer
# )

# cadastrar_transacao(
#     descricao="Conta de luz",
#     valor=-300,
#     categoria=categoria_contas
# )

# cadastrar_transacao(
#     descricao="Japão",
#     valor=-1000,
#     categoria=categoria_viagens
# )

total = saldo_total()

print(f"Seu saldo total foi de: R${total}")

