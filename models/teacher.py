# -*- coding: utf-8 -*-

"""
Classe Teacher
"""

from dataclasses import dataclass, field
from datetime import date
from typing import TYPE_CHECKING

from models.person import Person


@dataclass
class Teacher(Person):
    """Enseignant d'un ou plusieurs cours de l'école :
    - hiring_date : date d'arrivée dans l'école
    - courses_teached : cours qu'il ou elle enseigne
    """

    teacher_list = []

    id: int = field(default=None, init=False)
    hiring_date: date
    courses_teached: list = field(default_factory=list, init=False)

    @classmethod
    def create_teacher(cls, first_name, last_name, age, hiring_date):
        new_teacher = cls(
            first_name=first_name, last_name=last_name, age=age, hiring_date=hiring_date
        )
        Teacher.teacher_list.append(new_teacher)
        return new_teacher

    def add_course(self, course) -> None:
        """Ajout du cours course à la liste des cours qu'il enseigne."""
        course.teacher = self

    def __str__(self) -> str:
        person_str = super().__str__()
        return f"{person_str}, arrivé(e) le {self.hiring_date}"
