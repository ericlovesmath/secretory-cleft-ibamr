#/Applications/VisIt.app/Contents/Resources/3.1.2/../bin/visit -cli -s ~/Desktop/UCI/Python/VisitOutput.py
simName = raw_input("Simulation Name (Inside ./Simulations): ")
OpenDatabase("~/Desktop/UCI/Simulations/"+simName+"/viz_IB2d/lag_data.visit")
AddPlot("Subset", "fila_256_mesh")
for i in range(TimeSliderGetNStates()):
    SetTimeSliderState(i)
    DrawPlots()
    dbAtts = ExportDBAttributes()
    dbAtts.dirname = "./VisExport"
    dbAtts.db_type = "VTK"
    dbAtts.filename = "file%04d" % i
    dbAtts.variables = ("default")
    ExportDatabase(dbAtts)

# vtk to txt

for fileID in range(TimeSliderGetNStates()):
    fileLocation = "./VisExport/file" + format(fileID, "04") + ".vtk"
    with open(fileLocation, "r") as f:
        vtkText = f.readlines()
    for lineID in range(len(vtkText)):
        if vtkText[lineID][:7] == "POINTS ":
            startLine = lineID
        if vtkText[lineID][:6] == "CELLS ":
            endLine = lineID
    coordRow = "".join(vtkText[startLine+1:endLine]).split()
    coords = [[coordRow[3*i],coordRow[3*i+1]] for i in range(len(coordRow)//3)]
    print(coords)
    
    # Output
    outputFile = open("./VisExport/Analysis/" + format(fileID, "04") + ".txt", "w")
    outputFile.write("# x, y\n")
    for coord in coords:
        outputFile.write(" ".join(coord)+"\n")

outputFile.close()

# Images
s = SaveWindowAttributes()
s.format = s.PNG
s.fileName = "slice"
s.width, s.height = 1024,768
s.screenCapture = 0
s.outputDirectory = "./VisExport/Images"
s.outputToCurrentDirectory = 0
SetSaveWindowAttributes(s)

names = []
for state in range(TimeSliderGetNStates()):
  SetTimeSliderState(state)
  SaveWindow()

# gif
import os
print("VisIt: Message - Rendering gif...")
os.system("convert -delay 30 -loop 0 ./VisExport/Images/*.png ./VisExport/Images/sim.gif")
print("VisIt: Message - Saving gif...")
print("VisIt: Message - Saved ./VisExport/Images/sim.gif")

exit()