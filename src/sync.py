from DAO.student_dao import StudentManager
from models.adress import find_adress_by_id
from models.course import find_course_by_id
from models.person import Person, find_person_by_adress_id, find_person_by_id
from models.student import find_student_by_id


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
