from rich.console import Console
from DAO.student_dao import StudentDAO
from models.person import Person
from models.student import Student, find_student_by_id

from src.display import DisplaySchoolCourses, clear_screen, DisplayStudents, DisplayTeachers, modify_student, \
    modify_cours, rich_input
from src.factories import create_courses_from_query_results, creat_students_from_query_results, \
    create_teachers_from_query_results, create_persons_from_query_results, create_adresses_from_query_results
from src.sync import sync_student_course_enrollment, sync_person_addess, sync_student_and_person_addess, \
    sync_teacher_and_person_addess, add_teacher_to_course
from src.utils import student_creator


def init():
    """
    Initialise la base de données
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
    sync_teacher_and_person_addess()
    add_teacher_to_course()
    sync_student_and_person_addess()


def main():
    while True:
        clear_screen()

        console = Console()
        display_school_courses = DisplaySchoolCourses()
        display_students = DisplayStudents()
        display_teachers = DisplayTeachers()
        t1 = display_school_courses.display()
        t2 = display_students.display()
        t3 = display_teachers.display()

        console.print(t1, t2, t3, justify='center')

        response = rich_input('\n\tModifier un Etudiant ou un Cours ? :')
        if 'etudiant'.find(response.lower()) != -1:
            modify_student()
            continue

        elif 'cours'.find(response.lower()) != -1:
            modify_cours()
            continue


if __name__ == "__main__":
    init()
    main()
