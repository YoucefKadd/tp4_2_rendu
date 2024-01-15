# app.py

import random

# Liste de citations
citations = [
    "L'avenir appartient à ceux qui se lèvent tôt.",
    "La vie est un mystère qu'il faut vivre, et non un problème à résoudre.",
    "Le seul moyen de faire du bon travail est d'aimer ce que vous faites.",
    "La vie est ce qui arrive pendant que vous êtes occupé à faire d'autres projets."
]

def obtenir_citation():
    return random.choice(citations)

if __name__ == '__main__':
    citation = obtenir_citation()
    print(citation)
