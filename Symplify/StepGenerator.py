#!/usr/bin/env python
import sys

class StepGenerator():

	def __init__(self, StepType):
		self.StepType = StepType
		
	def StepTypeGenerator(self):
		StepType = self.StepValidityChecker(self.StepType)
		self.ExitIfInvalidStepType(StepType)
		StepType = 'W;'+str(self.StepType)+';'
		return StepType
		
	def StepValidityChecker(self,StepType):
		ValidSteps = [256,521,1024,2048,4096]
		ErrorFlag = 'StepError'
		if int(StepType) not in ValidSteps:
			return ErrorFlag
		else: 
			return int(StepType)
		
	def ExitIfInvalidStepType(self,StepType):
		if StepType == 'StepError':
			print 'Invalid Step Type Selected in at least one step.'
			print 'Exiting Script.'
			sys.exit()
		
	def FillerLineGenerator(self):
		FillerLine = 'S;;1.000;'
		return FillerLine
		

		
		