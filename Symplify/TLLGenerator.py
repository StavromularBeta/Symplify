#!/usr/bin/env python
class TLLGenerator():
    """
    This class generates the TLL file, which Symbiot reads.

    Method Hierarchy:
        tll_generator
        report_generator
    """

    def __init__(self, linelist, TLLfile):
        self.linelist = linelist
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
        print "-------------------------------------------"
        print "-------------------------------------------"
        print "Group: " + self.linelist[1].split(";")[2] + " (" + self.linelist[1].split(";")[1] + ")"
        print "Test: " + self.linelist[2].split(";")[2] + " (" + self.linelist[2].split(";")[1] + ")"
        print "-------------------------------------------"
        print "-------------------------------------------"
        if self.linelist[3].split(";")[1] == "256":
            print "Vial: 100mL" + " -> 96 well plate"
        elif self.linelist[3].split(";")[1] == "1024":
            print "Vial: 250mL" + " -> 96 well plate"
        else:
            print self.linelist[3].split(";")[1] + " -> 96 well plate"
        print "-------------------------------------------"
