from method import method

print '##############################'
print 'Method Generator'
print '##############################'

newmethod = method()

groupname = raw_input('group name?')
groupnumber = raw_input('group number?')
testname = raw_input('test name?')
testnumber = raw_input('test number?')
destinationrack = raw_input('destination rack?'
                            'a) MALDI 10x10 on row 16')

if destinationrack not in ['a']:
    print 'INVALID'
else:
    if destinationrack == 'a':
        destinationrack = 'MALDI 10x10 on row 16'

newmethod.GroupGenerator(groupname,groupnumber)
newmethod.TestGenerator(testnumber,testname,destinationrack)
newmethod.printmethod()