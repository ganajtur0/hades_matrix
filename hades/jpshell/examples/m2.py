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
	s = findSignal(Point(x, y+6000))
	s = findSignal(Point(x+r_shift, y+6000))
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
	connectWithSignal(findSimObject(Point(x,y)), "Y", findSimObject(Point(x+r_shift,y+y_offset)), "A", wire_points=Point(x+1200, y+y_offset+1200))
	# connect muller-inv
	connectWithSignal(findSimObject(Point(x+r_shift,y+y_offset)), "Y", findSimObject(Point(x+r_shift,y)), "A", wire_points=Point(x+r_shift+1200, y+1200))



def _createMullerInvPair(x, y, type):
	r_shift = 5400

	c = Muller()
	c.setSymbolType(type)
	inv = Inv()
	addComponentWithSymbol(c, Point(x,y))
	addComponentWithSymbol(inv, Point(x+r_shift,y), mirror="@X")
	connectWithSignal(inv, "Y", c, "B") 


# signale initialisieren
editor.initSignals(0)



createMicropipeline(5)
