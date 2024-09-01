import os
import platform
from abc import abstractmethod, ABC
from datetime import datetime

from rich import box
from rich.table import Table
from rich.console import Console


from DAO.course_dao import CourseDAO
from DAO.person_dao import PersonDAO
from DAO.student_dao import StudentDAO
from models.course import Course, find_course_by_id
from models.person import find_person_by_id
from models.student import Student, find_student_by_id
from models.teacher import Teacher

import time
from rich.progress import track


class Display(ABC):

    @abstractmethod
    def display(self):
        """
        Affiche l'interface graphique
        :return:
        """
        pass


class DisplaySchoolCourses(Display):

    def display(self):
        console = Console()
        terminal_width = console.size.width - 4

        table = Table(show_header=True, title="\n\n\nCours dispensés par l'Ecole",
                      box=box.SQUARE, width=terminal_width, header_style="dodger_blue1",
                      border_style='grey42')
        table.add_column("ID", style="deep_sky_blue1", width=1, justify="right")
        table.add_column("Nom", style="dim", width=12, justify="center")

        table.add_column("Date de debut", style="dim", width=12, justify="center")
        table.add_column("Date de fin", style="dim", width=12, justify="center")
        table.add_column("Enseignant de ce cours", style="plum2", width=12, justify="left")

        for course in Course.course_list:
            table.add_row(str(course.id), str(course.name), str(course.start_date), str(course.end_date),
                          str(f"{course.teacher.first_name}  {course.teacher.last_name}"))

        return table


class DisplayStudents(Display):

    def display(self):
        console = Console()
        terminal_width = console.size.width - 4
        table = Table(show_header=True, title="\n\n\nEtudiants presents dans l'Ecole",
                      box=box.SQUARE, width=terminal_width, header_style="dodger_blue1",
                      border_style='grey42')
        table.add_column("n° Etudiant", style="deep_sky_blue1", width=1, justify="right")
        table.add_column("Prenom", style="plum2", width=1, justify="center")

        table.add_column("Nom", style="plum2", width=1, justify="center")
        table.add_column("Age", style="dim", width=1, justify="center")
        table.add_column("Addresse", style="dim", width=12, justify="left")
        table.add_column("Cours suivis", style="dim", width=12, justify="left", min_width=400)

        for student in Student.student_list:
            table.add_row(str(student.id), str(student.first_name), str(student.last_name), str(student.age),
                          str(student.address), ", ".join(student.courses_taken))
        # console.print(table)
        return table


class DisplayTeachers(Display):
    def display(self):
        console = Console()
        terminal_width = console.size.width - 4
        table = Table(title="\nEnseignants presents dans l'Ecole",title_style="bright_white",
                      box=box.SQUARE, width=terminal_width, header_style="dodger_blue1",
                      border_style='grey42')
        table.add_column("ID", style="deep_sky_blue1", width=1, justify="right")
        table.add_column("Prenom", style="plum2", width=2, justify="center")

        table.add_column("Nom", style="plum2", width=1, justify="center")
        table.add_column("Age", style="dim", width=1, justify="center")
        table.add_column("Addresse", style="dim", width=12, justify="left")
        table.add_column("Cours enseignés", style="dim", width=12, justify="left", no_wrap=True)

        for teacher in Teacher.teacher_list:
            table.add_row(str(teacher.id), str(teacher.first_name), str(teacher.last_name), str(teacher.age),
                          str(teacher.address), str(teacher.courses_teached))
        # console.print(table)
        return table


def rich_input(prompt):
    """
    Cette fonction affiche une boite de dialogue avec un texte de prompt et renvoie la saisie utilisateur.
    Elle utilise la bibliothèque rich.
    """
    console = Console()
    return console.input(f"[yellow3]{prompt}[/yellow3] ")


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


def modify_student():
    """
    Permet de modifier un etudiant
    :return:
    """
    pm = PersonDAO()
    sm = StudentDAO()
    response = rich_input('\n\t\tID de l\'Etudiant ? :')
    id_person = sm.find_id_person_by_student_nbr(int(response))
    student_to_modifie = find_student_by_id(int(response))
    person_to_modifie = find_person_by_id(id_person[0]['id_person'])
    print(f"\n\t\t\t{person_to_modifie}")
    person_to_modifie.first_name = rich_input('\n\t\tNouveau Prenoms :')
    person_to_modifie.last_name = rich_input('\n\t\tNouveau Nom :')
    person_to_modifie.age = rich_input('\n\t\tNouveau Age :')
    print(f"\t\t{person_to_modifie}")
    pm.update(person_to_modifie)


def modify_cours():
    """
    Permet de modifier un cours
    :return:
    """
    cm = CourseDAO()
    response = rich_input('\n\tID du du Cours ? :')
    course_to_modify: Course = find_course_by_id(int(response))

    print(f"\t\t{course_to_modify}")
    course_to_modify.name = rich_input('\n\t\tNouveau Nom du Cours :')
    course_to_modify.start_date = (datetime.strptime
                                   (rich_input('\n\t\tNouvelle Date de debut (''yyyy-mm-dd) :'),
                                    '%Y-%m-%d').date())
    course_to_modify.end_date = (datetime.strptime
                                 (rich_input('\n\t\tNouvelle Date de fin (''yyyy-mm-dd) :'),
                                  '%Y-%m-%d').date())
    course_to_modify.teacher = int(rich_input('\n\t\tNouvel enseignant :'))
    cm.update(course_to_modify)




