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
        """
        This function first generates known_variables_1, which contains information on the test number and name. it
        then creates the string that represents the liquid reservoir (this tells symbiot where the vials are). It then
        creates the string that represents the destination rack (telling symbiot where to put liquid). When you
        write drop commands, you tell Symbiot to drop in the destination rack, and this destination rack is defined by
        this variable in this line. These three variables are returned as the list known_variables.
        """
        known_variables_1 = 'T;' + str(self.test_number) + ';' + self.test_name
        liquid_reservoir_location = 'Vial1'
        destination_rack = 'My Fake Maldi tray'
        known_variables = [known_variables_1, liquid_reservoir_location, destination_rack]
        return known_variables

    def generate_unknown_variables(self, known_variables):
        """This function first generates the three unknown variables, combines them with the known ones, and returns
        all variables as a list - the order of this list is important."""
        max_time = 0
        unknown_one = 0
        utilization = 0
        known_and_unknown_variables = [known_variables[0],
                                       str(max_time),
                                       str(unknown_one),
                                       str(utilization),
                                       known_variables[1],
                                       known_variables[2]]
        return known_and_unknown_variables

    def test_line_generator(self, known_and_unknown_variables):
        """This function generates the actual line of code Symbiot reads, it joins the variables up with semicolons."""
        test_line = ';'.join(known_and_unknown_variables)+';'
        return test_line