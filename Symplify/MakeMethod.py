#!/usr/bin/env python
from GroupGenerator import GroupGenerator
from TestGenerator import TestGenerator
from StepGenerator import StepGenerator
from DrawGenerator import DrawGenerator
from DropGenerator import DropGenerator
from HeaderGenerator import HeaderGenerator
from TLLGenerator import TLLGenerator
from sys import argv
MakeMethod, TLLfile = argv

# intro filler stuff.
Header = HeaderGenerator()
Header_line = Header.header_generator()
Group = GroupGenerator('pH_Experiments', 1)
GroupLine = Group.group_generator()
Test = TestGenerator('pH_Example', 1)
TestLine = Test.test_generator()
Step = StepGenerator(256)
StepTypeLine = Step.step_generator()
FillerLine = Step.filler_line_generator()

#the meat of it all.
Draw = DrawGenerator(1.00, '8;Vial 1-1')
DrawLine = Draw.draw_generator()
Drop = DropGenerator(1.00, '4;', [1, 0], "Y")
DropLine = Drop.drop_generator()
Draw_1 = DrawGenerator(2.00, '8;Vial 1-2')
DrawLine_1 = Draw_1.draw_generator()
Drop_1 = DropGenerator(2.00, '4;', [1, 0], "Y")
DropLine_1 = Drop_1.drop_generator()


linelist = [Header_line,GroupLine,TestLine,StepTypeLine,FillerLine,DrawLine,DropLine,DrawLine_1,DropLine_1]
FileGenerator = TLLGenerator(linelist, TLLfile)
FileGenerator.tll_generator()
FileGenerator.report_generator()
