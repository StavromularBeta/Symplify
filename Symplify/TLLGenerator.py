#!/usr/bin/env python
import sys


class TLLGenerator():
    """
    This class generates the TTL file, which Symbiot reads. The Method Hierarchy for this file illustrates the order
    in which the various functions are called to execute all the steps required to generate a TTL file - this is done
    by MethodMaker_functions.py.

    Method Hierarchy:
        error_checker
            determine_error_type
        previous_file_eraser
        tll_generator
        report_generator
            report_header_generator
            report_draw_drop_generator
    """

    def __init__(self, linelist, TLLfile):
        """This class is passed the linelist, a list of lines created by the user, and the path of the TTL file being
        used. """
        self.linelist = linelist
        self.droplist = linelist[4:]
        self.TLLfile = TLLfile

    def tll_generator(self):
        """
        This function first opens the file passed to it. It then writes each line, at the end of the file,
        followed by a linebreak. It then closes the file.
        """
        target = open(self.TLLfile, 'a')
        for item in self.linelist:
            target.write(item)
            target.write('\n')
        target.close()

    def previous_file_eraser(self):
        """
        This function first opens the TTL file in a read-only format. It reads the lines, and saves them as a variable
        called lines - this is a list of all the lines in the file in order. The file is then closed. One of these lines
        is the group line for the test we wrote. We go through the TTL file lines, and when we reach the group line we
        are looking for, we delete everything in the TTL file below and including this group line. This deletes the
        previously written test, if it existed. The TTL file is then opened again in a write format, and it is rewritten
        without the previously written test. This all serves to delete the previous test.
        """
        target = open(self.TLLfile, 'r')
        lines = target.readlines()
        target.close()
        for item in lines:
            if item[0:-1] == "G;13;Peter;1;0;65;":
                target_line = lines.index(item)
                del lines[target_line:]
        target = open(self.TLLfile, 'w')
        target.truncate()
        target.writelines(lines)
        target.close()

    def report_generator(self):
        """
        This function generates a report on the test produced by the TLL file generated. This report is a more readable
        form of the TTL file that shows the user what they have created. First, the header is created, and then the
        steps are created.
        """
        self.report_header_generator()
        self.report_draw_drop_generator()

    def report_header_generator(self):
        """
        This function generates the report header. This contains information on the group, and the test.
        """
        print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        for item in self.linelist:
            if item[0] == "G":
                print "Group: " + item.split(";")[2] + " (" + item.split(";")[1] + ")"
            elif item[0] == "T":
                print "Test: " + item.split(";")[2] + " (" + item.split(";")[1] + ")"
        print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    def report_draw_drop_generator(self):
        """
        This function prints out the draw/drop steps.

        The droplist is the list containing all the draw/drop information for the test. It is the linelist without the
        first four lines. 'len(self.droplist) - 3' is the index of the first of the last two footer lines in the test.
        When y == this value, we are finished our draw/drop steps, so the function ends just before that point.
        Increasing the value of x and y by 2 each iteration brings us to our next draw/drop pair.
        """
        x = 0
        y = 1
        while y < len(self.droplist) - 3:
            print self.droplist[x].split(";")[3] + " -> ( " + self.droplist[x].split(";")[1] + " uL )" + \
                " x,y = ( " + self.droplist[y].split(";")[5] + ", " + self.droplist[y].split(";")[6] + " )"
            print "----------------------------------------"
            x += 2
            y += 2
        return self.droplist

    def error_checker(self):
        """
        This function primarily checks for errors in line ordering in the TTL file. It strips the first characters
        off of the first five lines and the last two lines. If the lines aren't in the correct order, it runs
        determine_error_type to figure out what the problem is.
        """
        error_checker_characters = self.linelist[0][0] + self.linelist[1][0] + \
                                   self.linelist[2][0] + self.linelist[3][0] + self.linelist[4][0] + \
                                   self.linelist[-4][0] + self.linelist[-3][0]

        if error_checker_characters != "GTWSCWS":
            print "Error"
            self.determine_error_type(error_checker_characters)
        else:
            return "No Errors detected"

    def determine_error_type(self, error_checker_characters):
        """
        determine_error_type checks for three types of errors. If the first of the lines is a draw/drop line,
        there is no header. If there are no steps, the fifth line would also be the second last line, so the string
        would look like "GTWSW". Finally, if there was no footer, the last two characters wouldn't be 'WS'.
        If none of these errors are what cause the lines to be out of order, there is an unidentified error, and the
        system will still exit.
        """
        if error_checker_characters[0] == "C":
            print "Lacking appropriate header. must use header_maker prior to writing any steps. Exiting."
            sys.exit()
        elif error_checker_characters[0:5] == "GTWSW":
            print "No steps detected, only header and footer detected. Exiting."
            sys.exit()
        elif error_checker_characters[-2:-1] != "WS":
            print "Lacking appropriate footer. Must use footer_maker at the end of writing any steps. Exiting."
            sys.exit()
        else:
            print "Error unknown but fatal. Exiting."
            sys.exit()


