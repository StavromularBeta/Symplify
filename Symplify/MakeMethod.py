#!/usr/bin/env python
from GroupGenerator import GroupGenerator
from TestGenerator import TestGenerator
from StepGenerator import StepGenerator
from DrawGenerator import DrawGenerator
from DropGenerator import DropGenerator
from HeaderGenerator import HeaderGenerator
from sys import argv

MakeMethod, TLLfile = argv
target = open(TLLfile, 'w')
target.truncate()

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

linelist = [Header_line,GroupLine,TestLine,StepTypeLine,FillerLine,DrawLine,DropLine]

for item in linelist:
    target.write(item)
    target.write('\n')

target.close()