from jp_design_os import *
from jp_stl import *


# 1. Initialisierung
openDesign("/hades/examples/simple/ascii-display.hds", "Ascii-Display-Demo")
updateDesign()
debug = 1


# 2. Definition der Ein- und Ausgaenge 
#(wozu brauche man eigentlich die Ausgaenge, wir haben doch die probes ?) 
H, H1 = defAllPins("HexSwitch*.")
if (debug):
    print "HexSwitch:" 
    print "H: ", H
    print "H1: ", H1

#Version 1
#A, A4, A3, A2, A1 = defAllPins("AsciiDisplay")
#if (debug):
#    print "AsciiDisplay:"
#    print "A: ", A
#    print "A1: ", A1
#    print "A2: ", A2
#    print "A3: ", A3
#    print "A4: ", A4

#Version 2
A = defPinByName("AsciiDisplay")
if (debug):
    print "AsciiDisplay:"
    print "A: ", A


# 3. Definition der Spannungspegel
logicLevel = {'U':0, 'X':1, '0':2, '1': 3}
level = {'A':10, 'B':12, 'C': 13, 'D':14, 'E':15, 'F':16}


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
n9, n8, n7, n6, n5, n4, n3, n2, n1, n0 = defAllProbes()
if (debug):
    for i in range(9):
	exec("n = n"+repr(i)) 
	print "n"+repr(i)+": ", n 


# 7. Definiton des Eingabeformates
sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
	    level['A'], level['B'], level['C'], level['D'], level['E']]


# 8. Definition der Stimuli / Erwartungswerte
input_sequence = [H, H1]


#test_init = [n5, level['1']]
test_ende = [n9, logicLevel['1'], 
	     n8, logicLevel['0'], 
	     n7, logicLevel['1'],  
	     n6, logicLevel['1'], 
	     n5, logicLevel['1'], 
	     n4, logicLevel['1'], 
	     n3, logicLevel['1'], 
	     n2, logicLevel['1'], 
	     n1, logicLevel['1'], 
	     n0, logicLevel['1']]


# start test (a) zeit ~130 sec)
if (debug):
    print " Ascii-Display-Demo test: phase 1"
    printAllProbes()

#a)
#for i in sequence:
#    execSequence(iPins=[H], levelSequence=sequence, sleepTime=delay, debug=0)
#    execSequence(iPins=[H1], levelSequence=[i], sleepTime=delay, debug=0)

#b)
execSequence(iPins=[H], levelSequence=sequence, sleepTime=delay, debug=0)
execSequence(iPins=[H1], levelSequence=sequence, sleepTime=delay, debug=0)

if (debug):
    print " Ascii-Display-Demo test: phase 2"
    printAllProbes()

result = execTest([], test_ende)
if (result):
    print "Ascii-Display-Demo test ok"
else:
    print "Ascii-Display-Demo test failed"
# end test



