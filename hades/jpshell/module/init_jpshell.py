# Java-Python-Shell-INIT-Skript
# Umleiten der Ausgabe in das Java-Gui
import sys
try:
	sys.stdout = printStream
	sys.stderr = printStream
except:
	pass

import jp_os
import jp_design_os
import jp_sim_control
import jp_meta_tools
from jp_tools import *
from jp_design_os import *
from jp_sim_control import *
from jp_meta_tools import *

# set the editor into the local namespace from jp_design_os
jp_design_os.setEditor(editor)

# set usefulls globals
design = jp_design_os.getDesign()
simulator = jp_sim_control.getSimulator()



    
