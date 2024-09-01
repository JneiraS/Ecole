from DAO.course_dao import CourseDAO
from DAO.student_dao import StudentDAO
from DAO.teacher_dao import TeacherDAO
from models.adress import find_adress_by_id
from models.course import find_course_by_id
from models.person import Person, find_person_by_adress_id, find_person_by_id
from models.student import find_student_by_id
from models.teacher import find_teacher_by_id


def sync_student_course_enrollment():
    """
     Cette fonction connecte l'objet StudentManager à la base de données et récupère les lignes du tableau
     « takes ». Pour chaque ligne, elle recherche l'étudiant et le cours correspondant dans leurs listes
      respectives et ajoute le cours à la liste des cours suivis par l'étudiant.à la liste des cours suivis
      par l'étudiant.
    :return:
    """
    sm = StudentDAO()
    result = sm.course_taken_by_student()
    for i in result:
        student = find_student_by_id(i['student_nbr'])
        course = find_course_by_id(i['id_course'])
        try:
            student.add_course(course)
        except:
            pass


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
    sm = StudentDAO()
    result = sm.get_all_student_ids()
    for i in result:

        person = find_person_by_id(i['id_person'])
        print((i['student_nbr']))
        student = find_student_by_id(i['student_nbr'])
        print(student)

        try:
            student.address = person.address
        except:
            pass


def sync_teacher_and_person_addess():
    tm = TeacherDAO()
    result = tm.get_all_teacher_ids()
    for i in result:
        person = find_person_by_id(i['id_person'])
        teacher = find_teacher_by_id(i['id_teacher'])

        teacher.address = person.address


def add_teacher_to_course() -> None:
    """
    Affecte un enseignant à un cours sur la base des identifiants de cours.
    :return:
    """
    cm = CourseDAO()
    result = cm.get_all_course_ids()
    for i in result:
        teacher = find_teacher_by_id(i['id_teacher'])
        course = find_course_by_id(i['id_course'])

        course.teacher = teacher


