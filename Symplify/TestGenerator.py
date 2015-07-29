#!/usr/bin/env python
class TestGenerator():

    def __init__(self, test_name, test_number):
        self.test_name  = test_name
        self.test_number = test_number
        self.test_line = 'string'

    def test_generator(self):
        known_variables = self.generate_known_variables()
        known_and_unknown_variables = self.generate_unknown_variables(known_variables)
        test_line = self.GenerateTestLine(known_and_unknown_variables)
        self.test_line = test_line
        return test_line

    def generate_known_variables(self):
        known_variables = 'T;' + str(self.test_number) + ';' + self.test_name
        return known_variables

    def generate_unknown_variables(self, known_variables):
        #These variables have unknown functions and as such have odd names
        #Taken straight from the menus that generate these values on the Symbiot side
        max_time = 0
        unknown_one = 0
        utilization = 0
        predilution_rack_optional = ''
        destination_rack = 'MALDI 10X10 on row 16'
        known_and_unknown_variables = [known_variables,
                                       str(max_time),
                                       str(unknown_one),
                                       str(utilization),
                                       str(predilution_rack_optional),
                                       str(destination_rack)]
        return known_and_unknown_variables

    def test_line_generator(self, known_and_unknown_variables):
        test_line = ';'.join(known_and_unknown_variables)+';'
        return test_line