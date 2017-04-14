import MakeMethod as mm
from sys import argv
MethodMaker, TLLfile = argv

line_list = mm.header_maker("Peter", 1, "Peter", 1)

#Procedure
line_list = mm.step_maker(line_list, "8;Vial 1-1", 5.00, [1,0], "N")
line_list = mm.step_maker(line_list, "8;Vial 1-1", 10.00, [2,0], "N")
line_list = mm.step_maker(line_list, "8;Vial 1-1", 15.00, [3,0], "Y")
line_list = mm.step_maker(line_list, "8;Vial 1-2", 15.00, [1,0], "N")
line_list = mm.step_maker(line_list, "8;Vial 1-2", 10.00, [2,0], "N")
line_list = mm.step_maker(line_list, "8;Vial 1-2", 5.00, [3,0], "Y")
line_list = mm.step_maker(line_list, "8;Vial 1-1", 5.00, [1,0], "N")
line_list = mm.step_maker(line_list, "8;Vial 1-1", 5.00, [2,0], "N")
line_list = mm.step_maker(line_list, "8;Vial 1-1", 5.00, [3,0], "Y")

mm.file_and_report_generator(line_list,TLLfile)


