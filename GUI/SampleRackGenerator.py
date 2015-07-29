#!/usr/bin/env python
class SampleRackGenerator():
	
	def __init__(self, NumberOfLargeWells, NumberOfThirdWells, RadiusOfLargeWells):
		self.NumberOfLargeWells = NumberOfLargeWells
		self.NumberOfThirdWells = NumberOfThirdWells
		self.RadiusOfLargeWells = RadiusOfLargeWells
		self.RadiusOfThirdWells = RadiusOfLargeWells/2
	
	def SampleGrid(self):
		LargeWellCoordinates = self.PopulateLargeWells()
		SmallAndLargeCoordinates = self.PopulateSmallCoordinates(LargeWellCoordinates)
		return SmallAndLargeCoordinates
		
	def PopulateLargeWells(self):
		LargeWellCoordinates = {}
		Xo = 12
		Yo = 16
		for Well in range(self.NumberOfLargeWells):
			WellCoordinate = self.CreateSingleLargeWell(Xo,Yo)
			Xo = WellCoordinate[4]
			LargeWellCoordinates[Well] = [WellCoordinate[0],
										  WellCoordinate[1],
										  WellCoordinate[2],
										  WellCoordinate[3]]
		return LargeWellCoordinates
	
	def CreateSingleLargeWell(self,Xo,Yo):
		Xone = Xo + 2*self.RadiusOfLargeWells
		Yone = Yo + 2*self.RadiusOfLargeWells
		NextXo = Xone + 0.5*self.RadiusOfLargeWells
		return [Xo,Yo,Xone,Yone,NextXo]
		
	def PopulateSmallCoordinates(self, LargeWellCoordinates):
		SmallAndLargeWellCoordinates = LargeWellCoordinates
		KeyOfLastLargeWell = self.NumberOfLargeWells - 1
		LastWellCoordinates = LargeWellCoordinates[KeyOfLastLargeWell]
		smallXoYo = self.SmallXoYoGenerator(LastWellCoordinates)
		smallXo = smallXoYo[0]
		smallYo = smallXoYo[1]
		for well in range(1,self.NumberOfThirdWells+1):
			smallwellindex = well+(self.NumberOfLargeWells-1)
			WellCoordinate = self.CreateSingleThirdWell(smallXo,smallYo)
			smallXo = WellCoordinate[4]
			SmallAndLargeWellCoordinates[smallwellindex] = [WellCoordinate[0],
															WellCoordinate[1],
															WellCoordinate[2],
															WellCoordinate[3]]
		return SmallAndLargeWellCoordinates
			
		
	def SmallXoYoGenerator(self,LastWellCoordinates):
		smallXo = LastWellCoordinates[0] + 3*self.RadiusOfLargeWells
		smallYo = LastWellCoordinates[1] + self.RadiusOfThirdWells
		return [smallXo,smallYo]
		
	def CreateSingleThirdWell(self,Xo,Yo):
		Xone = Xo + 2*self.RadiusOfThirdWells
		Yone = Yo + 2*self.RadiusOfThirdWells
		NextXo = Xone + 0.5*self.RadiusOfThirdWells
		return [Xo,Yo,Xone,Yone,NextXo]
		
	
		
		