import jp_design_os
from jp_design_os import *
from Muller import Muller
from hades.models.io import Ipin, Opin
from hades.models.gates import InvSmall
from java.awt import Point
from Register import Register
from Delay import Delay

clearDesign()

# 1. Stufe
reg_1 = Register()
muller_1 = Muller()
muller_1.setSymbolType("SOUTH")
inv_c_1 = InvSmall()
req_in = Ipin()
data_in = Ipin()
d_1 = Delay()
ack_out = Opin()

# 1. Stufe
muller_1_pos	= Point(7200,0)
reg_1_pos		= Point(7200,3000)
inv_c_1_pos		= Point(12000, 600)
req_in_pos		= Point(5400, 1200)
data_in_pos		= Point(5400, 6000)
d_1_pos	   		= Point(9600, 10200)
ack_out_pos		= Point(5400, 10800)

# 1. Stufe
addComponentWithSymbol(muller_1, 	muller_1_pos,   "muller")
addComponentWithSymbol(reg_1, 		reg_1_pos,		"register")
addComponentWithSymbol(inv_c_1,		inv_c_1_pos, 				mirror="@X")
addComponentWithSymbol(req_in, 		req_in_pos, 	"REQ_in")
addComponentWithSymbol(data_in, 	data_in_pos, 	"data_in")
addComponentWithSymbol(d_1, 		d_1_pos)
addComponentWithSymbol(ack_out, 	ack_out_pos,	"ACK_out", mirror="@X")

# 1. Stufe
connectWithSignalPos(muller_1_pos, 	"Y", 	reg_1_pos, 		"C")
connectWithSignalPos(reg_1_pos, 	"dP", 	inv_c_1_pos, 	"A")
connectWithSignalPos(inv_c_1_pos, 	"Y", 	muller_1_pos, 	"B")
connectWithSignalPos(req_in_pos, 	"Y", 	muller_1_pos, 	"A")
connectWithSignalPos(data_in_pos, 	"Y", 	reg_1_pos, 		"A")
connectWithSignalPos(reg_1_pos, 	"dC", 	ack_out_pos, 	"A", wire_points="Point(8400, 10800)")
signal_name = findSignal(Point(8400, 10800)).getSignal().getName()
obj = findSimObject(d_1_pos)
connectToSignal(obj, "A", signal_name, Point(8400, 10800))

# 2. Stufe
reg_2 = Register()
muller_2 = Muller()
muller_2.setSymbolType("NORTH")
inv_2 = InvSmall()
d_2 = Delay()

# 2. Stufe
reg_2_pos		= Point(17400, 9000)
muller_2_pos	= Point(17400, 9600)
inv_2_pos		= Point(22200, 10200)
d_2_pos			= Point(19800, 600)

# 2. Stufe
addComponentWithSymbol(muller_2, 	muller_2_pos,   "muller")
addComponentWithSymbol(reg_2, 		reg_2_pos,		"register",	mirror="@Y")
addComponentWithSymbol(inv_2,		inv_2_pos,	 				mirror="@X")
addComponentWithSymbol(d_2, 		d_2_pos)

# 2.Stufe
connectWithSignalPos(muller_2_pos,  "Y",    reg_2_pos,      "C")
connectWithSignalPos(reg_2_pos, 	"dP", 	inv_2_pos, 		"A")
connectWithSignalPos(inv_2_pos, 	"Y", 	muller_2_pos, 	"B")

# 1+2 Stufe
connectWithSignalPos(d_1_pos,		"Y", 	muller_2_pos,	"A")
connectWithSignalPos(reg_1_pos,		"P", 	d_2_pos,		"A", wire_points="Point(12000,9600), Point(16800,9600), Point(16800,1200)")
 


editor.getObjectCanvas().doFullRedraw()


