# Visit 3.1.2 log file
ScriptVersion = "3.1.2"
if ScriptVersion != Version():
    print "This script is for VisIt %s. It may not work with version %s" % (ScriptVersion, Version())
ShowAllWindows()
OpenDatabase("~/Desktop/UCI/Simulations/TrapezoidGoWhee/viz_IB2d/lag_data.visit", 0)
# The UpdateDBPluginInfo RPC is not supported in the VisIt module so it will not be logged.
AddPlot("Subset", "fila_256_mesh", 1, 1)
SetTimeSliderState(0)
DrawPlots()
ExportDBAtts = ExportDBAttributes()
ExportDBAtts.allTimes = 0
ExportDBAtts.dirname = "./VisExport"
ExportDBAtts.filename = "file0000"
ExportDBAtts.timeStateFormat = "_%04d"
ExportDBAtts.db_type = "VTK"
ExportDBAtts.db_type_fullname = "VTK_1.0"
ExportDBAtts.variables = ("default")
ExportDBAtts.writeUsingGroups = 0
ExportDBAtts.groupSize = 48
DBExportOpts = {'Tetrahedralize': 0, 'FileFormat': 'Legacy Ascii'}
ExportDatabase(ExportDBAtts, DBExportOpts)
SetTimeSliderState(1)
DrawPlots()
ExportDBAtts = ExportDBAttributes()
ExportDBAtts.allTimes = 0
ExportDBAtts.dirname = "./VisExport"
ExportDBAtts.filename = "file0001"
ExportDBAtts.timeStateFormat = "_%04d"
ExportDBAtts.db_type = "VTK"
ExportDBAtts.db_type_fullname = "VTK_1.0"
ExportDBAtts.variables = ("default")
ExportDBAtts.writeUsingGroups = 0
ExportDBAtts.groupSize = 48
DBExportOpts = {'Tetrahedralize': 0, 'FileFormat': 'Legacy Ascii'}
ExportDatabase(ExportDBAtts, DBExportOpts)
SetTimeSliderState(2)
DrawPlots()
ExportDBAtts = ExportDBAttributes()
ExportDBAtts.allTimes = 0
ExportDBAtts.dirname = "./VisExport"
ExportDBAtts.filename = "file0002"
ExportDBAtts.timeStateFormat = "_%04d"
ExportDBAtts.db_type = "VTK"
ExportDBAtts.db_type_fullname = "VTK_1.0"
ExportDBAtts.variables = ("default")
ExportDBAtts.writeUsingGroups = 0
ExportDBAtts.groupSize = 48
DBExportOpts = {'Tetrahedralize': 0, 'FileFormat': 'Legacy Ascii'}
ExportDatabase(ExportDBAtts, DBExportOpts)
SetTimeSliderState(3)
DrawPlots()
ExportDBAtts = ExportDBAttributes()
ExportDBAtts.allTimes = 0
ExportDBAtts.dirname = "./VisExport"
ExportDBAtts.filename = "file0003"
ExportDBAtts.timeStateFormat = "_%04d"
ExportDBAtts.db_type = "VTK"
ExportDBAtts.db_type_fullname = "VTK_1.0"
ExportDBAtts.variables = ("default")
ExportDBAtts.writeUsingGroups = 0
ExportDBAtts.groupSize = 48
DBExportOpts = {'Tetrahedralize': 0, 'FileFormat': 'Legacy Ascii'}
ExportDatabase(ExportDBAtts, DBExportOpts)
SetTimeSliderState(4)
DrawPlots()
ExportDBAtts = ExportDBAttributes()
ExportDBAtts.allTimes = 0
ExportDBAtts.dirname = "./VisExport"
ExportDBAtts.filename = "file0004"
ExportDBAtts.timeStateFormat = "_%04d"
ExportDBAtts.db_type = "VTK"
ExportDBAtts.db_type_fullname = "VTK_1.0"
ExportDBAtts.variables = ("default")
ExportDBAtts.writeUsingGroups = 0
ExportDBAtts.groupSize = 48
DBExportOpts = {'Tetrahedralize': 0, 'FileFormat': 'Legacy Ascii'}
ExportDatabase(ExportDBAtts, DBExportOpts)
SetTimeSliderState(5)
DrawPlots()
ExportDBAtts = ExportDBAttributes()
ExportDBAtts.allTimes = 0
ExportDBAtts.dirname = "./VisExport"
ExportDBAtts.filename = "file0005"
ExportDBAtts.timeStateFormat = "_%04d"
ExportDBAtts.db_type = "VTK"
ExportDBAtts.db_type_fullname = "VTK_1.0"
ExportDBAtts.variables = ("default")
ExportDBAtts.writeUsingGroups = 0
ExportDBAtts.groupSize = 48
DBExportOpts = {'Tetrahedralize': 0, 'FileFormat': 'Legacy Ascii'}
ExportDatabase(ExportDBAtts, DBExportOpts)
SetTimeSliderState(6)
DrawPlots()
ExportDBAtts = ExportDBAttributes()
ExportDBAtts.allTimes = 0
ExportDBAtts.dirname = "./VisExport"
ExportDBAtts.filename = "file0006"
ExportDBAtts.timeStateFormat = "_%04d"
ExportDBAtts.db_type = "VTK"
ExportDBAtts.db_type_fullname = "VTK_1.0"
ExportDBAtts.variables = ("default")
ExportDBAtts.writeUsingGroups = 0
ExportDBAtts.groupSize = 48
DBExportOpts = {'Tetrahedralize': 0, 'FileFormat': 'Legacy Ascii'}
ExportDatabase(ExportDBAtts, DBExportOpts)
SetTimeSliderState(7)
DrawPlots()
ExportDBAtts = ExportDBAttributes()
ExportDBAtts.allTimes = 0
ExportDBAtts.dirname = "./VisExport"
ExportDBAtts.filename = "file0007"
ExportDBAtts.timeStateFormat = "_%04d"
ExportDBAtts.db_type = "VTK"
ExportDBAtts.db_type_fullname = "VTK_1.0"
ExportDBAtts.variables = ("default")
ExportDBAtts.writeUsingGroups = 0
ExportDBAtts.groupSize = 48
DBExportOpts = {'Tetrahedralize': 0, 'FileFormat': 'Legacy Ascii'}
ExportDatabase(ExportDBAtts, DBExportOpts)
SetTimeSliderState(8)
DrawPlots()
ExportDBAtts = ExportDBAttributes()
ExportDBAtts.allTimes = 0
ExportDBAtts.dirname = "./VisExport"
ExportDBAtts.filename = "file0008"
ExportDBAtts.timeStateFormat = "_%04d"
ExportDBAtts.db_type = "VTK"
ExportDBAtts.db_type_fullname = "VTK_1.0"
ExportDBAtts.variables = ("default")
ExportDBAtts.writeUsingGroups = 0
ExportDBAtts.groupSize = 48
DBExportOpts = {'Tetrahedralize': 0, 'FileFormat': 'Legacy Ascii'}
ExportDatabase(ExportDBAtts, DBExportOpts)
