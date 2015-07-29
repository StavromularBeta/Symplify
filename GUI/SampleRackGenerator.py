#!/usr/bin/env python
class SampleRackGenerator():

    def __init__(self, number_of_large_samples, number_of_small_samples, radius_of_large_samples):
        self.number_of_large_samples = number_of_large_samples
        self.number_of_small_samples = number_of_small_samples
        self.radius_of_large_samples = radius_of_large_samples
        self.radius_of_small_samples = radius_of_large_samples/2

    def sample_generator(self):
        large_sample_coordinates = self.large_sample_generator()
        large_and_small_sample_coordinates = self.small_sample_generator(large_sample_coordinates)
        return large_and_small_sample_coordinates

    def large_sample_generator(self):
        large_sample_coordinates = {}
        starting_x_0 = 12
        starting_y_0 = 16
        for sample in range(self.number_of_large_samples):
            sample_coordinate = self.large_sample_coordinate_generator(starting_x_0, starting_y_0)
            starting_x_0 = sample_coordinate[4]
            large_sample_coordinates[sample] = [sample_coordinate[0],
                                                sample_coordinate[1],
                                                sample_coordinate[2],
                                                sample_coordinate[3]]
        return large_sample_coordinates

    def large_sample_coordinate_generator(self, starting_x_0, starting_y_0):
        x_1 = starting_x_0 + 2*self.radius_of_large_samples
        y_1 = starting_y_0 + 2*self.radius_of_large_samples
        next_x_0 = x_1 + 0.5*self.radius_of_large_samples
        return [starting_y_0, starting_y_0, x_1, y_1, next_x_0]

    def small_sample_generator(self, large_sample_coordinates):
        large_and_small_sample_coordinates = large_sample_coordinates
        key_of_last_large_sample = self.number_of_large_samples - 1
        last_well_coordinates = large_sample_coordinates[key_of_last_large_sample]
        small_sample_x_0_y_0 = self.small_x_0_y_0_generator(last_well_coordinates)
        small_x_0 = small_sample_x_0_y_0[0]
        small_y_0 = small_sample_x_0_y_0[1]
        for well in range(1,self.number_of_small_samples+1):
            small_well_index = well+(self.number_of_large_samples-1)
            small_sample_coordinate = self.small_well_coordinate_generator(small_x_0, small_y_0)
            small_x_0 = small_sample_coordinate[4]
            large_and_small_sample_coordinates[small_well_index] = [small_sample_coordinate[0],
                                                                    small_sample_coordinate[1],
                                                                    small_sample_coordinate[2],
                                                                    small_sample_coordinate[3]]
        return large_and_small_sample_coordinates

    def small_x_0_y_0_generator(self, last_well_coordinates):
        small_x_0 = last_well_coordinates[0] + 3*self.radius_of_large_samples
        small_y_0 = last_well_coordinates[1] + self.radius_of_small_samples
        return [small_x_0, small_y_0]

    def small_well_coordinate_generator(self, small_x_0, small_y_0):
        x_1 = small_y_0 + 2*self.radius_of_small_samples
        y_1 = small_y_0 + 2*self.radius_of_small_samples
        next_x_0 = x_1 + 0.5*self.radius_of_small_samples
        return [small_x_0, small_y_0, x_1, y_1, next_x_0]