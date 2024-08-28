from abc import ABC, abstractmethod

from DAO.address_dao import AddressManager
from DAO.course_dao import CourseManager
from DAO.person_dao import PersonManager
from DAO.teacher_dao import TeacherManager
from models.course import Course
from models.person import Person
from models.adress import Adress
from models.teacher import Teacher
from src.table_name import TableName


class Creator(ABC):
    @abstractmethod
    def factory_method(self, information_source):
        pass


class CourseCreator(Creator):
    def factory_method(self, information_source: dict):
        course = Course.create_course(information_source['name'], information_source['start_date'],
                                      information_source['end_date'])
        course.id = information_source['id_course']


class PersonCreator(Creator):
    def factory_method(self, information_source: dict):
        person = Person.create_person(information_source['first_name'], information_source['last_name'],
                                      information_source['age'], information_source['id_address'])
        person.id = information_source['id_person']


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


def create_teachers_from_query_results():
    """
    Crée des objets Teacher à partir de la base de données
    """
    teacher = TeacherManager()
    results: list[dict] = teacher.query_all(TableName.TEACHER.value)
    list(map(TeacherCreator().factory_method, results))


def create_courses_from_query_results():
    """
    Crée des objets Course à partir de la base de données
    """
    course = CourseManager()
    results: list[dict] = course.query_all(TableName.COURSE.value)
    list(map(CourseCreator().factory_method, results))


def create_persons_from_query_results():
    """
    Crée des objets Person à partir de la base de données
    """
    person = PersonManager()
    results: list[dict] = person.query_all(TableName.PERSON.value)
    list(map(PersonCreator().factory_method, results))


def create_adresses_from_query_results():
    """
    Crée des objets Adress à partir de la base de données
    """
    adress = AddressManager()
    results: list[dict] = adress.query_all(TableName.ADDRESS.value)
    list(map(AdressCreator().factory_method, results))
