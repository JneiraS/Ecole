from datetime import datetime

from rich.console import Console
from rich.panel import Panel

from DAO.course_dao import CourseManager
from DAO.student_dao import StudentManager
from models.adress import find_adress_by_id
from models.course import find_course_by_id, Course
from models.person import Person, find_person_by_adress_id, find_person_by_id
from models.student import Student, find_student_by_id
from src.display import DisplaySchoolCourses, clear_screen, DisplayStudents, DisplayTeachers, modify_student, \
    modify_cours, rich_input
from src.factories import create_courses_from_query_results, creat_students_from_query_results, \
    create_teachers_from_query_results, create_persons_from_query_results, create_adresses_from_query_results


def init():
    """
    Initialise les donées de l'application
    :return:
    """
    # chargement des elements de la base de données
    creat_students_from_query_results()
    create_teachers_from_query_results()
    create_courses_from_query_results()
    create_persons_from_query_results()
    create_adresses_from_query_results()
    sync_student_course_enrollment()
    sync_person_addess()
    sync_student_and_person_addess()





def sync_student_course_enrollment():
    """
     Cette fonction connecte l'objet StudentManager à la base de données et récupère les lignes du tableau
     « takes ». Pour chaque ligne, elle recherche l'étudiant et le cours correspondant dans leurs listes
      respectives et ajoute le cours à la liste des cours suivis par l'étudiant.à la liste des cours suivis
      par l'étudiant.
    :return:
    """
    sm = StudentManager()
    result = sm.course_taken_by_student()
    for i in result:
        student = find_student_by_id(i['student_nbr'])
        course = find_course_by_id(i['id_course'])
        student.add_course(course)


def sync_person_addess():
    """
    OK
    :return:
    """

    for person in Person.person_list:
        if person.address is not None:
            person_to_update_address = (find_person_by_adress_id(person.address))

            address = find_adress_by_id(person_to_update_address.address)

            person_to_update_address.address = address


def sync_student_and_person_addess():
    sm = StudentManager()
    result = sm.get_all_student_ids()
    for i in result:
        person = find_person_by_id(i['id_person'])
        student = find_student_by_id(i['student_nbr'])

        student.address = person.address


def main():
    while True:
        clear_screen()
        console = Console()
        console.print(Panel("--  ECOLE MANAGER  --", border_style="red"), justify="center")

        display_school_courses = DisplaySchoolCourses()
        display_students = DisplayStudents()
        display_teachers = DisplayTeachers()
        t1 = display_school_courses.display()
        t2 = display_students.display()
        t3 = display_teachers.display()

        console.print(t1, t2, t3, justify='center')

        response = rich_input('\n\t\tModifier un Etudiant ou un Cours ? :')
        if 'Etudiant'.lower().find(response.lower()) != -1:
            modify_student()
            continue

        elif 'Cours'.lower().find(response.lower()) != -1:
            modify_cours()
            continue

if __name__ == "__main__":

    init()
    main()
