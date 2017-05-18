import MakerFunctions.MethodMaker_functions as mm
FilePath = "/Users/PeterLevett/Documents/My Actual Documents/Work Study/Symplify/Symplify/TTLfiles/TLLfile"
method = mm.MethodMakerFunctions(FilePath)
method.header_maker("pH_study")

#Procedure
# vial options: '8;Vial 1-1', '8;Vial 1-2', '8;Vial 1-3'
# units of volume in microlitres. format X.XX
# drop coordinates - [X,Y].
# drop_tip = "Y" or "N".

volume = 1.00
x_coord = 0

while x_coord < 6:
    method.step_maker("8;Vial 1-1", volume, [x_coord, 0])
    volume += float(1.00)
    x_coord += 1
else:
    method.step_maker("8;Vial 1-1", volume, [x_coord, 0], "Y")

vial_2_volume = 10.00
x_coord = 0

while x_coord < 6:
    method.step_maker("8;Vial 1-2", vial_2_volume, [x_coord, 0])
    volume -= float(1.00)
    x_coord += 1
    vial_2_volume -= 1
else:
    method.step_maker("8;Vial 1-2", vial_2_volume, [x_coord, 0], "Y")

method.file_and_report_maker()


