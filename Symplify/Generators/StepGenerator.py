#!/usr/bin/env python
import sys


class StepGenerator:
	"""This class writes the code corresponding to the step type. There are various step 
    types recognized by the symbiot software. At the moment, these step types are 
    hardcoded in when required by the Maker.py classes. 
    
    Method Hierarchy:
    step_generator
    	check_if_valid_step
    	exit_if_invalid_step
    filler_line_generator
    """
    def __init__(self, step_type):
    """
    the step_type is the step type. 256 is the value for any vial transfer-to-plate steps.
    1024 is the value for the footer step, which is required at the end of a script.
    """
        self.step_type = step_type

    def step_generator(self):
    """
    This function generates the step line. It checks if the step is valid - i.e., it is 
    one of the 5 steps possible (note that currently only two steps are used). It exits 
    if the step is invalid. Otherwise, it writes the correct line and returns it.
    """
        step_type = self.check_if_valid_step(self.step_type)
        self.exit_if_invalid_step(step_type)
        step_type = 'W;'+str(self.step_type)+';'
        return step_type

    def check_if_valid_step(self, step_type):
    """
    This function checks to see if int(step_type) is in the list valid_steps, which 
    contains 5 int values. If it is, int(step_type) is returned. If it isn't, the string
    'StepError' is returned.
    """
        valid_steps = [256, 521, 1024, 2048, 4096]
        step_error = 'StepError'
        if int(step_type) not in valid_steps:
            return step_error
        else:
            return int(step_type)

    def exit_if_invalid_step(self, step_type):
    """
    This function checks to see if step_type is 'StepError'. If it is, it prints an error
    message and exits the script. 
    """
        if step_type == 'StepError':
            print 'Invalid Step Type Selected in at least one step.'
            print 'Exiting Script.'
            sys.exit()

    def filler_line_generator(self):
    """
    This function generates the filler line. Not much is known about the filler line,
    or what it does. 
    """
        filler_line = 'S;;1.000;'
        return filler_line
