#!/usr/bin/env python
class DropGenerator():

	def __init__(self, DropVolume, DropLocation):
		self.DropVolume = DropVolume
		self.DropLocation = DropLocation
		self.GeneratedDropLine = 'string'

	def DropGenerator(self):
		KnownVariables = self.GenerateKnownVariables()
		KnownAndUnknownVariables = self.GenerateUnknownVariables(KnownVariables)
		GeneratedDropLine = self.GenerateDropLine(KnownAndUnknownVariables)
		self.GeneratedDropLine = GeneratedDropLine
		return GeneratedDropLine
	
	def GenerateKnownVariables(self):
		KnownVariables = "C;"+str(self.DropVolume)+";"+str(self.DropLocation)
		return KnownVariables
		
	def GenerateUnknownVariables(self, KnownVariables):
		unknown1 = 262170
		unknown2 = 0
		unknown3 = 0
		unknown4 = 0
		unknown5 = 1
		unknown6 = 1
		unknown7 = 0
		KnownAndUnknownVariables = [KnownVariables,
									str(unknown1),
									str(unknown2),
									str(unknown3),
									str(unknown4),
									str(unknown5),
									str(unknown6),
									str(unknown7),]
		return KnownAndUnknownVariables
		
	def GenerateDropLine(self,KnownAndUnknownVariables):
		DropLine = ';'.join(KnownAndUnknownVariables)+';'
		return DropLine
		