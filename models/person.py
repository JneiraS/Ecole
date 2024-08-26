# -*- coding: utf-8 -*-

"""
Classe abstraite Person, mère de Student et Teacher
"""

from dataclasses import dataclass, field
from abc import ABC
from .address import Address


@dataclass
class Person(ABC):
    """Personne liée à l'école : enseignant ou élève."""
    first_name: str
    last_name: str
    age: int
    address: Address | None = field(default=None, init=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.age} ans)"
