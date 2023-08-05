"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a 
mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    LANG=pt_BR

Execução:

    python hello.py
"""
__version__ = "0.0.1"
__author__ = "Matheus"

import os

current_language = os.getenv("LANG", "en_US")[:5] #primeiros 5 char

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)