#!/usr/bin/env python
class RecievingPlateGenerator():

	def __init__(self, WellsPerRow, WellsPerColumn, RadiusOfWells):
		self.WellsPerRow = WellsPerRow
		self.WellsPerColumn = WellsPerColumn
		self.RadiusOfWells = RadiusOfWells
		
	def WellGrid(self):
		FirstRowCoordinates = self.PopulateFirstRow()
		FullCoordinates = self.PopulateRemainingCoordinates(FirstRowCoordinates)
		return FullCoordinates
		
	def PopulateFirstRow(self):
		FirstRowCoordinates = {}
		StartingXo = 4
		StartingYo = 4
		for Well in range(1,self.WellsPerRow+1):
			FirstRowWellCoordinateXoYo = self.FirstRowCoordinates(StartingXo, StartingYo)
			FirstRowCoordinates[Well] = FirstRowWellCoordinateXoYo[0]		
			StartingXo = FirstRowWellCoordinateXoYo[1]
			StartingYo = FirstRowWellCoordinateXoYo[2]
		return FirstRowCoordinates
			
	def FirstRowCoordinates(self,XoOfWell,YoOfWell):
		XoOfNextWell = XoOfWell + 2*self.RadiusOfWells
		YoOfNextWell = YoOfWell
		Xone = XoOfNextWell
		Yone = YoOfNextWell + 2*self.RadiusOfWells		
		FirstRowWellCoordinate = [XoOfWell, YoOfWell, Xone, Yone]
		CoordinatesAndNextXoYo = [FirstRowWellCoordinate, XoOfNextWell, YoOfNextWell]
		return CoordinatesAndNextXoYo
	
	def PopulateRemainingCoordinates(self,FirstRowCoordinates):
	
		RemainingCoordinates = FirstRowCoordinates
		for FirstRowWell, FirstRowCoordinates in FirstRowCoordinates.items():
			ColumnRangeInfo = self.ColumnRangeMaker(FirstRowWell)
			for Well in range(ColumnRangeInfo[0],ColumnRangeInfo[1],ColumnRangeInfo[2]):
			    rowofitem = (Well - FirstRowWell)/8 
			    Xo = FirstRowCoordinates[0]
			    Yo = FirstRowCoordinates[1]+(rowofitem*self.RadiusOfWells*2)
			    Xone = FirstRowCoordinates[2]
			    Yone = FirstRowCoordinates[3]+(rowofitem*self.RadiusOfWells*2)
			    RemainingCoordinates[Well] = [Xo,Yo,Xone,Yone]
			self.EnterLastCoordinate(Well,ColumnRangeInfo[1],RemainingCoordinates)
		return RemainingCoordinates
		
	def ColumnRangeMaker(self, FirstRowWell):
		step = self.WellsPerRow
		start = FirstRowWell+self.WellsPerRow
		end = (self.WellsPerRow*self.WellsPerColumn) - self.WellsPerRow + FirstRowWell + 1
		return [start, end, step]
		
	def EnterLastCoordinate(self,Penultimate,endrange,FinishedRowCoordinates):
		FinalCoordinates = FinishedRowCoordinates
		if Penultimate == endrange:
			FinalXo = FinalCoordinates[Penultimate][0] + 2*self.RadiusOfWells
			FinalYo = FinalCoordinates[Penultimate][1] 
			FinalXone = FinalCoordinates[Penultimate][2] + 2*self.RadiusOfWells
			FinalYone = FinalCoordinates[Penultimate][3]
			Ultimate = [FinalXo,FinalYo,FinalXone,FinalYone]
			FinalCoordinates[Penultimate+1] = Ultimate
	
	def PrintCoordinates(self,CoordinatesToPrint):
		for keys, values in CoordinatesToPrint.items():
			print keys, values
	

		