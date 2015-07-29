#!/usr/bin/env python
class RecievingPlateGenerator():

    def __init__(self, wells_per_row, wells_per_column, well_radius):
        self.wells_per_row = wells_per_row
        self.wells_per_column = wells_per_column
        self.well_radius = well_radius

    def well_generator(self):
        first_row_coordinates = self.first_row_generator()
        full_coordinates = self.remaining_coordinate_generator(first_row_coordinates)
        return full_coordinates

    def first_row_generator(self):
        first_row_coordinates = {}
        starting_x_0 = 4
        starting_y_0 = 4
        for Well in range(1, self.wells_per_row+1):
            one_first_row_coordinate = self.first_row_coordinate_generator(starting_x_0, starting_y_0)
            first_row_coordinates[Well] = one_first_row_coordinate[0]
            starting_x_0 = one_first_row_coordinate[1]
            starting_y_0 = one_first_row_coordinate[2]
        return first_row_coordinates

    def first_row_coordinate_generator(self, x_0, y_0):
        next_x_0 = x_0 + 2*self.well_radius
        next_y_0 = y_0
        x_1 = next_x_0
        y_1 = next_y_0 + 2*self.well_radius
        first_row_coordinate = [x_0, y_0, x_1, y_1]
        one_first_row_coordinate = [first_row_coordinate, next_x_0, next_y_0]
        return one_first_row_coordinate

    def remaining_coordinate_generator(self, first_row_coordinates):
        remaining_coordinates = first_row_coordinates
        for first_row_well, first_row_well_coordinates in remaining_coordinates.items():
            column_range_information = self.column_range_generator(first_row_well)
            for well in range(column_range_information[0], column_range_information[1], column_range_information[2]):
                row_of_well = (well - first_row_well)/8
                x_0 = first_row_well_coordinates[0]
                y_0 = first_row_well_coordinates[1]+(row_of_well*self.well_radius*2)
                x_1 = first_row_well_coordinates[2]
                y_1 = first_row_well_coordinates[3]+(row_of_well*self.well_radius*2)
                remaining_coordinates[well] = [x_0, y_0, x_1, y_1]
                self.enter_last_coordinate(well, column_range_information[1], column_range_information)
        return remaining_coordinates

    def column_range_generator(self, first_row_well):
        step = self.wells_per_row
        start = first_row_well + self.wells_per_row
        end = (self.wells_per_row * self.wells_per_column) - self.wells_per_row + first_row_well + 1
        return [start, end, step]

    def enter_last_coordinate(self, penultimate_coordinate, endrange, finished_row_coordinates):
        final_coordinates = finished_row_coordinates
        if penultimate_coordinate == endrange:
            final_x_0 = final_coordinates[penultimate_coordinate][0] + 2*self.RadiusOfWells
            final_y_0 = final_coordinates[penultimate_coordinate][1]
            final_x_1 = final_coordinates[penultimate_coordinate][2] + 2*self.RadiusOfWells
            final_y_1 = final_coordinates[penultimate_coordinate][3]
            ultimate_coordinate = [final_x_0, final_y_0, final_x_1, final_y_1]
            final_coordinates[penultimate_coordinate+1] = ultimate_coordinate

    def print_coordinates(self, coordinates_to_print):
        for well, coordinates in coordinates_to_print.items():
            print well, coordinates