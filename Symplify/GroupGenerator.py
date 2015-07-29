#!/usr/bin/env python
class GroupGenerator():

    def __init__(self, group_name, group_number):
        self.group_name = str(group_name)
        self.group_number = group_number
        self.group_line = 'string'

    def group_generator(self):
        known_variables = self.known_variable_generator()
        known_and_unknown_variables = self.unknown_variable_generator(known_variables)
        group_line = self.group_line_generator(known_and_unknown_variables)
        self.group_line = group_line
        return group_line

    def known_variable_generator(self):
        known_variables = 'G;' + str(self.group_number) + ';' + self.group_name
        return known_variables

    def unknown_variable_generator(self, known_variables):
        #These variables have unknown functions and as such have odd names
        #Taken straight from the menus that generate these values on the Symbiot side
        max_tests_per_plate = 1
        output_formats = 0
        optimizing_mode = 65
        known_and_unknown_variables = [known_variables,
                                       str(max_tests_per_plate),
                                       str(output_formats),
                                       str(optimizing_mode)]
        return known_and_unknown_variables

    def group_line_generator(self, known_and_unknown_variables):
        group_line = ';'.join(known_and_unknown_variables)+';'
        return group_line