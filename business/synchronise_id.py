import time
from abc import ABC, abstractmethod
from datetime import date

from DAO.course_dao import CourseDAO
from DAO.teacher_dao import TeacherDAO
from models.course import Course
from models.teacher import Teacher


class SynchroniseId(ABC):
    @abstractmethod
    def actualise_id(self, class_name):
        """
        Met à jour l'id de la classe avec celui correrspondant à l'entité de la base de données
        :param class_name:
        :return:
        """
        pass


class SynchroniseCourseId(SynchroniseId):

    def actualise_id(self, course: Course):
        course_manager = CourseDAO()
        last_course_id: int = course_manager.create(course)
        course.id = last_course_id


class SynchroniseTeacherId(SynchroniseId):

    def actualise_id(self, teacher: Teacher):
        teacher_manager = TeacherDAO()
        last_teacher_id: int = teacher_manager.create(teacher)
        teacher.id = last_teacher_id
