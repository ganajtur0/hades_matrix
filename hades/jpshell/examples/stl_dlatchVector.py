import jp_design_os
import jp_sim_control
from jp_stl import *

#####       
# 1. Initialisierung 
###        
openDesign("/hades/examples/simple/dlatch.hds")
jp_design_os.updateDesign()
jp_sim_control.updateSimulator()
jp_sim_control.pauseSimulator()

#####
# 2. Definition der Ein- und Ausgaenge
###
D, C = defAllPins("Ipin")
Q = defPinByName("Q")


#####
# 3. Definition der Spannungspegel 
###
level = {'U':0, 'X':1, '0':2, '1': 3}


#####
# 4. Definition der Abtastpunkte
###
n5, n4, n3, n2, n1, n0 = defAllProbes()

#alternativen
n5 = defProbesBevor(Q)
n5 = defProbesAfter("i2")

 
#####
# 5. Definiton der Clocks, die an die IPins angelegt werden
###
#?? Warum laufen sie jetzt sofort, wenn ich den simulator starte ?
# warum kein wakeup s. startClocks ?
def startClocks():
    jp_sim_control.resetSimulator()
    addClock(ipin=D, offset=0.0, period=0.5, dutycycle=0.5)
    addClock(ipin=C, offset=0.0, period=0.5, dutycycle=0.5)
    execSequence(stimuli_clock)

    
#####
# 6. Definiton der Stimuli, Format: Ipin, value, atTime (Object, int, douple) 
###
stimuli_init = [C, level['1'], 0.0,
                 D, level['1'], 0.0]

stimuli_test = [D, level['0'], 0.15,		
                D, level['X'], 0.2,		
                D, level['U'], 0.4,		
                D, level['1'], 0.5,		
                D, level['0'], 0.55,		
                D, level['1'], 0.8]

stimuli_clock = [C, level['0'], 0.0,
                 D, level['0'], 0.0,
                 C, level['U'], 1.0,
                 D, level['U'], 1.0,
                 C, level['X'], 2.0,
                 D, level['X'], 2.0,
                 C, level['1'], 3.0,
                 D, level['1'], 3.0,
                 C, level['0'], 4.0,
                 D, level['1'], 4.0,
                 C, level['1'], 5.0,
                 D, level['0'], 5.0,
                 C, level['1'], 5.0,
                 D, level['1'], 5.0,]


#####
# 7. Definition der Erwartungswerte, Format: (probe, value)* am ende atTime 
###
test_init = [n5, level['1'], 0.1]

test_ende = [n5, level['1'], 
	     n4, level['0'], 
	     n3, level['1'], 
	     n2, level['0'], 
	     n1, level['1'], 
	     n0, level['1'], 1.0] 

#####
# test 
###
def test():
    jp_sim_control.runSimulator()
    result = execTest(stimuli_init, test_init)
    if (result):
        result = execTest(stimuli_test, test_ende)
        if (result):
            printAllProbes(1.0)
            print "D-latch test ok"
        else:
            print "D-latch test failed"
    else:
        print "D-latch init failed."
       
    
#####
# main
###
#jp_sim_control.runSimulator()
from VectorGen import *
v = VectorGen()
v.defTiming([0.5, 1.0, 1.5])
v.defFormat([C, D])
v.defStimuli( [level['0'], level['0'],
               level['1'], level['1'],
               level['0'], level['0']])
              
