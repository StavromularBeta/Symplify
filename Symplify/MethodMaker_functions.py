#!/usr/bin/env python
from GroupGenerator import GroupGenerator
from TestGenerator import TestGenerator
from StepGenerator import StepGenerator
from DrawGenerator import DrawGenerator
from DropGenerator import DropGenerator
from HeaderGenerator import HeaderGenerator
from TLLGenerator import TLLGenerator


def header_maker(group_name, group_number, test_name, test_number):
    header = HeaderGenerator()
    header_line = header.header_generator()
    group = GroupGenerator(group_name, group_number)
    group_line = group.group_generator()
    test = TestGenerator(test_name, test_number)
    test_line = test.test_generator()
    step = StepGenerator(256)
    step_type_line = step.step_generator()
    filler_line = step.filler_line_generator()
    return [header_line, group_line, test_line, step_type_line, filler_line]


def step_maker(header_list, vial, volume, drop_coordinates, drop_tip):
    draw = DrawGenerator(volume, vial)
    draw_line = draw.draw_generator()
    drop = DropGenerator(volume, '4;', drop_coordinates, drop_tip)
    drop_line = drop.drop_generator()
    header_list.append(draw_line)
    header_list.append(drop_line)
    return header_list


def file_and_report_maker(line_list, TLLfile):
    file_generator = TLLGenerator(line_list, TLLfile)
    file_generator.tll_generator()
    file_generator.report_generator()
