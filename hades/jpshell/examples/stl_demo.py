import time
from jp_design_os import *
from jp_stl import *


# 1. Initialisierung
openDesign("/hades/examples/simple/dlatch.hds", "D-latch")
updateDesign()
debug = 1

# 2. Definition der Ein- und Ausgaenge
D, C = defPin("Ipin")
Q = defPin("Opin")
if (debug):
    print "C: ", C, "D: ", D, "Q: ", Q

# 3. Definition der Spannungspegel
#level = {'vil':0, 'vih':5, 'vol':0, 'vol':5}
level = {'U':0, 'X':1, '0':2, '1': 3}


# 4. Zeitschema (ist mir noch etwas unklar!)
# - a) Zeitauflösung des Simulators ? 
#      Soll hier sowas wie: simulator.runFor(double) oder simulator. singleStep() hin ?
# - b) Zeitraster der Clock ? was ist der unterschied zu 5. ?
# - c) Zeitraster der Stimuli ?
delay = 0.5


# 5. Definiton der Clocks
# - Frage wie würde es für ".1111...." aussehen?
#clk.setOffset('0.1')
#clk.setDutycycle('0.5')
#clk.setPeriod('1')


# 6. Definition der Abtastzeitpunkte
# IDEE: n0 = getProbeAfter(C) und n5 = getProbeBefore(Q) oder so !!!!!
n5, n4, n3, n2, n1, n0 = defProbes()
if (debug):
    print "n0: ", n0, "n1: ", n1, "n2: ", n2, "n3: ", n3, "n4: ", n4, "n5: ", n5

# 7. Definiton des Eingabeformates
sequence = [C, C, D, D]


# 8. Definition der Stimuli / Erwartungswerte
test_init = [n5, level['1']]
test_ende = [n5, level['1'], 
	     n4, level['0'], 
	     n3, level['1'], 
	     n2, level['0'], 
	     n1, level['0'], 
	     n0, level['1']] 


# start test
if (debug):
    print "D-latch test: phase 1"
    printAllProbes()
result = execTest(sequence, test_init, sleepTime=delay)
if (debug):
    print "\nD-latch test: phase 2"
    printAllProbes()

if (result):
    result = execTest([D], test_ende, count=9, sleepTime=delay)
    if (debug):
	print "\nD-latch test: phase 3"
	printAllProbes()
    if (result):
	print "D-latch test ok"
    else:
	print "D-latch test failed"

# end test



