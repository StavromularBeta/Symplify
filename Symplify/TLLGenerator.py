#!/usr/bin/env python
class TLLGenerator():
    """
    This class generates the TLL file, which Symbiot reads.

    Method Hierarchy:
        tll_generator
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