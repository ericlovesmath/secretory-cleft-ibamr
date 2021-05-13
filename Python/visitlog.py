# Visit 3.1.2 log file
ScriptVersion = "3.1.2"
if ScriptVersion != Version():
    print "This script is for VisIt %s. It may not work with version %s" % (ScriptVersion, Version())
ShowAllWindows()
OpenDatabase("~/Desktop/UCI/Simulations/BIG_Nom", 0)
# The UpdateDBPluginInfo RPC is not supported in the VisIt module so it will not be logged.
OpenDatabase("~/Desktop/UCI/Simulations/BIG_Nom/viz_IB2d/lag_data.visit", 0)
