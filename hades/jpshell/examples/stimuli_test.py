import hades.simulator
from jp_design_os import *
from jp_sim_control import *

class ClockGenerator (hades.models.gates.GenericGate, hades.simulator.Simulatable, hades.simulator.Wakeable):

    def __init__(self, period):
	self.period = period
	self.state = 0
	self.n_cycles = 0

    def elaborate(self, dummy):
	self.state = 0
	self.n_cycles = -16
	simulator = getSimulator()
	time = simulator.getSimTime()
        simulator.scheduleWakeup( self, time+self.period, self )

    def evaluate(self, dummy):
	print "evaluate execute.."
	simulator = getSimulator()
	time = simulator.getSimTime()
	simulator.scheduleWakeup(period)
	state = not state

    def wakeup(self, arg): 
	simulator = getSimulator()
    	self.n_cycles = self.n_cycles + 1 
	#if (divmod(self.n_cycles, 10000)):
	if (self.n_cycles % 1000 == 0):
	    print "wakeup", self.n_cycles
    	time = self.simulator.getSimTime()
    	#schedule( output_0, time+dutycycle*period );
        #schedule( output_1, time+period );
        simulator.scheduleWakeup( self, time+self.period, self );


print "Testbench starts"
design = getDesign()
    
clockGen = ClockGenerator(1.0E-6)
design.addComponent(clockGen)
global clockGen
