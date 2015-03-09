
class method:

    def __init__(self):
        self.textlines = {}

    def GroupGenerator(self,GroupNumber,
                       GroupName,
                       MaxTestsPerPlate=1,OutputFormats=0,OptimizingMode=65):

        #GroupNumber is the number of the group
        # #GroupName is the name of the group
        # #MaxTestsPerPlate = 1 for every group in standardtests.TTL
        # #OutputFormats = 0 as default
        # #OptimizingMode = 65 as default.

        groupline = 'G;' + str(GroupNumber) + ';' + str(GroupName) + ';' \
            + str(MaxTestsPerPlate) + ';' + str(OutputFormats) + ';' \
            + str(OptimizingMode) + ';'

        if 'group' not in self.textlines:
            self.textlines['group'] = groupline

    def TestGenerator(self,TestNumber,
                  TestName,
                  DestinationRack,
                  PredilutionRack='',MaxTime=0,Unknown=0,Utilization=0):

        opener = 'T'
        variablelist = [opener,
                    TestNumber,
                    TestName,
                    MaxTime,
                    Unknown,
                    Utilization,
                    PredilutionRack,
                    DestinationRack]

        variablelist = [str(item) for item in variablelist]
        Testline = ';'.join(variablelist)+';'

        if 'test' not in self.textlines:
            self.textlines['test'] = Testline

    def printmethod(self):
        for key, value in self.textlines.items():
            print value
