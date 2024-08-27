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

    person_list = []

    id: int = field(default=None, init=False)
    first_name: str
    last_name: str
    age: int
    address: Address | None = field(default=None, init=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.age} ans)"

    @classmethod
    def create_person(cls, first_name, last_name, age, address):
        """
        Crée un nouvel objet Person et l'ajoute à la liste des personnes.
        :param first_name:
        :param last_name:
        :param age:
        :param address:
        :return:
        """
        new_person = cls(first_name=first_name, last_name=last_name, age=age)
        Person.person_list.append(new_person)
        return new_person

