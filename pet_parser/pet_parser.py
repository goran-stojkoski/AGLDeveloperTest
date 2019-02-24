#!/usr/bin/env python
"""
The following class imports a JSON file from a web address and expects a list of persons with name, gender, age and a list of pets.
The class has a single static method which accepts the url for the JSON file, the type of pet requested (i.e. dog or cat) and the person field to group by
The method returns an alphabetically ordered list of tuple pairs with the group value in index position 0 and the pet name in index position 1
"""

import json
import static.constants
from urllib.request import urlopen
from exceptions.custom_exceptions import InvalidPersonGroupField, InvalidPetType


class PetParser:

    """
    This static method accepts the url for the JSON file, the type of pet requested (i.e. dog or cat) and the person field to group by
    The method returns an alphabetically ordered list of tuple pairs with the group value in index position 0 and the pet name in index position 1
    """

    @staticmethod
    def get_pet_names_by_field(pet_type, group_by_person_field):

        # Validate arguments
        if group_by_person_field.lower() not in static.constants.VALID_SELECTION_FIELDS['person_group']:
            raise InvalidPersonGroupField

        if pet_type.lower() not in static.constants.VALID_SELECTION_FIELDS['pet_types']:
            raise InvalidPetType

        with urlopen(static.constants.AGL_JSON_URL) as response:
            source = response.read()

        data = json.loads(source)

        # using list comprehension (lower() method used to ensure match regardless of case)
        pet_names = PetParser.pet_parser(data, pet_type, group_by_person_field)

        return sorted(pet_names)

    @staticmethod
    def pet_parser(json_data, pet_type, group_by_person_field):
        pet_names = [(person[group_by_person_field.lower()], pet['name'])   # create a tuple list of pet names paired with desired person field
                     for person in json_data                                     # loop through persons
                     if person['pets'] is not None                          # exclude persons without pets
                     for pet in person['pets']                              # loop through individual pets
                     if pet['type'].lower() == pet_type.lower()]            # extract requested pet type
        return sorted(pet_names)
