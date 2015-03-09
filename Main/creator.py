import sys
from method import method

print '##############################'
print 'Method Generator'
print '##############################'

newmethod = method()

print 'Group Select'
print '##############################'

groupname = raw_input('group name?')
groupnumber = raw_input('group number?')

print '##############################'
print 'Test Select'
print '##############################'

testname = raw_input('test name?')
testnumber = raw_input('test number?')

print '##############################'
print 'Destination Select'
print '##############################'

destinationrack = raw_input("""destination rack?'
    a) MALDI 10x10 on row 16

choose one of the presented options.""")

if destinationrack not in ['a']:
    print 'INVALID option - script exiting.'
    sys.exit()
else:
    if destinationrack == 'a':
        destinationrack = 'MALDI 10x10 on row 16'

newmethod.GroupGenerator(groupname,groupnumber)
newmethod.TestGenerator(testnumber,testname,destinationrack)

print '##############################'
print 'Step Select'
print '##############################'

for key, value in newmethod.possiblesteps.items():
    print str(key) + ') ' + str(value)

stepchosen = raw_input('choose a step to continue.')
newmethod.StepGenerator(stepchosen)
newmethod.printmethod()


