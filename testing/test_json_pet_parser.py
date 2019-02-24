#!/usr/bin/env python
"""
The following class tests if the get_pet_names_by_field from the json_pet_parser module is working correctly.
It tests two valid input conditions, an invalid pet type exception and an invalid person group exception
"""

import unittest
import static.constants
from pet_parser.pet_parser import PetParser
from exceptions.custom_exceptions import InvalidPetType, InvalidPersonGroupField


class PetParserTest(unittest.TestCase):

    def setUp(self):
        self.expected_gender_cat = [('Female', 'Garfield'),
                                    ('Female', 'Simba'),
                                    ('Female', 'Tabby'),
                                    ('Male', 'Garfield'),
                                    ('Male', 'Jim'),
                                    ('Male', 'Max'),
                                    ('Male', 'Tom')]
    # Run Unit Test
    def test_pet_parser(self):
        gender_cat = PetParser.pet_parser(static.constants.mock_data, 'Cat', 'gender')
        self.assertEqual(self.expected_gender_cat, gender_cat)

    # Run Integration Tests
    def test_gender_cat(self):
        gender_cat = PetParser.get_pet_names_by_field('Cat', 'gender')
        self.assertEqual(self.expected_gender_cat, gender_cat)

    def test_age_dogs(self):
        expected_age_dog = [(23, 'Fido'), (40, 'Sam')]
        age_dog = PetParser.get_pet_names_by_field('DoG', 'AGE')
        self.assertEqual(expected_age_dog, age_dog)


class CustomExceptionsTest(unittest.TestCase):

    def test_pet_type_exception(self):
        self.assertRaises(InvalidPetType, PetParser.get_pet_names_by_field, 'Bird', 'gender')

    def test_person_group_exception(self):
        self.assertRaises(InvalidPersonGroupField, PetParser.get_pet_names_by_field, 'Cat', 'height')


if __name__ == '__main__':
    unittest.main()
