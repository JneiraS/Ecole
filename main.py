from DAO.student_dao import StudentManager
from models.course import Course, find_course_by_id
from models.student import Student, find_student_by_id
from src.display import DisplaySchoolCourses, clear_screen, DisplayStudents

from rich.console import Console

from src.factories import create_courses_from_query_results, creat_students_from_query_results








def main():
    clear_screen()
    console = Console()

    create_courses_from_query_results()
    creat_students_from_query_results()

    sync_student_course_enrollment()

    display_school_courses = DisplaySchoolCourses()
    display_students = DisplayStudents()
    t1 = display_school_courses.display()
    t2 = display_students.display()

    console.print(t1, t2, style="white on blue", justify="center")


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


if __name__ == "__main__":
    main()
