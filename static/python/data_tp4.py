from typing import List

import requests


def recuperation_produit(code_barre: str) -> dict:
    import requests

    res = requests.get(
        f"https://world.openfoodfacts.org/api/v0/product/{code_barre}.json"
    )
    data = res.json()
    return data


class ProduitAllergeneDto:
    def __init__(
        self, code_barre: str, liste_allergenes: List[str], liste_traces: List[str]
    ):
        self.code_barre = code_barre
        self.liste_allergenes = liste_allergenes
        self.liste_traces = liste_traces

    def __str__(self):
        return str(self.liste_allergenes)


def transformer_produit_recupere(produit_dict: dict) -> ProduitAllergeneDto:
    return ProduitAllergeneDto(
        code_barre=produit_dict["code"],
        liste_allergenes=produit_dict["product"]["allergens_tags"],
        liste_traces=produit_dict["product"]["traces_tags"],
    )


def verification_allergenes(
    allergenes: List[str], produit_allergenes: ProduitAllergeneDto
) -> bool:
    allergenes_of_product = produit_allergenes.liste_allergenes
    for allergene in allergenes:
        if allergene in allergenes_of_product:
            return True
    return False


code_barre = 3560071407711
allergenes = ["en:gluten"]
produit_dict = recuperation_produit(code_barre)
produit_allergenes = transformer_produit_recupere(produit_dict)
print(produit_allergenes)
print(
    verification_allergenes(
        allergenes=allergenes, produit_allergenes=produit_allergenes
    )
)
