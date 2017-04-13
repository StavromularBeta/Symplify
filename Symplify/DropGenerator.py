#!/usr/bin/env python
class DropGenerator():

    def __init__(self, drop_volume, drop_location, drop_coordinates, change_tip):
        self.drop_volume = drop_volume
        self.drop_location = drop_location
        self.drop_coordinates = drop_coordinates
        self.change_tip = change_tip
        self.drop_line = 'string'

    def drop_generator(self):
        known_variables = self.generate_known_variables()
        known_and_unknown_variables = self.generate_unknown_variables(known_variables)
        drop_line = self.generate_drop_line(known_and_unknown_variables)
        self.drop_line = drop_line
        return drop_line

    def generate_known_variables(self):
        known_variables_1 = "C;"+str(self.drop_volume)+";"+str(self.drop_location)
        known_variables_2 = str(self.drop_coordinates[0])+";"+str(self.drop_coordinates[1])
        known_variables_3 = self.drop_or_not()
        known_variables = [known_variables_1,known_variables_2,known_variables_3]
        return known_variables

    def drop_or_not(self):
        if self.change_tip == "Y":
            return ["262170", "1"]
        elif self.change_tip == "N":
            return ["262162", "0"]
        else:
            return ["262170", "1"]

    def generate_unknown_variables(self, known_variables):
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
        drop_line = ';'.join(known_and_unknown_variables)+';'
        return drop_line
