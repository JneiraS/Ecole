# -*- coding: utf-8 -*-

"""
Classe Adress
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Adress:
    """
    Adresse d'une personne (enseignant ou élément).
    """

    aderess_list = []

    id: Optional[int] = field(default=None, init=False)
    street: str
    city: str
    postal_code: int

    @classmethod
    def create_adress(cls, street, city, postal_code):
        new_adress = cls(street=street, city=city, postal_code=postal_code)
        Adress.aderess_list.append(new_adress)
        return new_adress

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.postal_code}"

def find_adress_by_id(id_number) -> Adress:
    """
    Renvoit l'objet Adress correspondant à l'id_number
    :param id_number:

    """
    return next((a for a in Adress.aderess_list if a.id == id_number), None)
