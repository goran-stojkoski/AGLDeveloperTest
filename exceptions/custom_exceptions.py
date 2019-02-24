#!/usr/bin/env python
"""
The following module contains exceptions specific to the AGL Test
"""


class AGLTestExceptions(Exception):
    pass


class InvalidPersonGroupField(AGLTestExceptions):
    pass


class InvalidPetType(AGLTestExceptions):
    pass
