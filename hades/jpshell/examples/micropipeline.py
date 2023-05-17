# DESIGN erzeugen: Micropipelines

# req[in]  >---->C1<--INV1-+--------->C3<--INV3-< ack[in]
#                |         |          |
#                |         |          |
#                |         |          |
# ack[out] <-----+-------->C2<--INV2--+---------> req[out]
#

import jp_design_os
from jp_design_os import *
from async_gates import Muller
from hades.models.io import Ipin, Opin
from hades.models.gates import Inv
from java.awt import Point

editor = getEditor()
editor.doDeleteAll()

# objekte erzeugen
c1      = Muller()
c2      = Muller()
c3      = Muller()
req_in  = Ipin()
ack_in  = Ipin()
req_out = Opin()
ack_out = Opin()
inv1    = Inv()
inv2    = Inv()
inv3    = Inv()

#componenten dem design hinzufügen
addComponentWithSymbol( c1,      Point(3600,1800),  "C1")
addComponentWithSymbol( c2,      Point(12000,6600), "C2")
addComponentWithSymbol( c3,      Point(20400,1800), "C3")
addComponentWithSymbol( req_in,  Point(2400,2400),  "REQ[in]")
addComponentWithSymbol( ack_in,  Point(31200,3000), "ACK[in]")
addComponentWithSymbol( req_out, Point(28800,7800), "REQ[out]")
addComponentWithSymbol( ack_out, Point(1200,8400),  "ACK[out]")
addComponentWithSymbol( inv1,    Point(8400,1800),  "INV1")
addComponentWithSymbol( inv2,    Point(16800,6600), "INV2")
addComponentWithSymbol( inv3,    Point(25200,1800), "INV3")


#signale erzeugen
connectWithSignal( req_in, "Y", c1,      "A", Point(2400,2400),  Point(3600,2400),  "req[in]-c1")
connectWithSignal( inv1,   "Y", c1,      "B", Point(10800,3000), Point(3600,3600),  "inv1-c1")
connectWithSignal( c1,     "Y", ack_out, "A", Point(7200,3000),  Point(1200,8400),  "c1-ack[out]")
connectWithSignal( c1,     "Y", c2,      "A", Point(7200,3000),  Point(12000,7200), "c1-c2")
connectWithSignal( inv2,   "Y", c2,      "B", Point(19200,7800), Point(12000,8400), "inv2-c2")
connectWithSignal( c2,     "Y", inv1,    "A", Point(15600,7800), Point(8400,3000),  "c2-inv1") 
connectWithSignal( c2,     "Y", c3,      "A", Point(15600,7800), Point(20400,2400), "c2-c3")
connectWithSignal( inv3,   "Y", c3,      "B", Point(27600,3000), Point(20400,3600), "inv3-c3")
connectWithSignal( c3,     "Y", inv2,    "A", Point(24000,3000), Point(16800,7800), "c3-inv2") 
connectWithSignal( ack_in, "Y", inv3,    "A", Point(31200,3000), Point(25200,3000), "c3-inv2") 
connectWithSignal( c3,     "Y", req_out, "A", Point(24000,3000), Point(28800,7800), "c3-req[out]")

# signale initialisieren, noch gibts timing probleme
# todo....
editor.initSignals(0)
