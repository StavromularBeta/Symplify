#!/usr/bin/env python
class DropGenerator:
    """
    This class generates a drop line. Each draw line must be followed by a drop line.

    Method Hierarchy:

    drop_generator
        generate_known_variables
            drop_or_not
        generate_unknown_variables
        generate_drop_line
    """

    def __init__(self, drop_volume, drop_location, drop_coordinates, change_tip):
        """This class receives 4 variables: drop_volume (the amount, in microlitres, to be dropped
        into the drop location at the drop coordinates), drop_location (the tray the volume is being dropped in to),
        drop_coordinates (the coordinates on the tray the volume is being dropped into) and change_tip - "Y" indicates that
        the tip should be ejected and changed after the volume drop, "N" indicates that the tip shouldn't be ejected.

        the drop_line is the string of code that Symbiot reads."""
        self.drop_volume = drop_volume
        self.drop_location = drop_location
        self.drop_coordinates = drop_coordinates
        self.change_tip = change_tip
        self.drop_line = 'string'

    def drop_generator(self):
        """This function generates the known variables, then generates the unknown variables. It uses these to generate
        the drop line, updates the drop line, and returns the drop_line."""
        known_variables = self.generate_known_variables()
        known_and_unknown_variables = self.generate_unknown_variables(known_variables)
        drop_line = self.generate_drop_line(known_and_unknown_variables)
        self.drop_line = drop_line
        return drop_line

    def generate_known_variables(self):
        """This function creates the correct strings representing each known variable. known_variables_1 contains the
        information for the volume and the location. known_variables_2 contains the coordinates. known_variables_3
        contains information on whether or not to exchange the tip post-drop. These are then combined into a list and
        returned."""
        known_variables_1 = "C;"+str(self.drop_volume)+";"+str(self.drop_location)
        known_variables_2 = str(self.drop_coordinates[0])+";"+str(self.drop_coordinates[1])
        known_variables_3 = self.drop_or_not()
        known_variables = [known_variables_1,known_variables_2,known_variables_3]
        return known_variables

    def drop_or_not(self):
        """
        This function contains an if statement that returns the appropriate code for each condition (Y or N). If
        neither Y or N is detected, the function returns the least damaging instruction - to change the tip, which
        reduces the risk of the test failing.

        note that the 6 digit code accompanying the 1 or the 0 is technically unknown. The '70' is for drop and '62'
        is for don't drop, but the other 4 numbers are anybody's guess.
        """
        if self.change_tip == "Y":
            return ["262170", "1"]
        elif self.change_tip == "N":
            return ["262162", "0"]
        else:
            return ["262170", "1"]

    def generate_unknown_variables(self, known_variables):
        """This function first generates the three unknown variables, combines them with the known ones, and returns
        all variables as a list - the order of this list is important."""
        unknown_four = 0
        unknown_five = 1
        unknown_seven = 0
        known_and_unknown_variables = [known_variables[0],
                                       known_variables[2][0],
                                       known_variables[1],
                                       str(unknown_four),
                                       str(unknown_five),
                                       known_variables[2][1],
                                       str(unknown_seven)]
        return known_and_unknown_variables

    def generate_drop_line(self, known_and_unknown_variables):
        """This function generates the actual line of code Symbiot reads, it joins the variables up with semicolons."""
        drop_line = ';'.join(known_and_unknown_variables)+';'
        return drop_line