import string
import jp_sim_control
from hades.jpshell import JPWrapper
from hades.models import PortStdLogic1164, StdLogic1164
from hades.simulator import Port
from jarray import array

class Delay (JPWrapper):
	
	def __init__(self):
		JPWrapper.__init__(self)
		self.port_A = PortStdLogic1164( self, "A", Port.IN, None )
		self.port_Y = PortStdLogic1164( self, "Y", Port.OUT, None )
		self.ports = array( [self.port_A, self.port_Y], Port)
		self.t_delay = 1.0E-5
	
	def elaborate(self, arg):
		self.simulator = jp_sim_control.getSimulator()

	def evaluate(self, arg):
		signal_Y = self.port_Y.getSignal()
		if signal_Y == None:
			return

		value_A = self.port_A.getValueOrU()
		JPWrapper.scheduleEventAfter( self, signal_Y, self.t_delay, value_A, self.port_Y )
		
	def getSymbolResourceName(self):
		return "/hades/jpshell/module/objects/Delay.sym"
