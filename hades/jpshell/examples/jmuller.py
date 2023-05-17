# DESIGN erzeugen

import jp_design_os
from jp_design_os import *
from hades.models.gates import Muller
from hades.models.io import Ipin, Opin
from java.awt import Point

muller = Muller()
#muller.setSymbolType("vertikal")
ipin_a = Ipin()
ipin_b = Ipin()
opin   = Opin()

#BUG: signal not or forever deletet
clearDesign()

#inch:2400 == 1
addComponentWithSymbol(muller, Point(6000,3600),   "muller")
addComponentWithSymbol(ipin_a, Point(4800,2400),   "A")
addComponentWithSymbol(ipin_b, Point(4800,7200),   "B")
addComponentWithSymbol(opin,   Point(10800, 4800), "Y")

connectWithSignal(ipin_a, "Y", muller, "A")
connectWithSignal(ipin_b, "Y", muller, "B")
connectWithSignal(muller, "Y", opin,   "A")

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


stl_test()
