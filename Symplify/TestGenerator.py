#!/usr/bin/env python
class TestGenerator:
    """
    This class generates the test line. This line contains information about the sequence of events in the script. There
    can be multiple tests per group.

    Method Hierarchy:

    test_generator
        generate_known_variables
        generate_unknown_variables
        test_line_generator
    """

    def __init__(self, test_name, test_number):
        """
        the test name and number are the name and number of the test, which is the sequence of events in the script. The
        test line is a string containing the information read by symbiot.
        """
        self.test_name  = test_name
        self.test_number = test_number
        self.test_line = 'string'

    def test_generator(self):
        """
        This function generates the known variables, then generates the unknown variables. It then generates the line
        of Symbiot Code that represents a Test. Then, this function updates the test_line object and also returns the
        test_line.
        """
        known_variables = self.generate_known_variables()
        known_and_unknown_variables = self.generate_unknown_variables(known_variables)
        test_line = self.test_line_generator(known_and_unknown_variables)
        self.test_line = test_line
        return test_line

    def generate_known_variables(self):
        known_variables = 'T;' + str(self.test_number) + ';' + self.test_name
        return known_variables

    def generate_unknown_variables(self, known_variables):
        max_time = 0
        unknown_one = 0
        utilization = 0
        predilution_rack_optional = 'Vial1'
        destination_rack = 'My Fake Maldi Tray'
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