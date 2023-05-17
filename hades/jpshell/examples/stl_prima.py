import jp_design_os
import jp_sim_control
from jp_stl import *

#####       
# 1. Initialisierung 
###        
openDesign("/hades/examples/prima/prima.hds")
jp_design_os.updateDesign()
jp_sim_control.updateSimulator()


#####
# 2. Definition der Ein- und Ausgaenge
###
clock = defPinByName("clock")
switch = defPinByName("switch")
nreset = defPinByName("nreset")

#####
# 3. Definition der Spannungspegel 
###
#level = {'U':0, 'X':1, '0':2, '1': 3}


#####
# 4. Definition der Abtastpunkte
###
probes = defAllProbes()

#alternativen
#n5 = defProbesBevor(Q)
#n5 = defProbesAfter("i2")

 
#####
# 5. Definiton der Clocks, die an die IPins angelegt werden
###
#addClk(ipin=clock, offset=0.0, period=0.3, dutycycle=33.0)
addClock(ipin=clock, offset=0.0, period=0.5, dutycycle=0.33)
#addClk(ipin=C, offset=0.0, period=0.5, dutycycle=50.0)

#####
# 6. Definiton der Stimuli, Format: Ipin, value, atTime (Object, int, douple) 
###
#stimuli_init = [C, level['1'], 0.0,
#		D, level['1'], 0.0]

#stimuli = [D, level['0'], 0.15,		
#	   D, level['X'], 0.2,		
#	   D, level['U'], 0.4,		
#	   D, level['1'], 0.5,		
#	   D, level['0'], 0.55,		
#	   D, level['1'], 0.8]		
	  

#####
# 7. Definition der Erwartungswerte, Format: (probe, value)* am ende atTime 
###
#test_init = [n5, level['1'], 0.1]

#test_ende = [n5, level['1'], 
#	     n4, level['0'], 
#	     n3, level['1'], 
#	     n2, level['0'], 
#	     n1, level['1'], 
#	     n0, level['1'], 1.0] 

#####
# start test 
###
#result = execTest(stimuli_init, test_init)

#if (result):
#    result = execTest(stimuli, test_ende)
#    if (result):
#	printAllProbes(1.0)
#	print "D-latch test ok"
#    else:
#	print "D-latch test failed"
#else:
#    print "D-latch init failed"
#####
# end test
###


