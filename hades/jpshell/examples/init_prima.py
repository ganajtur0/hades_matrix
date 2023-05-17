from jp_design_os import *
#
# default init script for the PRIMA processor visualization
#


def info():
	print "show_traces()   hide_traces()"
	print "show_waves()    hide_waves()" 
	print ""
	print "one_clock()"
	print "one_instruction()"
	print "show_control_signals( 1/0 )"
	print "hide_control_signals()"
	print "print_registers()"
	print "print_memory( address )"
	print "dump_memory()"
	return



_tracesSignalNames = [ \
  'nreset', 'clock', \
  'PC', 'AR', 'BR', 'AKKU', \
  'cycle1_fetch', 'cycle2_address', 'cycle3_execute', \
  'PC.enable', 'AR.enable', 'BR.enable', 'AKKU.enable', \
  'RAMADDR', 'RAM.DIN', 'RAM.DOUT', 'RAM.noe', 'RAM.write_enable', \
  'PC.IN', 'PC+1', 'pcmux.s', 'adrmux.s', \
  'ALU.B', 'ALU.OPCODE', 'ALUOUT', 'ALU.overflow' \
]



_controlSignalNames = [ \
  'nreset', 'clock', 'cycle1_fetch', 'cycle2_address', 'cycle3_execute', \
  'PC.enable', 'AR.enable', 'BR.enable', 'AKKU.enable', \
  'RAM.noe', 'RAM.write_enable', \
  'pcmux.s', 'adrmux.s', 'ALU.OPCODE', 'ALU.overflow' \
]


_registerNames = [ 'PC', 'AR', 'BR', 'AKKU' ]



#
# functions start here
#


def show_traces():
	print 'show_traces...'
	design = getDesign()
	for i in range( len( _tracesSignalNames )):
		signal = design.getSignal( _tracesSignalNames[i] )
		if (signal != None):
			print signal
			editor.addProbeToSignal( _tracesSignalNames[i] )
	print 'show_traces ok.'
	return 0




def hide_traces():
	print 'hide_traces...'
	design = getDesign()
	editor.removeProbesFromAllSignals()
	print 'hide_traces ok.'
	return 0




def show_control_signals( flag ):
#	print 'show_control_signals' + flag
	design = getDesign()
	for i in range( len( _controlSignalNames )):
		signal = design.getSignal( _controlSignalNames[i] )
		if (signal != None):
			print signal
			signal.showInternalWireSegments( flag )
	editor.doFullRedraw()
	return 0


def hide_control_signals():
	show_control_signals( 0 )
	return None



def one_clock():	
	print 'one_clock NOT YET'
	return -1


def one_instruction():
	print 'one_instruction NOT YET'
	return -1


def print_registers():
	design = getDesign()
	for i in range( len( _registerNames )):
		name = _registerNames[i]
		print "%-10s %5d" % ( name , design.getComponent( name ).getValue())
	return 0


def print_memory( address ):
	memory = getDesign().getComponent( "RAM" )
	if (memory == None):
		print "-E- internal: RAM not found!"
		return -1

	print memory.getDataAt( address )
	return 0



def dump_memory():
	memory = getDesign().getComponent( "RAM" )
	if (memory == None):
		print "-E- internal: RAM not found!"
		return -1

	#
	# PRIMA's memory has 256 words of 8 bit each, 
	# print as 16 lines of address and 16 data words
	#
	for i in range( 0, 16 ):
		line = "%4d  " % (i*16)
		#	print line
		for j in range( 0, 16 ):
			value = memory.getDataAt( 16*i + j )
			line = "%s %4d" % (line, value)
			if j == 7:
				line = "%s%s" % (line, '    ')
		print line	
	return 



def show_waves():
	editor = getEditor()
	editor.doShowWaves()
	return


def hide_waves():
	editor = getEditor()
	waveformViewer = editor.getWaveformViewer()
	if (waveformViewer == None):
		 return -1
	waveformViewer.setVisible( 0 )
	return


def waves_zoom_fit():
	editor = getEditor()
	waveformViewer = editor.getWaveformViewer()
	if (waveformViewer == None):
		 return -1
	waveformViewer.waveCanvas.zoomF()
	return


def waves_zoom_end():
	editor = getEditor()
	waveformViewer = editor.getWaveformViewer()
	if (waveformViewer == None):
		 return -1
	waveformViewer.doZoomFit()
	return
	




# end of init-prima.py
