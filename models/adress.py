# -*- coding: utf-8 -*-

"""
Classe Adress
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Adress:
    """Adresse d'une personne (enseignant ou élève)."""

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
