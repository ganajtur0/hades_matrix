# DESIGN erzeugen: Micropipelines

# req[in]  >---->C1<--INV1-+--------->C3<--INV3-< ack[in]
#                |         |          |
#                |         |          |
#                |         |          |
# ack[out] <-----+-------->C2<--INV2--+---------> req[out]
#

import jp_design_os
from jp_design_os import *
from Muller import Muller
from hades.models.io import Ipin, Opin
from hades.models.gates import Inv
from java.awt import Point

editor = getEditor()
editor.doDeleteAll()

# objekte erzeugen
c1      = Muller()
c1.setSymbolType("SOUTH")
c2      = Muller()
c2.setSymbolType("NORTH")
c3      = Muller()
c3.setSymbolType("SOUTH")
req_in  = Ipin()
ack_in  = Ipin()
req_out = Opin()
ack_out = Opin()
inv1    = Inv()
inv2    = Inv()
inv3    = Inv()


#componenten dem design hinzufügen
addComponentWithSymbol( c1,      Point(3600, 1200),  "C1")
addComponentWithSymbol( c2,      Point(12000, 6600), "C2")
addComponentWithSymbol( c3,      Point(20400, 1200), "C3")       
addComponentWithSymbol( req_in,  Point(2400, 2400),  "REQ[in]")
addComponentWithSymbol( ack_in,  Point(28800, 2400), "ACK[in]",  mirror="@X")
addComponentWithSymbol( req_out, Point(28800, 7800), "REQ[out]")
addComponentWithSymbol( ack_out, Point(2400, 7800),  "ACK[out]", mirror="@X")
addComponentWithSymbol( inv1,    Point(10800, 1200), "INV1",     mirror="@X")
addComponentWithSymbol( inv2,    Point(19200, 6600), "INV2",     mirror="@X")
addComponentWithSymbol( inv3,    Point(27600, 1200), "INV3",     mirror="@X")

#signale erzeugen
connectWithSignal( req_in, "Y", c1,      "A", "req[in]")
connectWithSignal( c1,     "Y", c2,      "A", "C1.A",       wire_points="Point(4800,7800)")
connectWithSignal( c2,     "Y", c3,      "A", "C2.A",       wire_points="Point(13800,2400)") 
connectWithSignal( c3,     "Y", req_out, "A", "C3.A",       wire_points="Point(21600,7800)") 
connectWithSignal( inv1,   "Y", c1,      "B", "inv1")
connectWithSignal( inv2,   "Y", c2,      "B", "inv2")
connectWithSignal( inv3,   "Y", c3,      "B", "inv3")
connectWithSignal( ack_in, "Y", inv3,    "A", "ack[in]") 

connectToSignal( ack_out, "A", "C1.A", Point(4800,7800))
connectToSignal( inv1,    "A", "C2.A", Point(13200,2400))
connectToSignal( inv2,    "A", "C3.A", Point(21600,7800))


def createMicropipeline(length, x=0, y=0):
	r_shift = 10800

	# the first step
	_createOneStep(x, y)
	# REQ IN
	addComponentWithSymbol( Ipin(),  Point(x-600, y+1200))
	connectWithSignal(findSimObject(Point(x-600, y+1200)), "Y", findSimObject(Point(x,y)), "A")
	# ACK OUT
	s = findSignal(Point(x+1200, y+6000))
	addComponentWithSymbol( Opin(),  Point(x-600, y+6000), mirror="@X")
	connectToSignal(findSimObject(Point(x-600, y+6000)), "A", s.getSignal().getName(), Point(x+1200, y+6000))
	# the middle
	for i in range(length-1):
		x = x + r_shift 
		_createOneStep(x, y)
		# connect c
		s = findSignal(Point(x-r_shift+6600, y+1200))
		obj = findSimObject(Point(x, y))
		connectToSignal(obj, "A", s.getSignal().getName(), Point(x-r_shift+6600, y+1200))

		# connect inv
		s = findSignal(Point(x+1200, y+6000))
		obj = findSimObject(Point(x, y+6000))
		connectToSignal(obj, "A", s.getSignal().getName(), Point(x+1200, y+6000))

	# the and
	# ACK IN + 1/2 Step
	x_end = x+r_shift+600
	_createMullerInvPair(x_end, y, "SOUTH")
	addComponentWithSymbol( Ipin(), Point(x_end+5400+600, y+1200), mirror="@X")
	# connect ack_in and inv	
	connectWithSignal(findSimObject(Point(x_end+5400+600, y+1200)), "Y", findSimObject(Point(x_end+5400,y)), "A")
	# connect c and inv1
	s = findSignal(Point(x+6600, y+1200))
	connectToSignal(findSimObject(Point(x_end, y+1200)), "A", s.getSignal().getName(), Point(x+6600, y+1200))
	# REQ OUT
	addComponentWithSymbol( Opin(), Point(x_end+5400+600, y+6000))
	connectWithSignal(findSimObject(Point(x_end+5400+600, y+6000)), "A", findSimObject(Point(x+r_shift,y+6000)), "A")

	# connect c and inv2
	print Point(x+r_shift+1800, y+6000)
	s = findSignal(Point(x, y+6000))
	print s
	s = findSignal(Point(x+r_shift, y+6000))
	print s
	#s = findSignal(Point(x+r_shift+1800, y+6000))
	#print s
	#s = findSignal(Point(12000, 18000))
	#print s
	connectToSignal(findSimObject(Point(x_end, y+1200)), "Y", s.getSignal().getName(), Point(x+r_shift+1800, y+6000))


def _createOneStep(x, y):
	y_offset = 4800
	r_shift = 5400

	_createMullerInvPair(x,y, "SOUTH")	
	_createMullerInvPair(x+r_shift,y+y_offset, "NORTH")	
	# connect the mullers
	connectWithSignal(findSimObject(Point(x,y)), "Y", findSimObject(Point(x+r_shift,y+y_offset)), "A", wire_points="Point(x+1200, y+y_offset+1200)")
	# connect muller-inv
	connectWithSignal(findSimObject(Point(x+r_shift,y+y_offset)), "Y", findSimObject(Point(x+r_shift,y)), "A", wire_points="Point(x+r_shift+1200, y+1200)")



def _createMullerInvPair(x, y, type):
	r_shift = 5400

	c = Muller()
	c.setSymbolType(type)
	inv = Inv()
	addComponentWithSymbol(c, Point(x,y))
	addComponentWithSymbol(inv, Point(x+r_shift,y), mirror="@X")
	connectWithSignal(inv, "Y", c, "B") 

createMicropipeline(2, y=12000)

# signale initialisieren
editor.initSignals(0)

from VectorGen import *
from jp_stl import *
import jp_sim_control

def stl_test():
       
    #####       
    # Initialisierung 
    ###  
    jp_design_os.updateDesign()
    jp_sim_control.updateSimulator()
    v = VectorGen()
    
    REQ_IN = defPinByName("REQ[in]")
    ACK_IN = defPinByName("ACK[in]")
       
    #####
    # Definition der Abtastpunkte
    ###
    addProbes(mode="ALL")
    probe_ack_out = defProbesBevor("ACK[out]")
    probe_req_out = defProbesBevor("REQ[out]")
    print probe_ack_out, probe_req_out
    
    #####
    # 4. Definiton der Stimuli
    ###
    v.defTiming(start=0.0, end=0.001)

    v.defFormat([REQ_IN, ACK_IN])
    v.defStimuli([
        0,1,
        0,0
        ])

    #v.defFormat([
    #    REQ_IN, ACK_IN, probe_ack_out, probe_req_out
    #    ])

    #v.defStimuli([
    #    0, 1, 0, 0,
    #    0, 0, 0, 0,
    #    1, 0, 1, 1,
    #    0, 0, 0, 1,
    #    1, 0, 1, 1,
    #    0, 0, 1, 1,
    #    1, 0, 1, 1,
    #    0, 1, 0, 0,
    #    0, 0, 0, 1,
    #    0, 1, 0, 0,
    #    0, 0, 0, 0,
    #    ])
    
    #v.setDebug(1)
    v.start()
    
#stl_test()
