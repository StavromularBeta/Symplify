
class method:

    possiblesteps = {256: 'Pre-Reagent',
                     521: 'Control',
                     1024: 'Sample',
                     2048: 'EndControl',
                     4096: 'Post Reagent'}

    def __init__(self):
        self.textlines = {}

    def GroupGenerator(self,GroupNumber,
                       GroupName,
                       MaxTestsPerPlate=1,OutputFormats=0,OptimizingMode=65):

        #This function generates the group line.
        # GroupNumber is the number of the group
        # #GroupName is the name of the group
        # #MaxTestsPerPlate = 1 for every group in standardtests.TTL
        # #OutputFormats = 0 as default
        # #OptimizingMode = 65 as default.

        groupline = 'G;' + str(GroupNumber) + ';' + str(GroupName) + ';' \
            + str(MaxTestsPerPlate) + ';' + str(OutputFormats) + ';' \
            + str(OptimizingMode) + ';'

        if 'group' not in self.textlines:
            self.textlines['group'] = groupline

    def TestGenerator(self,
                      TestNumber,
                      TestName,
                      DestinationRack,
                      PredilutionRack='',
                      MaxTime=0,
                      Unknown=0,
                      Utilization=0):

        #This function generates the test line.

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

    def StepGenerator(self,stepvalue):

        #each step is going to become a dict entry with the key being the step and the value being an empty list.
        #each command will be an item in the list.
        #look into turning these into arrays or somehow fixing the order.

        stepline = 'W;'+str(stepvalue)+';'

        if stepline not in self.textlines:
            self.textlines[stepline] = []

    def printmethod(self):
        for key, value in self.textlines.iteritems():
            if isinstance(value, list):
                print key
            else:
                print value
