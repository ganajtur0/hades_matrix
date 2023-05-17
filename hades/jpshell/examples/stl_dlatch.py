import jp_design_os
import jp_sim_control
from jp_stl import *
from VectorGen import *

#####       
# 1. Initialisierung 
###        
jp_design_os.openDesign("/hades/examples/simple/dlatch.hds")
jp_design_os.updateDesign()
jp_sim_control.updateSimulator()
v = VectorGen()


#####
# 2. Definition der Ein- und Ausgaenge
###
C = defPinByName("C")
D = defPinByName("D")
Q = defPinByName("Q")


#####
# 3. Definition der Abtastpunkte
###
addProbes(mode="ALL")
n5, n4, n3, n2, n1, n0 = defAllProbes()

#n5 = defProbesBevor(Q)
#n1 = defProbesAfter(C)
#n0 = defProbesAfter(D)


#####
# 4. Definiton der Stimuli
###
v.defTiming(start=0.0, end=1E-8)

v.defFormat([
    C, D, n5
    ])

v.defStimuli([
    1, 1, ["AND", n1, n0],
    0, 1, ["OR", n1, n0],
    0, 0, ["OR", n1, n0],
    1, 0, ["NOT", n1],
    1, 1, 1,
    1, 0, ["AND", n0, n1, n2, n3, n4, n5],
    1, 1, ["OR", n0, n1, n2, n3, n4, n5]
    ])


def last_test(count, v):
    state = 0
    test = []
    for i in range(count):
        state = not state
        if(state):
            test.append(1)
            test.append(1)
            test.append(1)
        else:
            test.append(0)
            test.append(0)
            test.append(1)

    v.defStimuli(test, debug=1)

######
# 5. Starten  (Durch hinzufügen zum design)
###
#v.setDebug(1)
#last_test(10000, v)
v.start()


