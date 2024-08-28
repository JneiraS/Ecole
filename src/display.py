import os
import platform
from abc import abstractmethod, ABC

from rich import box
from rich.table import Table

from business.school import School
from models.course import Course
from models.student import Student


class Display(ABC):

    @abstractmethod
    def display(self):
        """
        Affiche l'interface graphique
        :return:
        """
        pass


class DisplaySchoolCourses(Display):
    def __init__(self):
        self.school = School()

    def display(self):
        table = Table(show_header=True, title="Cours dispensés par l'Ecole",
                      box=box.MINIMAL)
        table.add_column("ID", style="dim", width=12, justify="right")
        table.add_column("Nom", style="dim", width=12, justify="center")

        table.add_column("Date de debut", style="dim", width=12, justify="center")
        table.add_column("Date de fin", style="dim", width=12, justify="center")
        table.add_column("Enseignant de ce cours", style="dim", width=12, justify="left")

        for course in Course.course_list:
            table.add_row(str(course.id), str(course.name), str(course.start_date), str(course.end_date),
                          course.teacher)

        return table


class DisplayStudents(Display):
    def __init__(self):
        self.school = School()

    def display(self):
        table = Table(show_header=True, title="\nEtudiants presents dans l'Ecole",
                      box=box.MINIMAL)
        table.add_column("n° Etudiant", style="dim", width=12, justify="right")
        table.add_column("Prenom", style="dim", width=12, justify="center")

        table.add_column("Nom", style="dim", width=12, justify="center")
        table.add_column("Age", style="dim", width=12, justify="center")
        table.add_column("Addresse", style="dim", width=12, justify="left")
        table.add_column("Cours suivis", style="dim", width=12, justify="left", min_width=400)

        for student in Student.student_list:
            table.add_row(str(student.id), str(student.first_name), str(student.last_name), str(student.age),
                          str(student.address), str(student.courses_taken))
        # console.print(table)
        return table


def clear_screen() -> None:
    """
    Efface l'écran sur le terminal, en fonction du systeme
    :return:
    """
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
