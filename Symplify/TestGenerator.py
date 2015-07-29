#!/usr/bin/env python
class TestGenerator():

	def __init__(self, TestName, TestNumber):
		self.TestName = TestName
		self.TestNumber = TestNumber
		self.GeneratedTestLine = 'string'
		
	def TestLineGenerator(self):
		KnownVariables = self.GenerateKnownVariables()
		KnownAndUnknownVariables = self.GenerateUnknownVariables(KnownVariables)
		GeneratedTestLine = self.GenerateTestLine(KnownAndUnknownVariables)
		self.GeneratedTestLine = GeneratedTestLine
		return GeneratedTestLine

	def GenerateKnownVariables(self):
		KnownVariables = 'T;' + str(self.TestNumber) + ';' + self.TestName
		return KnownVariables
		
	def GenerateUnknownVariables(self,KnownVariables):
		#These variables have unknown functions and as such have odd names 
		#Taken straight from the menus that generate these values on the Symbiot side
		MaxTime = 0
		UnknownOne = 0
		Utilization = 0
		PredilutionRack_optional = ''
		DestinationRack = 'MALDI 10X10 on row 16'
		KnownandUnknownVariables = [KnownVariables,
									str(MaxTime),
									str(UnknownOne),
									str(Utilization),
									str(PredilutionRack_optional),
									str(DestinationRack)]
		return KnownandUnknownVariables
		
	def GenerateTestLine(self,KnownAndUnknownVariables):
		testline = ';'.join(KnownAndUnknownVariables)+';'
		return testline
	