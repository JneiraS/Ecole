# -*- coding: utf-8 -*-

"""
Classe Address
"""

from dataclasses import dataclass


@dataclass
class Address:
    """Adresse d'une personne (enseignant ou élève)."""
    street: str
    city: str
    postal_code: int
