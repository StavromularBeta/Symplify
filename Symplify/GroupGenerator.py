#!/usr/bin/env python
class GroupGenerator():
    """
    This class generates the line of code corresponding to the group that a particular test belongs to.

    Method Hierarchy:

    group_generator
        known_variable_generator
        unknown_variable_generator
        group_line_generator

    """

    def __init__(self, group_name, group_number):
        """
        The group name is the name of the group that the test belongs to. The group number is the number of the group.
        The group line is the object representing the line of Symbiot Code this class generates.
        """
        self.group_name = str(group_name)
        self.group_number = group_number
        self.group_line = 'string'

    def group_generator(self):
        """
        This function generates the known variables, then generates the unknown variables. It then generates the line
        of SymbiotCode that represents a group. Then, this function updates the group_line object and also returns the
        group_line.
        """
        known_variables = self.known_variable_generator()
        known_and_unknown_variables = self.unknown_variable_generator(known_variables)
        group_line = self.group_line_generator(known_and_unknown_variables)
        self.group_line = group_line
        return group_line

    def known_variable_generator(self):
        """
        This function combines the known variables as a string, without a trailing semi-colon.
        returns 'G;(group_number);(group_name)'.
        The known variables are currently the group_number, and the group_name.
        """
        known_variables = 'G;' + str(self.group_number) + ';' + self.group_name
        return known_variables

    def unknown_variable_generator(self, known_variables):
        """
        This function generates three unknown variables, giving them default values as their purpose is still unknown.
        The function then combines the known_variable string, and all of the unknown variables as strings, in a list.
        It returns this list.
        """
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
        """
        This function takes the list of known and unknown variables, in string form, and combines them with semicolons.
        It returns a string with each variable separated by a semi-colon, with one trailing at the end.
        """
        group_line = ';'.join(known_and_unknown_variables)+';'
        return group_line