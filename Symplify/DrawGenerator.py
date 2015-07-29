#!/usr/bin/env python
class DrawGenerator():

	def __init__(self, DrawVolume, DrawLocation):
		self.DrawVolume = DrawVolume
		self.DrawLocation = DrawLocation
		self.GeneratedDrawLine = 'string'

	def DrawGenerator(self):
		KnownVariables = self.GenerateKnownVariables()
		KnownAndUnknownVariables = self.GenerateUnknownVariables(KnownVariables)
		GeneratedDrawLine = self.GenerateDrawLine(KnownAndUnknownVariables)
		self.GeneratedDrawLine = GeneratedDrawLine
		return GeneratedDrawLine
	
	def GenerateKnownVariables(self):
		KnownVariables = "C;"+str(self.DrawVolume)+";"+str(self.DrawLocation)
		return KnownVariables
		
	def GenerateUnknownVariables(self, KnownVariables):
		unknown1 = 262210
		unknown2 = 0
		unknown3 = 0
		unknown4 = 0
		unknown5 = 2
		unknown6 = 0
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
		
	def GenerateDrawLine(self,KnownAndUnknownVariables):
		DrawLine = ';'.join(KnownAndUnknownVariables)+';'
		return DrawLine
		

									