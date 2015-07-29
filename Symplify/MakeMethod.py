#!/usr/bin/env python
from GroupGenerator import GroupGenerator
from TestGenerator import TestGenerator
from StepGenerator import StepGenerator
from DrawGenerator import DrawGenerator
from DropGenerator import DropGenerator

Group = GroupGenerator('Peter',1)
GroupLine = Group.GroupLineGenerator()

Test = TestGenerator('Peter',1)
TestLine = Test.TestLineGenerator()

Step = StepGenerator(1024)
StepTypeLine = Step.StepTypeGenerator()
FillerLine = Step.FillerLineGenerator()

Draw = DrawGenerator(1.00,'1;SAMPLE;')
DrawLine = Draw.DrawGenerator()

Drop = DropGenerator(1.00,'4;;')
DropLine = Drop.DropGenerator()

print GroupLine
print TestLine
print StepTypeLine
print FillerLine
print DrawLine
print DropLine

