# -*- coding: utf-8 -*-

"""
Classe Course
"""

# pour simplifier les annotations de types des classes non importées à l'exécution
# (teacher: Teacher plutôt que teacher: 'Teacher')
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, TYPE_CHECKING

# pour éviter une circularité des imports à l'exécution,
# les classes Student et Teacher important la classe Course
if TYPE_CHECKING:
    from .student import Student
    from .teacher import Teacher


@dataclass
class Course:
    """Cours enseigné à l'école :
    - id : identifiant du cours
    - name : nom du cours
    - start_date : date de début
    - end_date : date de fin
    - teacher : enseignant de ce cours
    - students_taking_it : élèves qui suivent ce cours
    """
    course_list = []

    id: int = field(default=None, init=False)
    name: str
    start_date: date
    end_date: date
    teacher: Optional[Teacher] = field(default=None, init=False)
    students_taking_it: list[Student] = field(default_factory=list, init=False)

    @classmethod
    def create_course(cls, name: str, start_date, end_date):
        """
        Crée un nouvel objet Course et l'ajoute à la liste des cours.
        :param name:
        :param start_date:
        :param end_date:
        :return:
        """
        new_course = cls(name=name, start_date=start_date, end_date=end_date)
        Course.course_list.append(new_course)
        return new_course

    def set_teacher(self, teacher: Teacher) -> None:
        """Indique quel est l'enseignant de ce cours."""
        if teacher != self.teacher:
            # il y a quelque chose à faire
            if self.teacher is not None:
                # un autre enseignant enseignait précédemment ce cours, qui ne doit
                # donc plus faire partie de la liste des cours qu'il enseigne
                teacher.courses_teached.remove(self)
            # ajout du cours à l'enseignant indiqué
            teacher.courses_teached.append(self)

    def add_student(self, student: Student) -> None:
        """Ajoute :
        - l'étudiant student à la liste des étudiants suivant ce cours
        - ce cours à la liste des cours que suit cet étudiant"""
        self.students_taking_it.append(student)
        student.courses_taken.append(self)

    def __str__(self) -> str:
        course_str = f"{self.name} ({self.start_date} – {self.end_date}),\n"
        course_str += f"enseigné par {self.teacher}" \
            if self.teacher is not None else "pas d'enseignant affecté"
        return course_str


def find_course_by_id(id_number: int) -> Course:
    """Renvoit l'objet Course correspondant à l'id_number
    :param id_number:
    """
    return next((s for s in Course.course_list if s.id == id_number), None)