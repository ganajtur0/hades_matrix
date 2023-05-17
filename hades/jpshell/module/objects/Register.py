import string
import jp_sim_control
from hades.jpshell import JPWrapper
from hades.models import PortStdLogic1164, StdLogic1164
from hades.simulator import Port
from jarray import array

class Register (JPWrapper):

	def __init__(self):
		JPWrapper.__init__(self)
		self.port_C = PortStdLogic1164( self, "C", Port.IN, None )
		self.port_P = PortStdLogic1164( self, "P", Port.IN, None )
		self.port_A = PortStdLogic1164( self, "A", Port.IN, None )
		self.port_dC = PortStdLogic1164( self, "dC", Port.OUT, None )
		self.port_dP = PortStdLogic1164( self, "dP", Port.OUT, None )
		self.port_Y = PortStdLogic1164( self, "Y", Port.OUT, None )
		
		self.ports = array( [self.port_C, self.port_P, self.port_A, self.port_dC, self.port_dP, self.port_Y], Port)
		self.t_delay = 1.0E-5 
		self.register_value = StdLogic1164( StdLogic1164._U )
		#self.pyWriteArgs = ""


	def elaborate(self, arg):
		self.simulator = jp_sim_control.getSimulator()

	
	def evaluate(self, arg):
		if arg.getSource().getSignal() == self.port_A.getSignal():
			return

		#print "huhuhu", self.register_value 
		
		signal_Y = self.port_Y.getSignal()
		signal_dC = self.port_dC.getSignal()
		signal_dP = self.port_dP.getSignal()

		if signal_Y == None:
			return
	
		if arg.getSource().getSignal() == self.port_C.getSignal():
			value_C = self.port_C.getValueOrU()
		
			if value_C.is_1():
				value_A = self.port_A.getValueOrU()
				#print "1 Event on C, value A:",value_A, value_A.getClass()
				self.register_value = value_A.copy() 
				#print "new reg_value", self.register_value
			JPWrapper.scheduleEventAfter( self, signal_dC, self.t_delay, value_C, self.port_dC )

	

		if arg.getSource().getSignal() == self.port_P.getSignal():
			value_P = self.port_P.getValueOrU()
		
			if value_P.is_1():
				#print "1 Event on P, register_value", self.register_value
				JPWrapper.scheduleEventAfter( self, signal_Y, self.t_delay, self.register_value, self.port_Y )
			JPWrapper.scheduleEventAfter( self, signal_dP, self.t_delay, value_P, self.port_dP )

	
	def getSymbolResourceName(self):
		return "/hades/jpshell/module/objects/Register.sym"

