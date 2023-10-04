"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a 
mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    LANG=pt_BR

Execução:

    python hello.py
"""
__version__ = "0.1.2"
__author__ = "Matheus"

import os

current_language = os.getenv("LANG", "en_US")[:5] #primeiros 5 char

# Dicts, Sets, Hash Table - O(1) - Constante

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "fr_FR": "Bonjour, Monde!",
    "es_SP": "Hola, Mondo!",
}

print(msg[current_language])
