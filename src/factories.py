from abc import ABC, abstractmethod

from DAO.person_dao import PersonManager
from models.person import Person
from src.table_name import TableName
from DAO.course_dao import CourseManager
from models.course import Course


class Creator(ABC):
    @abstractmethod
    def factory_method(self, information_source):
        pass


class CourseCreator(Creator):
    def factory_method(self, information_source: dict):
        Course.create_course(information_source['name'], information_source['start_date'],
                             information_source['end_date'])
        Course.id = information_source['id_course']


class PersonCreator(Creator):
    def factory_method(self, information_source: dict):
        Person.create_person(information_source['first_name'], information_source['last_name'],
                             information_source['age'], information_source['id_address'])
        Person.id = information_source['id_person']

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


