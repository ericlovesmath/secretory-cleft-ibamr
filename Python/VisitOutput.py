#/Applications/VisIt.app/Contents/Resources/3.1.2/../bin/visit -cli -s ~/Desktop/UCI/Python/VisitOutput.py
OpenDatabase("~/Desktop/UCI/Simulations/TrapezoidGoWhee/viz_IB2d/lag_data.visit")
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
    outputFile.write("x, y\n")
    for coord in coords:
        outputFile.write(" ".join(coord)+"\n")

outputFile.close()

exit()