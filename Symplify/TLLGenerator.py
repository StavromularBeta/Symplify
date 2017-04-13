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
        print "-------------------------------------------"
        print "-------------------------------------------"
        for item in self.linelist:
            if item[0] == "G":
                print "Group: " + item.split(";")[2] + " (" + item.split(";")[1] + ")"
        print "Test: " + self.linelist[2].split(";")[2] + " (" + self.linelist[2].split(";")[1] + ")"
        print "-------------------------------------------"
        print "-------------------------------------------"
        self.draw_drop_generator()

    def draw_drop_generator(self):
        x = 0
        y = 1
        while y < len(self.droplist):
            print self.droplist[x].split(";")[3] + " -> Plate ( " + self.droplist[x].split(";")[1] + " uL )"
            print "Coordinates = ( " + self.droplist[y].split(";")[5] + ", " + self.droplist[y].split(";")[6] + " )"
            print "-------------------------------------------"
            x += 2
            y += 2
        return self.droplist


