# -*- coding: utf-8 -*-

"""
Classe Student, fille de la classe Person
"""

from dataclasses import dataclass, field
from typing import ClassVar

from models.person import Person



@dataclass
class Student(Person):
    """Elève suivant un ou plusieurs cours de l'école :
    - students_nb   : nombre total d'élèves
    - student_nbr   : n° d'élève
    - courses_taken : liste des cours pris par cet élève
    """

    student_list = []

    students_nb: ClassVar[int] = 0  # nb d'étudiants créés
    student_nbr: int = field(init=False)
    courses_taken: list = field(default_factory=list, init=False)

    def __post_init__(self):
        """Détermination du n° de l'élève créé."""
        Student.students_nb += 1
        self.student_nbr = Student.students_nb

    @classmethod
    def create_student(cls, first_name, last_name, age):
        new_student = cls(first_name=first_name, last_name=last_name, age=age)
        Student.student_list.append(new_student)
        return new_student

    def add_course(self, course) -> None:
        """Ajout du cours course à la liste des cours suivis par l'élève."""
        self.courses_taken.append(course.name)
        course.students_taking_it.append(self)

    def __str__(self) -> str:
        person_str = super().__str__()
        return f"{person_str}, n° étudiant : {self.student_nbr}"


def find_student_by_id(id_number: int) -> Student:
    """
    Renvoit l'objet Student correspondant à l'id_number
    :param id_number:

    """
    return next((s for s in Student.student_list if s.student_nbr == id_number), None)





