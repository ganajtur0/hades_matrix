# DESIGN erzeugen

import jp_design_os
from jp_design_os import *
from Muller import Muller
from hades.models.io import Ipin, Opin
from java.awt import Point

muller = Muller()
#muller.setSymbolType("SOUTH")
muller_s = Muller()
muller_s.setSymbolType("SOUTH")
muller_n = Muller()
muller_n.setSymbolType("NORTH")

clearDesign()

#inch:2400 == 1
muller_pos 	= Point(6000,3600)
muller_s_pos 	= Point(3000,3600)
muller_n_pos 	= Point(0,3600)

addComponentWithSymbol(muller, muller_pos,   "muller")
addComponentWithSymbol(muller_s, muller_s_pos,   "muller")
addComponentWithSymbol(muller_n, muller_n_pos,   "muller")
addComponeditor.getObjectCanvas().doFullRedraw()
