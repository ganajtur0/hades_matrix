import sys
import string
import time
import jp_design_os
import jp_sim_control
from hades.models import StdLogic1164
from hades.signals import SignalStdLogic1164
from hades.models.io import ClockGen

# global logic const
global X, U
X='X'
U='U'

#def openDesign(resourcename):
#    ''' <None> openNewEditorWithDesign(resourcename)
#    openDesign try to open a hades-file (.hds) specified 
#    by the resourcename in a new HADES-Editor. 
#    For examble:
#    - openDesign("/hades/examples/simple/dlatch.hds")
#    '''
#    editor = jp_design_os.getEditor()
#    editor.doOpenDesign(resourcename, 0)




def _getDesignName(resourcename):
    sl = string.split(resourcename, "/")
    n_tmp = sl[-1]
    s = string.split(n_tmp, ".")
    design_name = s[0]
    return design_name

	

def printAllProbes(time):
    simulator = jp_sim_control.getSimulator()
    if(time>simulator.getSimTime()):
	print "printAllProbesAtTime("+str(time)+") are in future, canceld !"
    else:
	design = jp_design_os.getDesign()
	signals = design.getSignals()
	while(signals.hasMoreElements()):
	    signal = signals.nextElement()
	    p_tmp = signal.getProbe()
	    p_name = p_tmp.getName()
	    p_value = StdLogic1164(p_tmp.getValue(time))
	    print "probe: ",p_name, ", value: ", p_value, ", time: ", time


#old, without Stimuli-Class
#def execSequence(stimuli, debug=0):
#    if(debug):
#	print stimuli, len(stimuli)
#   i = 0
#    while(i<len(stimuli)):
#	pin = stimuli[i] 
#	value = StdLogic1164(stimuli[i+1]) 
#	time = stimuli[i+2] 
#	pin.setValueAtTime(value, time)
#	i = i + 3


#new, witch Stimuli-Class
#def execStimulus(stimulus, debug=0):
#    if(debug):
#	print stimulus
#    pin = stimulus.getPin() 
#    value = StdLogic1164(stimulus.getValue()) 
#    time = stimulus.getTime()
#    pin.setValueAtTime(value, time)
#	


#def execTest(stimuli, test, debug=0):
#    execSequence(stimuli, debug)
#
#    #########################
#    # auf den simulator warten
#    ##########
#    testTime=test[-1]
#    time.sleep(testTime)
#
#    i = 0
#    while (i < len(test)-1):
#	result = testProbe(test[i], StdLogic1164(test[i+1]), testTime, debug)
#	if (not result):
#	    return 0
#	i = i + 2
#    return 1


#def testProbe(probe, state, testTime, debug=0):
#    probeValue = StdLogic1164(probe.getValue(testTime))
#    if ( probeValue == state):
#	result = 1
#        if(debug):
##            _result="true"
#    else:
#        result = 0
#        if(debug):
#            _result="false"
#            
#    if(debug):
#	print "testProbe: ", probe.getName(), probeValue, state, testTime, _result
##        
#    return result


def defAllPins(pattern):
    pins = jp_design_os.get(pattern)
    return pins


def defPinByName(name):
    design = jp_design_os.getDesign()
    pin =  jp_design_os.getByName(name)
    return pin


def addProbes(mode):
    editor = jp_design_os.getEditor()
    mode = string.upper(mode)
    if mode == "ALL":
        editor.addProbesToAllSignals()
    elif mode == "TOPLEVEL":
        editor.addProbesToToplevelSignals()
    elif mode == "TOPLEVELIO":
        editor.addProbesToToplevelIO() 


def addProbeByName(signal_name):
    editor = jp_design_os.getEditor()
    editor.addProbeToSignal(signal_name)

    
def defAllProbes():
    design = jp_design_os.getDesign()
    signals = design.getSignals()
    probes = []
    for s in signals:
	probes.append(s.getProbe())
    return probes


def defProbeByName(name):
    design = jp_design_os.getDesign()
    signal = design.getSignal(name)
    probe = signal.getProbe()
    return probe


def defProbesBevor(component):
    try:
        ports = component.getPorts()
    except:
        component = defPinByName(component)
        ports = component.getPorts()

    probes = []
    for port in ports:
        if(port.isInputPort()):
            signal = port.getSignal()
            if(signal):
                probes.append(signal.getProbe())

    if (len(probes)<=1):
        return probes[0]
    else:
        return probe


def defProbesAfter(component):
    try:
        ports = component.getPorts()
    except:
        component = defPinByName(component)
        ports = component.getPorts()

    probes = []
    for port in ports:
        if(not port.isInputPort()):
            signal = port.getSignal()
            if(signal):
                probes.append(signal.getProbe())
    if (len(probes)<=1):
        return probes[0]
    else:
        return probe


def addClock(ipin, offset, period, dutycycle):
    clk = ClockGen()
    clk.setOffset(offset)
    clk.setPeriod(period)
    clk.setDutycycle(dutycycle)
    design = jp_design_os.getDesign()
    design.addComponent(clk, "STL_CLOCK")
    signal = ipin.getPort("Y").getSignal()
    signal.connect(clk.getPorts()[0])


#def startClocks():
#    design = jp_design_os.getDesign()
#    clocks = design.get("STL_CLOCK")
#    for clk in clocks:
#        clk.wakeup( clk )


    


#def simulateEvent(iPin, level=""):
#    ''' <None> simulateEvent(iPin, level="")
#    simulateEvent simulate an interaktive Event on a Input.
#   ... method in constuction ...
#    '''
#    import java
#
#    iPinClass = iPin.getClass()
#
#    if (not level):
#	try:
#	    if (iPinClass.getMethod('mousePressed', [java.awt.event.MouseEvent])):
#		m = java.awt.event.MouseEvent(java.awt.Button(), java.awt.event.MouseEvent.MOUSE_CLICKED, 0,0,0,0,1,0)
#		iPin.mousePressed(m)
#		return
#	except:
#	    print "jp_stl.simulateEvent error:", sys.exc_type, sys.exc_value
#
#    if(level):
#	try:
#	    if (iPinClass.getMethod('setIndex', [java.lang.Integer.TYPE])):
#		iPin.setIndex(level)
#		return
#	except:
#	    print "jp_stl.simulateEvent error:", sys.exc_type, sys.exc_value
#
#    print "ERROR: Can't simulate event for component ",iPin 


    #old
    #c = iPin.getClass()
    #n = string.split(c.__name__, ".")
    #iPinClass = n[-1]
   
    #if(iPinClass == "Ipin" or iPinClass == "DiodeSwitch"):
	#from java.awt.event import MouseEvent
	#from java.awt import Button
	#m = MouseEvent(Button(), MouseEvent.MOUSE_CLICKED, 0,0,0,0,1,0)
	#iPin.mousePressed(m)
    #elif(iPinClass == "HexSwitch"):
	#iPin.setIndex(level)


#def execSequence(iPins, levelSequence, count=1, sleepTime=0, debug=0):
#    while(count>0):
#	for pin in iPins:
#	    if(debug):
#		print pin
#	    if (levelSequence):
#		for level in levelSequence:
#		    simulateEvent(pin, level)
#		    time.sleep(sleepTime)
#		    if(debug):
#			printAllProbes()
#	    else:
#		simulateEvent(pin)
#		time.sleep(sleepTime)
#		if(debug):
#		    printAllProbes()
#	count = count - 1



#def execTest(iPins, test, levelSequence=[], count=1, sleepTime=0, debug=0):
#    execSequence(iPins, levelSequence, count, sleepTime, debug)
#
#    result = 0
#    i = 0
#    while (i < len(test)):
#	if(debug): 
#	    print "test: ", test[i], test[i+1]
#	if testProbe(test[i], test[i+1]):
#	    result = 1
#	else:
#	    result = 0
#	i = i + 2
#    return result



# nice complex, but old...
#def simulateEvent(iPin, level=""):
#    ''' <None> simulateEvent(iPin, level="")
#    simulateEvent simulate an interaktive Event on a Input.
#    ... method in constuction ...
#    '''
#    import java
#
#    iPinClass = iPin.getClass()
#
#    if (not level):
#	try:
#	    if (iPinClass.getMethod('mousePressed', [java.awt.event.MouseEvent])):
#		m = java.awt.event.MouseEvent(java.awt.Button(), java.awt.event.MouseEvent.MOUSE_CLICKED, 0,0,0,0,1,0)
#		iPin.mousePressed(m)
#		return
#	except:
#	    print "jp_stl.simulateEvent error:", sys.exc_type, sys.exc_value
#
#    if(level):
#	try:
#	    if (iPinClass.getMethod('setIndex', [java.lang.Integer.TYPE])):
#		iPin.setIndex(level)
#		return
#	except:
#	    print "jp_stl.simulateEvent error:", sys.exc_type, sys.exc_value
#
#    print "ERROR: Can't simulate event for component ",iPin 


    #old
    #c = iPin.getClass()
    #n = string.split(c.__name__, ".")
    #iPinClass = n[-1]
   
    #if(iPinClass == "Ipin" or iPinClass == "DiodeSwitch"):
	#from java.awt.event import MouseEvent
	#from java.awt import Button
	#m = MouseEvent(Button(), MouseEvent.MOUSE_CLICKED, 0,0,0,0,1,0)
	#iPin.mousePressed(m)
    #elif(iPinClass == "HexSwitch"):
	#iPin.setIndex(level)
	

#def defPin_versuch2(pattern, names):
#    ''' siehe unten :---------('''
#    pins = jp_design_os.get(pattern)
#    print pins
#    i = 0
#    while (i<len(pins)):
#	exec("global "+names[i])
#	exec(names[i]+" = jp_design_os.getByName('"+names[i]+"')")
#	i = i + 1
#    print dir()
#    print globals()

#def defPin_dynamic(pattern, names=""):
#    ''' luppt leider nicht so richtig, global nervt'''
#    design = jp_design_os.getDesign()
#    pins = jp_design_os.get(pattern)
#    i = 0
#    while(i<len(pins)):
#	print "...>"+pins[i].getName()
#	exec(pins[i].getName()+'= pins[i]')
#	exec('global '+pins[i].getName())
#	i = i + 1
    
	
