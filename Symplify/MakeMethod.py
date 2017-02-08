#!/usr/bin/env python
from GroupGenerator import GroupGenerator
from TestGenerator import TestGenerator
from StepGenerator import StepGenerator
from DrawGenerator import DrawGenerator
from DropGenerator import DropGenerator
from HeaderGenerator import HeaderGenerator

Header = HeaderGenerator()
Header_line = Header.header_generator()

Group = GroupGenerator('Peter', 1)
GroupLine = Group.group_generator()

Test = TestGenerator('Peter', 1)
TestLine = Test.test_generator()

Step = StepGenerator(1024)
StepTypeLine = Step.step_generator()
FillerLine = Step.filler_line_generator()

Draw = DrawGenerator(1.00, '1;SAMPLE;')
DrawLine = Draw.draw_generator()

Drop = DropGenerator(1.00, '4;;')
DropLine = Drop.drop_generator()

print Header_line
print GroupLine
print TestLine
print StepTypeLine
print FillerLine
print DrawLine
print DropLine

