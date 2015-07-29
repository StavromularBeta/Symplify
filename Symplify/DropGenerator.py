#!/usr/bin/env python
class DropGenerator():

    def __init__(self, drop_volume, drop_location):
        self.drop_volume = drop_volume
        self.drop_location = drop_location
        self.drop_line = 'string'

    def drop_generator(self):
        known_variables = self.generate_known_variables()
        known_and_unknown_variables = self.generate_unknown_variables(known_variables)
        drop_line = self.generate_drop_line(known_and_unknown_variables)
        self.drop_line = drop_line
        return drop_line

    def generate_known_variables(self):
        known_variables = "C;"+str(self.drop_volume)+";"+str(self.drop_location)
        return known_variables

    def generate_unknown_variables(self, known_variables):
        unknown_one = 262170
        unknown_two = 0
        unknown_three = 0
        unknown_four = 0
        unknown_five = 1
        unknown_six = 1
        unknown_seven = 0
        known_and_unknown_variables = [known_variables,
                                       str(unknown_one),
                                       str(unknown_two),
                                       str(unknown_three),
                                       str(unknown_four),
                                       str(unknown_five),
                                       str(unknown_six),
                                       str(unknown_seven)]
        return known_and_unknown_variables

    def generate_drop_line(self, known_and_unknown_variables):
        drop_line = ';'.join(known_and_unknown_variables)+';'
        return drop_line