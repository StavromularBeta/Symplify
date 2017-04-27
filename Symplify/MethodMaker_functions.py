#!/usr/bin/env python
from Generators.GroupGenerator import GroupGenerator
from Generators.TestGenerator import TestGenerator
from Generators.StepGenerator import StepGenerator
from Generators.DrawGenerator import DrawGenerator
from Generators.DropGenerator import DropGenerator
from Generators.HeaderGenerator import HeaderGenerator
from Generators.TLLGenerator import TLLGenerator


class MethodMakerFunctions:

    def __init__(self, TLLfile, linelist=[]):
        self.linelist = linelist
        self.TLLfile = TLLfile

    def header_maker(self, test_name, group_name="DoNotChangeThisString", group_number=13, test_number=1):
        group = GroupGenerator(group_name, group_number)
        group_line = group.group_generator()
        test = TestGenerator(test_name, test_number)
        test_line = test.test_generator()
        step = StepGenerator(256)
        step_type_line = step.step_generator()
        filler_line = step.filler_line_generator()
        self.linelist = [group_line, test_line, step_type_line, filler_line]
        return self.linelist

    def step_maker(self, vial, volume, drop_coordinates, drop_tip="N"):
        draw = DrawGenerator(volume, vial)
        draw_line = draw.draw_generator()
        drop = DropGenerator(volume, '4;', drop_coordinates, drop_tip)
        drop_line = drop.drop_generator()
        self.linelist.append(draw_line)
        self.linelist.append(drop_line)
        return self.linelist

    def footer_maker(self):
        step = StepGenerator(1024)
        step_type_line = step.step_generator()
        filler_line = step.filler_line_generator()
        self.linelist.append(step_type_line)
        self.linelist.append(filler_line)
        draw = DrawGenerator(1.00, "1;SAMPLE")
        draw_line = draw.draw_generator()
        drop = DropGenerator(1.00, '4;', [0, 0], "Y")
        drop_line = drop.drop_generator()
        self.linelist.append(draw_line)
        self.linelist.append(drop_line)
        return self.linelist

    def file_and_report_maker(self):
        self.footer_maker()
        file_generator = TLLGenerator(self.linelist, self.TLLfile)
        file_generator.error_checker()
        file_generator.previous_file_eraser()
        file_generator.tll_generator()
        file_generator.report_generator()