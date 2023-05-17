# DESIGN erzeugen

import jp_design_os
from jp_design_os import *
from Muller import Muller
from hades.models.io import Ipin, Opin
from java.awt import Point

muller = Muller()
#muller.setSymbolType("SOUTH")
ipin_a = Ipin()
ipin_b = Ipin()
opin   = Opin()

clearDesign()

#inch:2400 == 1
muller_pos 	= Point(6000,3600)
a_pos 		= Point(4800,2400)
b_pos		= Point(4800,7200)
y_pos 		= Point(10800,4800)

addComponentWithSymbol(muller, muller_pos,   "muller")
addComponentWithSymbol(ipin_a, a_pos,   "A")
addComponentWithSymbol(ipin_b, b_pos,   "B")
addComponentWithSymbol(opin, y_pos, "Y")

connectWithSignalPos(a_pos, "Y", muller_pos, "A")
connectWithSignalPos(b_pos, "Y", muller_pos, "B")
connectWithSignalPos(muller_pos, "Y", y_pos,   "A")

editor.getObjectCanvas().doFullRedraw()


# DESIGN mittels STL testen
import jp_sim_control
from VectorGen import *
from jp_stl import *

def stl_test():
    #####       
    # Initialisierung 
    ###  
    jp_design_os.updateDesign()
    jp_sim_control.updateSimulator()
    v = VectorGen()
   
    A = defPinByName("A")
    B = defPinByName("B")

    #####
    # Definition der Abtastpunkte
    ###
    addProbes(mode="ALL")
    probe = defProbesAfter("muller")

    #####
    # 4. Definiton der Stimuli
    ###
    v.defTiming(start=0.0, end=0.001)

    v.defFormat([
        A, B, probe
        ])

    v.defStimuli([
        1, 1, 1,
        0, 1, 1,
        1, 0, 1,
        0, 0, 0,
        0, 1, 0,
        1, 0, 0,
        1, 1, 1,
        ])

    v.setDebug(0)
    v.start()
    v.clearDesign()

#stl_test()
