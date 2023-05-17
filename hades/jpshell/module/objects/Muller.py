import string
#import java
#import java.io
import jp_sim_control
#import hades
from hades.jpshell import JPWrapper
from hades.models import PortStdLogic1164, StdLogic1164
from hades.simulator import Port
from jarray import array

class Muller (JPWrapper):
    '''
    Muller-C-Gate
    AB|Y
    00|0
    10|old value
    01|old value
    11|1 
    '''
    def __init__(self):
		JPWrapper.__init__(self)
		self.debug = 0
		
		self.port_Y = PortStdLogic1164( self, "Y", Port.OUT, None )
		self.port_A = PortStdLogic1164( self, "A", Port.IN, None )
		self.port_B = PortStdLogic1164( self, "B", Port.IN, None )
		self.ports = array( [self.port_A, self.port_B, self.port_Y], Port )

		self.next_Y = StdLogic1164( StdLogic1164._U )
		self.old_value = StdLogic1164( StdLogic1164._U )
		self.t_delay = 5.0E-9 
		self.symbol_type = "horizontal"
		self.pyWriteArgs = self.symbol_type

		if self.debug:
			print self

    def elaborate(self, arg):
        if self.debug:
            print "Muller.elaborate("+str(arg)+")"
            
        self.simulator = jp_sim_control.getSimulator()


    def evaluate(self, arg):
        if self.debug:
            print "Muller.evaluate("+str(arg)+")"

        signal_Y = self.port_Y.getSignal()

        if signal_Y == None:
            return

        value_A = self.port_A.getValueOrU()
        value_B = self.port_B.getValueOrU()
        if self.debug:
            print "value_A, value_B",value_A, value_B
       
        if value_A == value_B:
            self.next_Y.setToAnd( value_A, value_B )
            self.old_value = self.next_Y
        else:
            self.next_Y=self.old_value
        if self.debug:
            print "self.next_Y, self.old_value", self.next_Y, self.old_value
            
        JPWrapper.scheduleEventAfter( self, signal_Y, self.t_delay, self.next_Y, self.port_Y ) 


    def getSymbolResourceName(self):
        if string.upper(self.symbol_type) == "SOUTH":
            return "/hades/jpshell/module/objects/MullerC_V_S.sym"
        elif string.upper(self.symbol_type) == "NORTH":
            return "/hades/jpshell/module/objects/MullerC_V_N.sym"
        else:
            return "/hades/jpshell/module/objects/MullerC_H.sym"


    def setSymbolType(self, type):
		self.symbol_type = type
		self.pyWriteArgs = self.symbol_type

    def setArgs(self, s):
		#print "huhuhu mullier", s
		self.symbol_type = s 
		self.pyWriteArgs = s
        
    def setDebug(self, debug):
        self.debug=debug

    def __str__(self):
        if self.debug:
            return "Muller: \n"+\
                   str(self.port_Y)+",\n"+\
                   str(self.port_A)+",\n"+\
                   str(self.port_B)+",\n"+\
                   str(self.next_Y)+",\n"+\
                   str(self.t_delay)
        return "Muller: "+ self.getFullName()

