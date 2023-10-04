"""Cadastro de produto"""
__version__ = "0.1.0"

from pprint import pprint

produto = {
    "nome": "Caneta",
    "cores": ["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,
}

cliente = {
    "nome": "Matheus"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra['cliente']['nome']} comprou" 
    f" o produto {compra['produto']['nome']}"
    f" e pagou um total de R${total_compra}"
)

# pprint(compra)