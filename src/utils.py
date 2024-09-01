import hashlib

import models
from DAO import student_dao
from DAO.address_dao import AddressDAO
from DAO.person_dao import PersonDAO
from models.adress import Adress


def generate_unique_numeric_id_from_string(concatenation: str) -> int:
    """
    Permet de convertir une chaine de caractères en un nombre "unique" de 8 caracteres maximum.
    """
    nom_bytes = concatenation.encode('utf-8')
    hash_object = hashlib.sha256(nom_bytes)
    hex_dig = hash_object.hexdigest()
    chiffre_8 = hex_dig[:6]
    return int(chiffre_8, 16)


def student_creator(street, city, postal_code, first_name, last_name, age, course_id: int) -> None:
    """
    Crée une nouvelle entité étudiant en générant un identifiant unique basé sur le nom et l'âge de
    l'étudiant, en créant une nouvelle adresse et en associant l'adresse à l'étudiant.
    """
    try:
        address_manager = AddressDAO()
        person_manager = PersonDAO()
        student_manager = student_dao.StudentDAO()

        student_id = generate_unique_numeric_id_from_string(first_name + last_name)

        # Creer une nouvelle adresse
        adress = Adress.create_adress(street, city, postal_code, )
        id_adress = address_manager.create(adress)

        # Creer une nouvelle personne
        person = models.person.Person.create_person(first_name, last_name, age)
        person.address = adress
        person_id = person_manager.create(person, id_adress)

        # Creer un nouvel etudiant
        student_manager.create(person_id, student_id)

        student_manager.assign_student_to_course(student_id, course_id)

    except Exception as e:
        print(f"Une erreur s'est produite lors de la création de l'étudiant : {e}")
        raise
