#!/usr/bin/env python


class HeaderGenerator:
    """
    This class generates the header. In the current set up, this class is unnecessary, because there will already be
    a header in the TTL file. This class was necessary at some point and may be again, so it was left in the project.

    Method Hierarchy:

    header_generator
        generate_known_header
        generate_unknown_header
        finished_header

    """
    def __init__(self):
        self.header_text = 'string'

    def header_generator(self):
        """
        this function first generates the known header, which currently is no part of the header. It then generates
        the unknown portion of the header. Finished_header combines the two, and returns the completed header lines.
        """
        known_header = self.generate_known_header()
        unknown_header = self.generate_unknown_header()
        finished_header = self.finished_header(known_header, unknown_header)
        return finished_header

    def generate_known_header(self):
        """
        This is a dummy function for now, if, in the future, part of the header is understood and there is a desire
        for modification, that code would go here.
        """
        known_header = ""
        return known_header

    def generate_unknown_header(self):
        """
        This function generates the unknown lines of the header (copied directly from the pre existing TTL file) and
        returns them.
        """
        unknown_lines = ["V;104;",
                         "L;1;Aqueous;0;5;0;70;0;10;200;0;70;0;20;3;-5;0;0;0;1;0;1;60;0;1;4;0;0;4;50;0;0;1;1;10;0;10;0;70;0;0;0;0;60;0;0;4;0;50;1;0;0;10;100;0;1;",
                         "L;1;Aqueous;1;5;0;70;0;10;200;0;70;0;20;4;-5;20;0;1;1;4;1;80;3;2;4;0;0;4;50;0;0;1;1;10;0;10;0;70;0;0;0;0;80;0;0;4;0;50;1;0;0;10;100;1;1;",
                         "L;1;Aqueous;2;0;0;70;0;20;250;0;70;250;20;3;0;0;0;0;1;0;1;60;0;0;4;0;0;4;50;0;0;1;1;600;250;150;0;70;0;0;0;0;60;0;0;4;0;50;1;0;0;10;100;0;0;",
                         "L;1;Aqueous;3;0;0;70;0;50;50;0;70;0;20;3;0;1;0;0;1;0;1;80;0;0;4;0;0;4;50;0;0;1;1;600;100;400;0;70;0;0;0;0;80;0;0;4;0;50;1;0;0;10;100;0;0;",
                         "L;2;50% Acetonitrile;0;5;0;70;0;10;200;0;70;0;20;-1;-5;0;0;0;1;0;1;60;-1;1;4;0;0;4;50;0;0;1;1;10;0;10;0;70;0;0;0;0;60;0;0;4;0;50;1;0;0;10;100;0;1;",
                         "L;2;50% Acetonitrile;1;5;0;70;0;10;200;0;70;0;20;4;-5;20;0;1;1;4;1;80;3;2;4;0;0;4;50;0;0;1;1;10;0;10;0;70;0;0;0;0;80;0;0;4;0;50;1;0;0;10;100;1;1;",
                         "L;2;50% Acetonitrile;2;0;0;70;0;20;100;0;70;0;20;3;-5;0;0;0;1;0;1;60;0;0;4;0;0;4;50;0;0;1;1;600;250;150;0;70;0;0;0;0;60;0;0;4;0;50;1;0;0;10;100;0;0;",
                         "L;2;50% Acetonitrile;3;0;0;70;0;50;50;0;70;0;20;3;-5;1;0;0;1;0;1;80;0;2;4;0;0;4;50;0;0;1;1;600;100;400;0;70;0;0;0;0;80;0;0;4;0;50;1;0;0;10;100;0;0;",
                         "L;3;Airgap;0;5;0;70;0;10;200;0;70;0;20;3;-5;0;0;0;1;0;1;60;0;1;4;0;0;4;50;0;0;1;1;10;0;10;0;70;0;0;0;0;60;0;0;4;0;50;1;0;0;10;100;0;1;",
                         "L;3;Airgap;1;5;0;70;0;10;200;0;70;0;20;4;-5;20;0;1;1;4;1;80;3;2;4;0;0;4;50;0;0;1;1;10;0;10;0;70;0;0;0;0;80;0;0;4;0;50;1;0;0;10;100;1;1;",
                         "L;3;Airgap;2;0;0;70;0;20;250;1;70;250;20;0;0;0;0;0;1;0;1;60;0;0;4;0;0;4;50;0;0;1;1;600;250;150;0;70;0;0;0;0;60;0;0;4;0;50;1;0;0;10;100;0;0;",
                         "L;3;Airgap;3;0;0;70;0;50;50;0;70;0;20;3;0;1;0;0;1;0;1;80;0;0;4;0;0;4;50;0;0;1;1;600;100;400;0;70;0;0;0;0;80;0;0;4;0;50;1;0;0;10;100;0;0;",
                         "D;10uL DITI;1;0.0;0;0.0;0;0;1;20;1;70;0;"
                         ]
        return unknown_lines

    def finished_header(self, known_header, unknown_header):
        """
        this function joins the known and unknown parts of the header together, then returns them.
        """
        if not known_header:
            string_output = ""
            for item in unknown_header:
                string_output = string_output + "\n" + item
            return string_output



