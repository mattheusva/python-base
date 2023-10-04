"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a 
mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    LANG=pt_BR

ou informe através da CLI arguments "--lang"

ou o usuário terá que digitar.
Execução:

    python hello.py
"""
__version__ = "0.1.3"
__author__ = "Matheus"

import os
import sys

arguments = {
    "lang": None,
    "count": 1
}
for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language = os.getenv("LANG")
    if current_language is None:
        current_language = input("Choose a language:")

current_language = current_language[:5]

# Dicts, Sets, Hash Table - O(1) - Constante

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "fr_FR": "Bonjour, Monde!",
    "es_SP": "Hola, Mondo!",
}

print(msg[current_language] * int(arguments["count"]))
