""" Bloco de notas

$ notas.py new "Minha Nota"
tag: "tech"
text:
"Exemplo de anotação"

$ notas.py read tech"
...

"""
__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notas.txt")
cmds = ("read", "new")
arguments = sys.argv[1:]

if not arguments:
    print(f"Especifique o comando, utilize: {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Comando inválido, utilize:  {cmds}")
    sys.exit(1)

if arguments[0] == "new":
    titulo = arguments[1]
    text = [
        f"{titulo}",
        input("tag:").strip(),
        input("texto:\n").strip(),
    ]
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")

if arguments[0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()