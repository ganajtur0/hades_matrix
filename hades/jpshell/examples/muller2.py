from jp_design_os import *
from Muller import Muller
from hades.models.io import Ipin, Opin
from java.awt import Point

muller_pos 	= Point(6000,3600)
a_pos 		= Point(4800,2400)
b_pos		= Point(4800,7200)
y_pos 		= Point(10800,4800)

addComponentWithSymbol(Muller(), muller_pos,   "muller")
addComponentWithSymbol(Ipin(), a_pos,   "A")
addComponentWithSymbol(Ipin(), b_pos,   "B")
addComponentWithSymbol(Opin(), y_pos, "Y")

connectWithSignalPos(a_pos, "Y", muller_pos, "A")
connectWithSignalPos(b_pos, "Y", muller_pos, "B")
connectWithSignalPos(muller_pos, "Y", y_pos,   "A")
