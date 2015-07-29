#!/usr/bin/env python
class GroupGenerator():
	
	def __init__(self,GroupName,GroupNumber):
		self.GroupName = str(GroupName)
		self.GroupNumber = GroupNumber
		self.GeneratedGroupLine = 'string'
		
	def GroupLineGenerator(self):
		KnownVariables = self.GenerateKnownVariables()
		KnownAndUnknownVariables = self.GenerateUnknownVariables(KnownVariables)
		GeneratedGroupLine = self.GenerateGroupLine(KnownAndUnknownVariables)
		self.GeneratedGroupLine = GeneratedGroupLine
		return GeneratedGroupLine
		
	def GenerateKnownVariables(self):
		KnownVariables = 'G;' + str(self.GroupNumber) + ';' + self.GroupName
		return KnownVariables
		
	def GenerateUnknownVariables(self,KnownVariables):
		#These variables have unknown functions and as such have odd names 
		#Taken straight from the menus that generate these values on the Symbiot side
		MaxTestsPerPlate = 1
		OutputFormats = 0
		OptimizingMode = 65
		KnownAndUnknownVariables = [KnownVariables,
									str(MaxTestsPerPlate),
									str(OutputFormats),
									str(OptimizingMode)]
		return KnownAndUnknownVariables
		
	def GenerateGroupLine(self,KnownAndUnknownVariables):
		groupline = ';'.join(KnownAndUnknownVariables)+';'
		return groupline
	
		
		
		