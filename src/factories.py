from abc import ABC, abstractmethod

from DAO.address_dao import AddressDAO
from DAO.course_dao import CourseDAO
from DAO.person_dao import PersonDAO
from DAO.student_dao import StudentDAO
from DAO.teacher_dao import TeacherDAO
from models.adress import Adress
from models.course import Course
from models.person import Person
from models.student import Student
from models.teacher import Teacher


class Creator(ABC):

    @abstractmethod
    def factory_method(self, information_source):
        """
        Méthode abstraite qui doit être implémentée.
        Cette méthode prend une source d'information en entrée et est censée renvoyer un nouvel objet.
        """
        pass


class CourseCreator(Creator):
    def factory_method(self, information_source: dict):
        course = Course.create_course(information_source['name'], information_source[
            'start_date'],
                                                    information_source['end_date'])
        course.id = information_source['id_course']


class PersonCreator(Creator):
    def factory_method(self, information_source: dict):
        person = Person.create_person(information_source['first_name'], information_source['last_name'],
                                      information_source['age'])
        person.id = information_source['id_person']
        person.address = information_source['id_address']


class AdressCreator(Creator):
    def factory_method(self, information_source: dict):
        adress = Adress.create_adress(information_source['street'], information_source['city'],
                                      information_source['postal_code'])
        adress.id = information_source['id_address']


class TeacherCreator(Creator):
    def factory_method(self, information_source: dict):
        teacher = Teacher.create_teacher(information_source['first_name'],
                                         information_source['last_name'],
                                         information_source['age'],
                                         information_source['start_date'])
        teacher.id = information_source['id_teacher']


class StudentCreator(Creator):

    def factory_method(self, information_source: dict):
        student = Student.create_student(information_source['first_name'],
                                         information_source['last_name'],
                                         information_source['age'])
        student.id = information_source['student_nbr']


def create_teachers_from_query_results():
    """
    Crée des objets Teacher à partir de la base de données
    """
    teacher = TeacherDAO()
    results: list[dict] = teacher.query_all()
    list(map(TeacherCreator().factory_method, results))


def create_courses_from_query_results():
    """
    Crée des objets Course à partir de la base de données
    """
    course = CourseDAO()
    results: list[dict] = course.query_all()
    list(map(CourseCreator().factory_method, results))


def create_persons_from_query_results():
    """
    Crée des objets Person à partir de la base de données
    """
    person = PersonDAO()
    results: list[dict] = person.query_all()
    list(map(PersonCreator().factory_method, results))


def create_adresses_from_query_results():
    """
    Crée des objets Adress à partir de la base de données
    """
    adress = AddressDAO()
    results: list[dict] = adress.query_all()
    list(map(AdressCreator().factory_method, results))


def creat_students_from_query_results():
    """
    Crée des objets Student à partir de la base de données
    """
    student_manager = StudentDAO()
    results: list[dict] = student_manager.query_all()
    list(map(StudentCreator().factory_method, results))
