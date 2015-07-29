#!/usr/bin/env python
import Tkinter as tk
from WellGenerator import RecievingPlateGenerator
from SampleRackGenerator import SampleRackGenerator

# for the grid
WellsInRow = 8
WellsInColumn = 8
RadiusOfWell = 20
LastWell = WellsInRow*WellsInColumn

#for the samples
LargeSample = 4
SmallSample = 4
LargeSampleRadius = 20

Grid_to_generate = RecievingPlateGenerator(WellsInRow, WellsInColumn, RadiusOfWell)
Sample_rack = SampleRackGenerator(LargeSample, SmallSample, LargeSampleRadius)
Sample_coordinates = Sample_rack.SampleGrid()
CoordinatesOfWells = Grid_to_generate.WellGrid()
x = CoordinatesOfWells[LastWell][2] 
y = CoordinatesOfWells[LastWell][3]


class Application(tk.Frame):  # Application class inherits from Tkinter's Frame class

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)  # calls the constructor for the parent class, Frame
        self.grid()   # so the application actually appears on screen
        self.CreateWidgets()
		
	def CreateWidgets(self):
		self.quitButton = tk.Button(self, text='Exit Symplify',
			command=self.quit) #creates a button labeled Quit
		self.recievingplate = self.CreateRecievingPlate()
		self.solutionplate = self.CreateSolutionPlate()
		self.recievingplate.grid()
		self.solutionplate.grid()
		self.quitButton.grid() #places the button in the application
	
	def CreateRecievingPlate(self):
		self.recievingplate = tk.Canvas(self, width=x, height=y)
		for keys, values in CoordinatesOfWells.items():
			oval = self.recievingplate.create_oval(values[0],values[1],values[2],values[3])
		return self.recievingplate
	
	def CreateSolutionPlate(self):
		self.solutionplate = tk.Canvas(self, width=x, height=4*RadiusOfWell, bg='#1E90FF')
		for keys, values in SampleCoordinates.items():
			oval = self.solutionplate.create_oval(values[0],values[1],values[2],values[3])
		return self.solutionplate
		
	
	
app = Application()
app.master.title('Sample application')
app.mainloop()

#instantiating, giving a title, Starting the main loop.


		
		