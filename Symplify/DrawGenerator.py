#!/usr/bin/env python
class DrawGenerator():
    """
    This class writes code corresponding to drawing liquid. It needs to be coupled to a drop step.

    Method hierarchy:

    draw_generator
        generate_known_variables
        generate_unknown_variables
        generate_draw_line

    """

    def __init__(self, draw_volume, draw_location):
        """
        The draw volume is the amount of liquid, in microlitres, to be drawn into the pipet tip. the draw location is
        the vial the liquid will be taken from. The draw_line variable represents the string returned by draw_generator.
        """
        self.draw_volume = draw_volume
        self.draw_location = draw_location
        self.draw_line = 'string'

    def draw_generator(self):
        """
        This function creates the draw_line. It first generates the known variables, then generates the unknown ones.
        It then combines the information into the draw line (a string).
        """
        known_variables = self.generate_known_variables()
        known_and_unknown_variables = self.generate_unknown_variables(known_variables)
        draw_line = self.generate_draw_line(known_and_unknown_variables)
        self.draw_line = draw_line
        return draw_line

    def generate_known_variables(self):
        """This function generates the known variables, as a string, without the trailing semi-colon.
        returns "C;(draw_volume);(draw_location)".
        The known variables are currently the draw volume and the draw location.
        """
        known_variables = "C;"+str(self.draw_volume)+";"+str(self.draw_location)
        return known_variables

    def generate_unknown_variables(self, known_variables):
        """
        This function takes the known variables string returned by the function generate_known_variables and creates
        the unknown ones (uses default values). It then combines the known and unknown variables as a list and returns
        that list, called known_and_unknown_variables.
        """
        unknown_one = 262210
        unknown_two = 0
        unknown_three = 0
        unknown_four = 0
        unknown_five = 1
        unknown_six = 0
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

    def generate_draw_line(self, known_and_unknown_variables):
        """
        This function takes the list of known and unknown variables, in string form, and combines them with semicolons.
        It returns a string with each variable separated by a semi-colon, with one trailing at the end.
        """
        draw_line = ';'.join(known_and_unknown_variables)+';'
        return draw_line
