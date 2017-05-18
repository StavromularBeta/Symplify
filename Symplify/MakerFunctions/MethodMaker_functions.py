#!/usr/bin/env python
from Symplify.Generators.GroupGenerator import GroupGenerator
from Symplify.Generators.TestGenerator import TestGenerator
from Symplify.Generators.StepGenerator import StepGenerator
from Symplify.Generators.DrawGenerator import DrawGenerator
from Symplify.Generators.DropGenerator import DropGenerator
from Symplify.Generators.TLLGenerator import TLLGenerator


class MethodMakerFunctions:
    """
    This class contains functions that call Generator methods to make routines that allow a user to quickly make
    tests - MethodMaker.py is an example of a file that uses MethodMakerFunctions to create a sample test. It is an
    extra layer of abstraction over the more raw Generator methods.

    method hierarchy:
        header_maker
            GroupGenerator.group_generator
            TestGenerator.test_generator
            StepGenerator.step_generator
            StepGenerator.filler_line_generator
        step_maker
            DrawGenerator.draw_generator
            DropGenerator.drop_generator
        footer_maker
            StepGenerator.step_generator
            StepGenerator.filler_line_generator
            DrawGenerator.draw_generator
            DropGenerator.drop_generator
        file_and_report_maker
            footer_maker
            TLLGenerator.error_checker
            TLLGenerator.previous_file_eraser
            TLLGenerator.tll_generator
            TLLGenerator.report_generator
    """
    def __init__(self, TLLfile, linelist=[]):
        """
        The TLLfile is the filepath of the text file that the instructions are written to. This can be hardcoded in once
        development is done, because it is only necessary when working on a different computer than the one that the
        workstation is connected to. The linelist is an empty list by default. It is populated as the various methods
        are called.
        """
        self.linelist = linelist
        self.TLLfile = TLLfile

    def header_maker(self, test_name, group_name="DoNotChangeThisString", group_number=13, test_number=1):
        """The header maker file is passed the test name. The group name, number, and test number can optionally
        be changed, but then there may be issues working with the symbiot software - changes would have to be hard-coded
        on that end. It generates the group line with the group_name and group_number, generates the test line
        with the test_name and test_number, and generates the step type line (256 applies to all the steps prior to the
        footer) + filler line. It combines all these lines in an ordered list and returns it, updates the linelist."""
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
        """
        each call of step_maker requires you to provide the vial, which is the vial liquid is being transferred from,
        the volume of liquid being transferred, the drop_coordinates (the x and y value of the well on the plate you
        want to drop the liquid in) and instructions on whether or not to drop the tip (default is no). It generates
        the draw line with volume and vial, generates the drop line with volume, drop_coordinates, and drop_tip. It
        then appends the new steps to the linelist and returns the linelist. step_maker makes one step.
        """
        draw = DrawGenerator(volume, vial)
        draw_line = draw.draw_generator()
        drop = DropGenerator(volume, '4;', drop_coordinates, drop_tip)
        drop_line = drop.drop_generator()
        self.linelist.append(draw_line)
        self.linelist.append(drop_line)
        return self.linelist

    def footer_maker(self):
        """
        footer maker creates the footer lines, which is a transfer from the sample rack (which is empty) to the plate,
        which in essence does nothing - but at least one sample step is required per test, or the symbiot software
        fails. It generates the step line and filler line (step number for sample steps is 1024). It then draws a
        microlitre of nothing and adds it to the fist position on the plate. It updates and returns the linelist.
        """
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
        """
        this method first makes the footer line, then creates a TLLGenerator object. It runs the error_checker routines,
        erases the old test in the TLL file, writes the new test, and generates a report on the test created.
        """
        self.footer_maker()
        file_generator = TLLGenerator(self.linelist, self.TLLfile)
        file_generator.error_checker()
        file_generator.previous_file_eraser()
        file_generator.tll_generator()
        file_generator.report_generator()