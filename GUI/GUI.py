#!/usr/bin/env python
import Tkinter as tk
from WellGenerator import RecievingPlateGenerator
from SampleRackGenerator import SampleRackGenerator

# for the grid
wells_in_row = 8
wells_in_column = 8
radius_of_wells = 20
last_well = wells_in_row*wells_in_column

#for the samples
large_samples = 4
small_samples = 4
large_sample_radius = 20

grid_to_generate = RecievingPlateGenerator(wells_in_row, wells_in_column, radius_of_wells)
sample_rack = SampleRackGenerator(large_samples, small_samples, large_sample_radius)
sample_coordinates = sample_rack.sample_generator()
coordinates_of_wells = grid_to_generate.well_generator()
x = coordinates_of_wells[last_well][2]
y = coordinates_of_wells[last_well][3]


class Application(tk.Frame):  # Application class inherits from Tkinter's Frame class

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)  # calls the constructor for the parent class, Frame
        self.grid()   # so the application actually appears on screen
        self.create_widgets()

    def create_widgets(self):
        self.quit_button = tk.Button(self, text='Exit Symplify', command=self.quit)  # creates a button labeled Quit
        self.recieving_plate = self.recieving_plate_generator()
        self.solution_plate = self.solution_plate_generator()
        self.recieving_plate.grid()
        self.solution_plate.grid()
        self.quit_button.grid()  # places the button in the application

    def recieving_plate_generator(self):
        self.recieving_plate = tk.Canvas(self, width=x, height=y)
        for keys, values in coordinates_of_wells.items():
            oval = self.recieving_plate.create_oval(values[0], values[1], values[2], values[3])
        return self.recieving_plate

    def solution_plate_generator(self):
        self.solution_plate = tk.Canvas(self, width=x, height=4*RadiusOfWell, bg='#1E90FF')
        for keys, values in sample_coordinates.items():
            oval = self.solution_plate.create_oval(values[0], values[1], values[2], values[3])
        return self.solution_plate

app = Application()
app.master.title('Sample application')
app.mainloop()

# instantiating, giving a title, Starting the main loop.