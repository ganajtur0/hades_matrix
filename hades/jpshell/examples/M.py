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
connectToSignal(obj, "A", signal_name, Point(8400, 10800), at_pos=2)

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
connectWithSignalPos(reg_1_pos,		"Y", 	reg_2_pos,	"A")
 
# 3. Stufe
reg_3 		= Register()
muller_3 	= Muller()
muller_3.setSymbolType("SOUTH")
inv_3 		= InvSmall()
ack_in 		= Ipin()
data_out 	= Opin()
d_3 		= Delay()
req_out 	= Opin()

# 3. Stufe
reg_3_pos		= Point(27600, 3000)
muller_3_pos	= Point(27600, 0)
inv_3_pos		= Point(32400, 600)
d_3_pos			= Point(30000, 10200)
ack_in_pos		= Point(35400, 1200)
data_out_pos	= Point(35400, 6000)
req_out_pos		= Point(35400, 10800)

# 3.Stufe
addComponentWithSymbol(muller_3, 	muller_3_pos,   "muller")
addComponentWithSymbol(reg_3, 		reg_3_pos,		"register")
addComponentWithSymbol(inv_3,		inv_3_pos, 					mirror="@X")
addComponentWithSymbol(ack_in, 		ack_in_pos, 	"ACK_in", 	mirror="@X")
addComponentWithSymbol(data_out, 	data_out_pos, 	"data_out")
addComponentWithSymbol(d_3, 		d_3_pos)
addComponentWithSymbol(req_out, 	req_out_pos,	"REQ_out")

# 3.Stufe
connectWithSignalPos(muller_3_pos, 	"Y", 	reg_3_pos, 		"C")
connectWithSignalPos(reg_3_pos, 	"dP", 	inv_3_pos, 		"A")
connectWithSignalPos(inv_3_pos, 	"Y", 	muller_3_pos, 	"B")
connectWithSignalPos(d_3_pos, 		"Y", 	req_out_pos, 	"A")
connectWithSignalPos(reg_3_pos, 	"Y", 	data_out_pos,	"A")
connectWithSignalPos(ack_in_pos, 	"Y", 	reg_3_pos,		"P", wire_points="Point(34800,1200), Point(34800,9600), Point(32400,9600)")

# 2.+3. Stufe
connectWithSignalPos(reg_2_pos,		"Y", 	reg_3_pos,		"A")
connectWithSignalPos(d_2_pos,		"Y", 	muller_3_pos,	"A")
connectWithSignalPos(reg_2_pos,		"P", 	d_3_pos,		"A", wire_points="Point(22200,2400), Point(27000,2400), Point(27000,10800)")

# 2.Stufe
signal_name = findSignal(Point(19800, 1200)).getSignal().getName()
obj = findSimObject(reg_2_pos)
connectToSignal(obj, "dC", signal_name, Point(18600, 1200), at_pos=4)

# 3.Stufe
signal_name = findSignal(Point(30000, 10800)).getSignal().getName()
obj = findSimObject(reg_3_pos)
connectToSignal(obj, "dC", signal_name, Point(28800, 10800), at_pos=4)




from VectorGen import *
from jp_stl import *
import jp_sim_control

def stl_init():
    jp_design_os.updateDesign()
    jp_sim_control.updateSimulator()
    v = VectorGen()
    
    ACK_IN 	= defPinByName("ACK_in")

    v.defTiming(start=0.0, end=0.001)

    v.defFormat([ACK_IN])

    v.defStimuli([1, 0])
    v.start()
    v.clearDesign()	
	
################
# main
############
editor.initSignals(0)
import time
time.sleep(0.5)
editor.initSignals(0)

stl_init()

editor.getObjectCanvas().doFullRedraw()
