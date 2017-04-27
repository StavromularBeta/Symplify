#!/usr/bin/env python
import sys


class StepGenerator:

    def __init__(self, step_type):
        self.step_type = step_type

    def step_generator(self):
        step_type = self.check_if_valid_step(self.step_type)
        self.exit_if_invalid_step(step_type)
        step_type = 'W;'+str(self.step_type)+';'
        return step_type

    def check_if_valid_step(self, step_type):
        valid_steps = [256, 521, 1024, 2048, 4096]
        step_error = 'StepError'
        if int(step_type) not in valid_steps:
            return step_error
        else:
            return int(step_type)

    def exit_if_invalid_step(self, step_type):
        if step_type == 'StepError':
            print 'Invalid Step Type Selected in at least one step.'
            print 'Exiting Script.'
            sys.exit()

    def filler_line_generator(self):
        filler_line = 'S;;1.000;'
        return filler_line
