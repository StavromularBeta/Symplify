#!/usr/bin/env python
import sys


class TLLGenerator():
    """
    This class generates the TLL file, which Symbiot reads.

    Method Hierarchy:
        tll_generator
        report_generator
    """

    def __init__(self, linelist, TLLfile):
        self.linelist = linelist
        self.droplist = linelist[5:]
        self.TLLfile = TLLfile

    def tll_generator(self):
        """
        This function first opens the file passed to it and erases any text in the file. It then writes each line,
        followed by a linebreak. It then closes the file.
        """
        target = open(self.TLLfile, 'w')
        target.truncate()
        for item in self.linelist:
            target.write(item)
            target.write('\n')
        target.close()

    def report_generator(self):
        """
        This function generates a report on the test produced by the TLL file generated. It is easier to read than the
        TLL file. It currently only is capable of generating the report up to the step type.
        """
        self.report_header_generator()
        self.report_draw_drop_generator()

    def report_header_generator(self):
        print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        for item in self.linelist:
            if item[0] == "G":
                print "Group: " + item.split(";")[2] + " (" + item.split(";")[1] + ")"
            elif item[0] == "T":
                print "Test: " + item.split(";")[2] + " (" + item.split(";")[1] + ")"
        print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    def report_draw_drop_generator(self):
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
        error_checker_characters = self.linelist[1][0] + self.linelist[2][0] + \
                                   self.linelist[3][0] + self.linelist[4][0] + self.linelist[5][0] + \
                                   self.linelist[-4][0] + self.linelist[-3][0]

        if error_checker_characters != "GTWSCWS":
            print "Error"
            self.determine_error_type(error_checker_characters)
        else:
            return "No Errors detected"

    def determine_error_type(self, error_checker_characters):
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


