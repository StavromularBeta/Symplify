#This is the first script for Symplify.
#the goal of this script is to explore the idea of generating text files that can be read
#as tests by symbiot.
#the GUI refers to the program TestEdit
#text refers to opening the file up with a text editor.

#sample text
#G;1;Sample and Matrix;1;0;65;
#Group;GroupNumber;GroupTitle;MaxTestsPerPlate;OutputFormats;OptimizingMode;
#G specifies that this line is a group
#The groupNumber is the group number, 1 being the first group in the file
#the GroupTitle is the name of the group

#these variables are accessed by double clicking on "group" in the GUI, and refer to 
#various options/boxes/text inputs in said menus.
#max tests per plate = 1
#Output Formats - none are checked at 0
#numbers don't correspond to anything in particular, for example 11 is the first three
#checked and 15 is the first four checked. There are 8 options.
#the last number in the sequence refers to the optimizing mode. Don't really know what 
#any of these actually are.

#The W values
#W values refer to the type of Step being added.
#Pre Reagent = 256, Control(Before Samples) = Unknown(possibly 521), Sample = 1024,
#EndControl(After Samples) = Unknown(possibly 2048), Post Reagent = 4096

#NEXTLINE

#sample text
#T;101;Sample(SP)/Matrix(SP);0;0;0;;MALDI 10x10 on row 16;
#Test;TestNumber;TestName;MaxTime;Unknown;Utilization;PredilutionRack(optional);DestinationRack;

#so far we have 
#G;1;Sample and Matrix;1;0;65; (all known)
#T;101;Sample(SP)/Matrix(SP);0;0;0;;MALDI 10x10 on row 16; (only second 0 unknown)
#W;1024;
#S;;1.000; - dunno yet. Always after every W command, always this line.

#next comes C;1.00;1;SAMPLE;262210;0;0;0;2;0;0;
		   #Command;Volume;Unknown;Location;Unknown;Unknown;Unknown;Unknown;LiquidClass(Dropdown);Unknown;Unknown;
		   #C;1.00;4;;262170;0;0;0;2;1;0;
		   
#This line refers to the Draw step.		   
#for the unknown 6 digit number, the last two digits are 10 if single pipetting, 9 for multi		   
#C is command, or something similar. 

#This line refers to the Drop & DITI step
#C;1.00;4;;262170;0;0;0;1;1;0;
#Command;Volume;LocationModifier;Location;Unknown;Unknown;Unknown;Unknown;LiquidClass(Dropdown);Unknown;Unknown

#The second two values are pairs corresponding to different selections of Location.
#1;sample; = sample
#4;; = Dest. Rack
#8;ReagentName; = Reagent (Reagent name is selected from a dropdown list).
#16;; = Waste.

def GroupGenerator(GroupNumber,
				   GroupName,
				   MaxTestsPerPlate=1,OutputFormats=0,OptimizingMode=65):
				   
	#GroupNumber is the number of the group
	#GroupName is the name of the group
	#MaxTestsPerPlate = 1 for every group in standardtests.TTL
	#OutputFormats = 0 as default
	#OptimizingMode = 65 as default.
	
	groupline = 'G;' + str(GroupNumber) + ';' + str(GroupName) + ';' \
			  + str(MaxTestsPerPlate) + ';' + str(OutputFormats) + ';' \
			  + str(OptimizingMode) + ';'
			  
	return groupline
	
Firstgroup = GroupGenerator(1,'PeterGroup')
print Firstgroup

def TestGenerator(TestNumber,
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
	return Testline
	
FirstTest = TestGenerator(101,'PeterTest','MALDI 10x10 on row 16')
print FirstTest


def stepselector(steptype):

    return 'W;'+str(steptype)+';'








