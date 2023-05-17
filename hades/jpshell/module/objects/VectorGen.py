import hades.simulator
import jp_design_os
import jp_sim_control
import jp_stl 
import time
import string
from hades.models import StdLogic1164
from hades.models.gates import GenericGate
from Stimuli import *

class VectorGen (GenericGate, hades.simulator.Wakeable):

    def __init__(self):
		GenericGate.__init__(self)
		self.stimuli_list = []
		self.n_stimul = 0
		self.n_stimuli_executed = 0
		self.test_offset = 0.0
		self.test_result = []
		self.debug = 0

        
    #####
    #    HADES-INTERACTION
    ###
    def elaborate(self, arg):
        if self.debug:
            print "VectorGen elaborate execute..", str(arg)
        self.simulator = jp_sim_control.getSimulator()
        self.simulator.scheduleWakeup( self, 0.0, "APPLY" );
        self.simulator.scheduleWakeup( self, 0.0 + self.test_offset, "TEST" );
        
            
    def evaluate(self, arg):
        if self.debug:
            print "VectorGen evaluate execute..", str(arg)


    def wakeup(self, arg):
        tmp_arg = arg.getArg()
        if self.debug:
            print "VectorGen wakeup execute..", tmp_arg
        sim_time = arg.getTime()
               
        for j in range(len(self.format)):
            pin = self.format[j]
            if (tmp_arg == "APPLY"):
                if (str(pin.getClass()) != "hades.styx.WaveStdLogic1164"):
                    value = self._StdLogicToInt(self.stimuli_list[self.n_stimuli_executed])
                    self.executeStimulus(Stimuli(pin, value, sim_time), self.debug )
                    self.n_stimuli_executed = self.n_stimuli_executed + 1

            elif (tmp_arg == "TEST"):
                if (str(pin.getClass()) == "hades.styx.WaveStdLogic1164"):
                    test = self.stimuli_list[self.n_stimuli_executed]
                    if len(str(test)) == 1:
                        value = self._StdLogicToInt(test)
                        self.test_result.append(self.testProbe(pin, StdLogic1164(value), sim_time, self.debug))
                    else:
                        logic_value = self._BooleanToInt(sim_time, test)
                        self.test_result.append(self.testProbe(pin, logic_value, sim_time, self.debug))
                    
                    self.n_stimuli_executed = self.n_stimuli_executed + 1
                else:
                    # todo: little bug inside
                    if self.n_stimuli_executed >= self.n_stimuli:
                        tmp_arg = "NOTEST"

        if self.debug:
            print "n_stimuli_executed=", self.n_stimuli_executed, "of", self.n_stimuli
            print "tmp_arg:", tmp_arg
            
        if (self.n_stimuli_executed < self.n_stimuli):
            if (tmp_arg == "APPLY"):
                if (self.n_stimuli - self.n_stimuli_executed) >= len(self.format):
                    self.simulator.scheduleWakeup( self, sim_time+self.test_offset, "APPLY" )
            elif (tmp_arg == "TEST"):
                self.simulator.scheduleWakeup( self, sim_time+self.test_offset, "TEST" )
        else:
            if self.debug:
                print "VectorGen end, clear stimuli"
                print "#Test true:", self.test_result.count(1)
            self.n_stimuli_executed = 0

    def start(self):
        design = jp_design_os.getDesign()
        design.addComponent(self, "VectorGen")
		
    def clearDesign(self):
		design = jp_design_os.getDesign()
		design.deleteComponent("VectorGen")

    def setDebug(self, debug):
        self.debug = debug

        
    def getResult(self):
        return self.test_result


    def getTiming(self):
        return self.timing


    def defTiming(self, start, end):
        self.test_offset = end
        self.simtime = start


    def defFormat(self, format):
        self.format=format


    def getFormat(self):
        return self.format


    def executeStimulus(self, stimulus, debug=0):
        pin = stimulus.getPin() 
        value = StdLogic1164(stimulus.getValue()) 
        time = stimulus.getTime()
        pin.setValueAtTime(value, time)
        if debug:
            print "execStimulus: ", pin, value, time


    def defStimuli(self, stimuli_list, debug=0):
        self.stimuli_list = stimuli_list
        self.n_stimuli = len(self.stimuli_list)
        

    def testProbe(self, probe, state, time, debug=0):
        tmp_sim_time = self.simulator.getSimTime()
        probeValue = StdLogic1164(probe.getValue(time))
        
        if ( probeValue == state):
            result = 1
            if debug:
                _result="true"
        else:
            result = 0
            if debug:
                _result="false"
        if debug:
            print "testProbe: ", probe.getName(), "v=",probeValue, "?=",state, time, tmp_sim_time, "->", _result, "\n"
        return result

    
    def _StdLogicToInt(self, value):
        if (value == "U"):
            return 0
        elif (value == "X"):
            return 1
        elif (value == 0):
            return 2
        elif (value == 1):
            return 3


    def _BooleanToInt(self, simtime, stmt, debug=0):
        op = string.upper(str(stmt[0]))
        result = StdLogic1164(stmt[1].getValue(simtime))
        if debug:
            print "t:", simtime
            print "op:", op
            print "arg1:", result

        if op == "NOT":
            result = StdLogic1164.not(result)
            if debug:
                print " ..NOT result:", result
        else:
            for probe in stmt[2:]:
                tmp = StdLogic1164(probe.getValue(simtime))
                if debug:
                    print "tmp:", tmp

                if op == "AND":
                       result = StdLogic1164.and(result, tmp)
                       if debug:
                           print " ..AND result:", result
                elif op == "OR":
                       result = StdLogic1164.or(result, tmp)
                       if debug:
                           print "->OR result:", result
        return result


    def __str__(self):
        return "VectorGen: #Stimuli="+str(len(self.stimuli_list))



        
