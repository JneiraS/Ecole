from abc import ABC, abstractmethod

from DAO.course_dao import CourseManager
from models.course import Course


class Creator(ABC):
    @abstractmethod
    def factory_method(self, information_source):
        pass


class CourseCreator(Creator):
    def factory_method(self, information_source):
        Course.create_course(information_source['name'], information_source['start_date'],
                             information_source['end_date'])
        Course.id = information_source['id_course']


def create_courses_from_query_results():
    """
    Crée des objets Course à partir de la base de données
    """
    course = CourseManager()
    results: list[dict] = course.query_all('course')
    list(map(CourseCreator().factory_method, results))


create_courses_from_query_results()

print(list(Course._course_list))
