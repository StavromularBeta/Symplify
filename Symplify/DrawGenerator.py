#!/usr/bin/env python
class DrawGenerator():

    def __init__(self, draw_volume, draw_location):
        self.draw_volume = draw_volume
        self.draw_location = draw_location
        self.draw_line = 'string'

    def draw_generator(self):
        known_variables = self.generate_known_variables()
        known_and_unknown_variables = self.generate_unknown_variables(known_variables)
        draw_line = self.generate_draw_line(known_and_unknown_variables)
        self.draw_line = draw_line
        return draw_line

    def generate_known_variables(self):
        known_variables = "C;"+str(self.draw_volume)+";"+str(self.draw_location)
        return known_variables

    def generate_unknown_variables(self, known_variables):
        unknown_one = 262210
        unknown_two = 0
        unknown_three = 0
        unknown_four = 0
        unknown_five = 2
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
        draw_line = ';'.join(known_and_unknown_variables)+';'
        return draw_line