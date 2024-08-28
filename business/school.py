# -*- coding: utf-8 -*-

"""
Classe School
"""

from dataclasses import dataclass, field

from rich.console import Console
from rich.table import Table

from models.course import Course
from models.student import Student
from models.teacher import Teacher


@dataclass
class School:
    """Couche métier de l'application de gestion d'une école,
    reprenant les cas d'utilisation et les spécifications fonctionnelles :
    - courses : liste des cours existants
    - teachers : liste des enseignants
    - students : liste des élèves"""

    courses: list[Course] = field(default_factory=list)
    teachers: list[Teacher] = field(default_factory=list)
    students: list[Student] = field(default_factory=list)

    def add_course(self, course: Course) -> None:
        """Ajout du cours course à la liste des cours."""
        self.courses.append(course)

    def add_teacher(self, teacher: Teacher) -> None:
        """Ajout de l'enseignant teacher à la liste des enseignants."""
        self.teachers.append(teacher)

    def add_student(self, student: Student) -> None:
        """Ajout de l'élève spécifié à la liste des élèves."""
        self.students.append(student)

    # def display_courses_list(self) -> None:
    #     """Affichage de la liste des cours avec pour chacun d'eux :
    #     - leur enseignant
    #     - la liste des élèves le suivant"""
    #     for course in self.courses:
    #         print(f"cours de {course}")
    #         for student in course.students_taking_it:
    #             print(f"- {student}")
    #         print()

    # def display_courses_list(self) -> None:
    #
    #     console = Console()
    #
    #     table = Table(show_header=True, header_style="bold magenta",title="Cours dispensés par l'Ecole")
    #     table.add_column("ID", style="dim", width=12)
    #     table.add_column("Nom", style="dim", width=12)
    #
    #     table.add_column("Date de debut", style="dim", width=12)
    #     table.add_column("Date de fin", style="dim", width=12)
    #     table.add_column("Enseignant de ce cours", style="dim", width=12)
    #
    #     for course in self.courses:
    #         table.add_row(str(course.id),str(course.name), str(course.start_date), str(course.end_date),
    #                       course.teacher)
    #     console.print(table)
