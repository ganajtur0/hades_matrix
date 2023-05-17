# makefile for Hades, central top level makefile
# 
# (c) 1997 - 1999 
#          N.Hendrich, University of Hamburg, Computer Science
#          hendrich@informatik.uni-hamburg.de
#
# 15.10.99 added hades.models.mips and mcore, pic cleanups
# 19.02.99 hades.utils.vhdl 
# 21.10.98 added PIC stuff
# 04.08.98 cleanups, RTLIB stuff
# 01.03.98 Linux version
# 02.04.97 centralized all makefiles into this one
# 25.03.97 first try
#
# --------------------------------------------------------------------------
# Tools section
# --------------------------------------------------------------------------
#JAVAC = javac -deprecation
#JAVAC = jikes +P       # "pedantic"
# JAVAC = jikes +Z0 -Xstdout
# JAVAC = jikes  -O
JAVAC = jikes +Pno-shadow -Xstdout -O
# JAVACC = java COM.sun.labs.javacc.Main
JAVACC = ~/bin/javacc
#
JAR = jar
JAVADOC = javadoc -package
JAVAKEY = javakey
JAVAOPT = -g -d $(BASEDIR)
#JAVAOPT = -O -d $(BASEDIR)

# --------------------------------------------------------------------------
# pathnames section
# --------------------------------------------------------------------------

# where to put the HADES Web-pages and archives
WWWSERVER = tech18
WWWDIR = /export/www/htdocs/applets/hades
WWWARDIR = /export/www/htdocs/applets/hades/archive
WWWDOCDIR =  /export/www/htdocs/lehre/t3Prak

WEB_TEMP = /tmp/jetty/hades

# where to install the HADES classes, examples, and run scripts
INSTALLDIR = /opt/hades

# base directories of the source trees
# BASEDIR  = /home/tams_1/hendrich/java
BASEDIR = /home/hendrich/java

HADESDIR = $(BASEDIR)/hades
CLASSDIR = $(BASEDIR)/hades
ARCHIVEDIR = $(BASEDIR)/hades/archive
JAVAFIGARCHIVEDIR = $(BASEDIR)/jfig/archive

# HADES internal directories, relative to HADESDIR
SIMDIR = $(HADESDIR)/simulator
SIMDIROPT = $(HADESDIR)/simulator
SIGNALDIR = $(HADESDIR)/signals
MODELDIR = $(HADESDIR)/models
IODIR = $(HADESDIR)/models/io
STIMULIDIR = $(HADESDIR)/models/stimuli
GATEDIR = $(HADESDIR)/models/gates
GATEDELAYDIR = $(HADESDIR)/models/gates
CGATEDIR = $(HADESDIR)/models/complexgates
GATTERDIR = $(HADESDIR)/models/gatter
FLIPFLOPDIR = $(HADESDIR)/models/flipflops
TTLDIR = $(HADESDIR)/models/ttl74
MEMORYDIR = $(HADESDIR)/models/memory
RTLDIR = $(HADESDIR)/models/rtl
REGDIR = $(HADESDIR)/models/register
FSMDIR = $(HADESDIR)/models/fsm
MICROJAVADIR = $(HADESDIR)/models/microjava
#FSMDIR = $(HADESDIR)/fsm
DCF77DIR = $(HADESDIR)/models/dcf77
PICDIR = $(HADESDIR)/models/pic
MIPSDIR = $(HADESDIR)/models/mips
MCOREDIR = $(HADESDIR)/models/mcore
SPECIALDIR = $(HADESDIR)/models/special
METADIR = $(HADESDIR)/models/meta
I8048DIR = $(HADESDIR)/models/i8048
IMAGINGDIR = $(HADESDIR)/models/imaging
STRINGDIR = $(HADESDIR)/models/string
RUGEDIR = $(HADESDIR)/models/ruge
HAGENDIR = $(HADESDIR)/models/hagen
MCS4DIR  = $(HADESDIR)/models/mcs4
SWITCHEDDIR  = $(HADESDIR)/models/switched
DSPDIR = $(HADESDIR)/models/dsp

RTLIBDIR = $(HADESDIR)/models/rtlib
RTLIB_ARITH_DIR    = $(HADESDIR)/models/rtlib/arith
RTLIB_COMPARE_DIR  = $(HADESDIR)/models/rtlib/compare
RTLIB_LOGIC_DIR    = $(HADESDIR)/models/rtlib/logic
RTLIB_MEMORY_DIR   = $(HADESDIR)/models/rtlib/memory
RTLIB_MUXES_DIR    = $(HADESDIR)/models/rtlib/muxes
RTLIB_IO_DIR       = $(HADESDIR)/models/rtlib/io
RTLIB_REGISTER_DIR = $(HADESDIR)/models/rtlib/register

SYMBOLDIR = $(HADESDIR)/symbols
GUIDIR = $(HADESDIR)/gui
MANAGERDIR = $(HADESDIR)/manager
WAVESDIR = $(HADESDIR)/waves
STYXDIR = $(HADESDIR)/styx
UTILSDIR = $(HADESDIR)/utils
VHDLDIR  = $(HADESDIR)/utils/vhdl
JPSHELLDIR = $(HADESDIR)/jpshell

# --------------------------------------------------------------------------
# rules section
# --------------------------------------------------------------------------
.SUFFIXES:
.SUFFIXES: .java .class

%.class: %.java
	$(JAVAC) $(JAVAOPT) $*.java

$(SIMDIROPT)/%.class:	$(SIMDIROPT)/%.java
	$(JAVAC) $(JAVAOPTO) $(SIMDIROPT)/$*.java

$(SIMDIR)/%.class:	$(SIMDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(SIMDIR)/$*.java

$(SIGNALDIR)/%.class:	$(SIGNALDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(SIGNALDIR)/$*.java

$(MODELDIR)/%.class:	$(MODELDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(MODELDIR)/$*.java

$(GATEDIR)/%.class:	$(GATEDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(GATEDIR)/$*.java

$(GATEDELAYDIR)/%.class:	$(GATEDELAYDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(GATEDELAYDIR)/$*.java

$(GATTERIR)/%.class:	$(GATTERIR)/%.java
	$(JAVAC) $(JAVAOPT) $(GATTERDIR)/$*.java

$(CGATEDIR)/%.class:	$(CGATEDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(CGATEDIR)/$*.java

$(IODIR)/%.class:	$(IODIR)/%.java
	$(JAVAC) $(JAVAOPT) $(IODIR)/$*.java

$(FLIPFLOPDIR)/%.class:	$(FLIPFLOPDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(FLIPFLOPDIR)/$*.java

$(TTLDIR)/%.class:	$(TTLDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(TTLDIR)/$*.java

$(FSMDIR)/%.class:	$(FSMDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(FSMDIR)/$*.java

$(MICROJAVADIR)/%.class:	$(MICROJAVADIR)/%.java
	$(JAVAC) $(JAVAOPT) $(MICROJAVADIR)/$*.java

$(MEMORYDIR)/%.class:	$(MEMORYDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(MEMORYDIR)/$*.java

$(RTLDIR)/%.class:	$(RTLDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(RTLDIR)/$*.java

$(RTLIB_ARITH_DIR)/%.class:	$(RTLIB_ARITH_DIR)/%.java
	$(JAVAC) $(JAVAOPT) $(RTLIB_ARITH_DIR)/$*.java

$(RTLIB_COMPARE_DIR)/%.class:	$(RTLIB_COMPARE_DIR)/%.java
	$(JAVAC) $(JAVAOPT) $(RTLIB_COMPARE_DIR)/$*.java

$(RTLIB_LOGIC_DIR)/%.class:	$(RTLIB_LOGIC_DIR)/%.java
	$(JAVAC) $(JAVAOPT) $(RTLIB_LOGIC_DIR)/$*.java

$(RTLIB_MEMORY_DIR)/%.class:	$(RTLIB_MEMORY_DIR)/%.java
	$(JAVAC) $(JAVAOPT) $(RTLIB_MEMORY_DIR)/$*.java

$(RTLIB_MUXES_DIR)/%.class:	$(RTLIB_MUXES_DIR)/%.java
	$(JAVAC) $(JAVAOPT) $(RTLIB_MUXES_DIR)/$*.java

$(RTLIB_IO_DIR)/%.class:	$(RTLIB_IO_DIR)/%.java
	$(JAVAC) $(JAVAOPT) $(RTLIB_IO_DIR)/$*.java

$(RTLIB_REGISTER_DIR)/%.class:	$(RTLIB_REGISTER_DIR)/%.java
	$(JAVAC) $(JAVAOPT) $(RTLIB_REGISTER_DIR)/$*.java

$(REGDIR)/%.class:	$(REGDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(REGDIR)/$*.java

$(SPECIALDIR)/%.class:	$(SPECIALDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(SPECIALDIR)/$*.java

$(STIMULIDIR)/%.class:	$(STIMULIDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(STIMULIDIR)/$*.java

$(STIMULIDIR)/%.java:	$(STIMULIDIR)/%.jj
	$(JAVACC) -OUTPUT_DIRECTORY="models/stimuli" $(STIMULIDIR)/$*.jj

$(STIMULIDIR)/%.class:	$(STIMULIDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(STIMULIDIR)/$*.java


$(DCF77DIR)/%.class:	$(DCF77DIR)/%.java
	$(JAVAC) $(JAVAOPT) $(DCF77DIR)/$*.java

$(PICDIR)/%.class:	$(PICDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(PICDIR)/$*.java

$(MIPSDIR)/%.class:	$(MIPSDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(MIPSDIR)/$*.java

$(MCOREDIR)/%.class:	$(MCOREDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(MCOREDIR)/$*.java

$(METADIR)/%.class:	$(METADIR)/%.java
	$(JAVAC) $(JAVAOPT) $(METADIR)/$*.java

$(I80480DIR)/%.class:	$(I80480DIR)/%.java
	$(JAVAC) $(JAVAOPT) $(I80480DIR)/$*.java

$(IMAGINGDIR)/%.class:	$(IMAGINGDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(IMAGINGDIR)/$*.java

$(STRINGDIR)/%.class:	$(STRINGDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(STRINGDIR)/$*.java

$(RUGEDIR)/%.class:	$(RUGEDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(RUGEDIR)/$*.java

$(MCS4DIR)/%.class:	$(MCS4DIR)/%.java
	$(JAVAC) $(JAVAOPT) $(MCS4DIR)/$*.java

$(HAGENDIR)/%.class:	$(HAGENDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(HAGENDIR)/$*.java

$(RTLIBDIR)/%.class:	$(RTLIBDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(RTLIBDIR)/$*.java

$(SWITCHEDDIR)/%.class:	$(SWITCHEDDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(SWITCHEDDIR)/$*.java

$(DSPDIR)/parser/%.java:	$(DSPDIR)/parser/%.jj
	$(JAVACC) -OUTPUT_DIRECTORY="models/dsp/parser" $(DSPDIR)/parser/$*.jj

$(DSPDIR)/%.class:	$(DSPDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(DSPDIR)/$*.java

$(SYMBOLDIR)/%.class:	$(SYMBOLDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(SYMBOLDIR)/$*.java

$(GUIDIR)/%.class:	$(GUIDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(GUIDIR)/$*.java

$(MANAGERDIR)/%.class:	$(MANAGERDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(MANAGERDIR)/$*.java

$(WAVESDIR)/%.class:	$(WAVESDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(WAVESDIR)/$*.java

$(STYXDIR)/%.class:	$(STYXDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(STYXDIR)/$*.java

$(UTILSDIR)/%.class:	$(UTILSDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(UTILSDIR)/$*.java

$(VHDLDIR)/%.class:	$(VHDLDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(VHDLDIR)/$*.java

$(JPSHELLDIR)/%.class:	$(JPSHELLDIR)/%.java
	$(JAVAC) $(JAVAOPT) $(JPSHELLDIR)/$*.java





# --------------------------------------------------------------------------
# targets section
# --------------------------------------------------------------------------
OBJ =\
	$(GUIDIR)/Console.class 


SIMOBJ =\
	$(SIMDIROPT)/Simulatable.class \
	$(SIMDIROPT)/Wakeable.class \
	$(SIMDIROPT)/Assignable.class \
	$(SIMDIROPT)/Port.class \
	$(SIGNALDIR)/Signal.class \
	\
	$(MODELDIR)/PortStdLogic1164.class \
	$(SIGNALDIR)/SignalStdLogic1164.class \
	\
	$(SIMDIR)/GenericSwitch.class \
	$(SIGNALDIR)/SignalStdLogicSwitched.class \
	\
	$(SIGNALDIR)/SignalStdLogicVector.class \
	$(MODELDIR)/PortStdLogicVector.class \
	\
	$(SIGNALDIR)/SignalInteger.class \
	$(SIGNALDIR)/PortInteger.class \
	$(SIGNALDIR)/SignalDouble.class \
	$(SIGNALDIR)/PortDouble.class \
	\
	$(SIMDIROPT)/SimObject.class \
	$(SIMDIROPT)/SimEvent.class \
	$(SIMDIROPT)/SimEvent1164.class \
	$(SIMDIROPT)/WakeupEvent.class \
	$(SIMDIR)/SimulatorInterruptEvent.class \
	$(SIMDIR)/SignalEvent.class \
	$(SIMDIROPT)/EventList.class \
	$(SIMDIROPT)/SimEventRecycler.class \
	$(SIMDIROPT)/SimKernel.class \
	$(SIMDIROPT)/RealTimeSimKernel.class \
	$(SIMDIROPT)/BatchModeSimKernel.class \
	$(SIMDIROPT)/InteractiveSimKernel.class \
	$(SIMDIROPT)/VhdlSimKernel.class \
	$(SIMDIROPT)/VhdlBatchSimKernel.class \
	$(SIMDIROPT)/CommandQueue.class \
	$(SIMDIROPT)/SimulatorCommand.class \
	$(SIMDIROPT)/SimulatorScheduleCommand.class \
	$(SIMDIROPT)/SimulatorSingleStepCommand.class \
	$(SIMDIROPT)/DeleteAllEventsFromSourceCommand.class \
	$(SIMDIR)/SimDebugPanel.class 


SYMBOLOBJ =\
	$(SYMBOLDIR)/Symbol.class \
	$(SYMBOLDIR)/SymbolManager.class \
	$(SYMBOLDIR)/PortSymbol.class \
	$(SYMBOLDIR)/TinyPortSymbol.class \
	$(SYMBOLDIR)/BusPortSymbol.class \
	$(SYMBOLDIR)/TextSource.class \
	$(SYMBOLDIR)/ColorSource.class \
	$(SYMBOLDIR)/Label.class \
	$(SYMBOLDIR)/PortLabel.class \
	$(SYMBOLDIR)/FatLabel.class \
	$(SYMBOLDIR)/InstanceLabel.class \
	$(SYMBOLDIR)/FatInstanceLabel.class \
	$(SYMBOLDIR)/PersistentInstanceLabel.class \
	$(SYMBOLDIR)/ClassLabel.class \
	$(SYMBOLDIR)/BindkeyLabel.class \
	$(SYMBOLDIR)/Polyline.class \
	$(SYMBOLDIR)/Circle.class \
	$(SYMBOLDIR)/ColoredPolyline.class \
	$(SYMBOLDIR)/ColoredCircle.class \
	$(SYMBOLDIR)/Arc.class \
	$(SYMBOLDIR)/Rectangle.class \
	$(SYMBOLDIR)/ImageObject.class \
	$(SYMBOLDIR)/BboxRectangle.class \
	$(SYMBOLDIR)/WireSegment.class \
	$(SYMBOLDIR)/SolderDot.class \
	$(SYMBOLDIR)/ProbeSymbol.class \
	$(SYMBOLDIR)/ClockArm.class \
	$(SYMBOLDIR)/FigWrapper.class \
	$(SYMBOLDIR)/Color_DIN_IEC_62.class \
	$(SYMBOLDIR)/ColoredRectangle.class \
	$(SYMBOLDIR)/ColoredValueLabel.class \
	$(SYMBOLDIR)/HorizontalBarGraph.class \
	$(SYMBOLDIR)/HighlightRectangle.class \
	$(SYMBOLDIR)/HighlightWireSegment.class \
	$(SYMBOLDIR)/ErrorMarker.class \


MODELOBJ =\
	$(MODELDIR)/InputConnector.class \
	$(MODELDIR)/OutputConnector.class \
	$(MODELDIR)/Design.class \
	$(MODELDIR)/StdLogic1164.class \
	$(MODELDIR)/Const1164.class \
	$(MODELDIR)/StdLogicVector.class \
	$(MODELDIR)/FigObject.class \
	$(IODIR)/Vcc.class \
	$(IODIR)/Gnd.class \
	$(IODIR)/Pullup.class \
	$(IODIR)/Constant.class \
	$(IODIR)/ConstantU.class \
	$(IODIR)/ConstantX.class \
	$(IODIR)/Constant0.class \
	$(IODIR)/Constant1.class \
	$(IODIR)/ConstantZ.class \
	$(IODIR)/ConstantH.class \
	$(IODIR)/ConstantL.class \
	$(IODIR)/ConstantW.class \
	$(IODIR)/LED.class \
	$(IODIR)/Opin.class \
	$(IODIR)/OpinVertical.class \
	$(IODIR)/OpinLarge.class \
	$(IODIR)/OpinWithLabel.class \
	$(IODIR)/Ipin.class \
	$(IODIR)/IpinVertical.class \
	$(IODIR)/IpinLarge.class \
	$(IODIR)/IpinStdLogic1164.class \
	$(IODIR)/PulseSwitch.class \
	$(IODIR)/DiodeSwitch.class \
	$(IODIR)/SevenSegment.class \
	$(IODIR)/SevenSegmentMultiplexed.class \
	$(IODIR)/HexDisplay.class \
	$(IODIR)/HexDisplaySmall.class \
	$(IODIR)/AsciiDisplay.class \
	$(IODIR)/Iso8859Display.class \
	$(IODIR)/HexSwitch.class \
	$(IODIR)/ClockGen.class \
	$(IODIR)/ClockGen2.class \
	$(IODIR)/ClockGenWithAutoStop.class \
	$(IODIR)/PowerOnReset.class \
	$(IODIR)/BitReg6.class \
	$(IODIR)/Swatch.class \
	$(IODIR)/RandomBitGenerator.class \
	$(IODIR)/RomDiode.class \
	$(IODIR)/GalFuse.class \
	\
	$(IODIR)/Stimulus.class \
	$(IODIR)/RemoteOpin.class \
	$(IODIR)/RemoteOpin8.class \
	$(IODIR)/RemoteIpin.class \
	$(IODIR)/RemoteIpin8.class \

GATES =\
	$(GATEDIR)/GenericGate.class \
	$(GATEDIR)/Buffer.class \
	$(GATEDIR)/BufferSmall.class \
	$(GATEDIR)/And2.class \
	$(GATEDIR)/And3.class \
	$(GATEDIR)/And4.class \
	$(GATEDIR)/And6.class \
	$(GATEDIR)/And4Neg2.class \
	$(GATEDIR)/And2Vertical.class \
	$(GATEDIR)/And3Vertical.class \
	$(GATEDIR)/Demux14.class \
	$(GATEDIR)/Inv.class \
	$(GATEDIR)/InvSmall.class \
	$(GATEDIR)/InvSmallVertical.class \
	$(GATEDIR)/InvOpenCollector.class \
	$(GATEDIR)/Or2.class \
	$(GATEDIR)/Or3.class \
	$(GATEDIR)/Or4.class \
	$(GATEDIR)/Or6.class \
	$(GATEDIR)/Mux21.class \
	$(GATEDIR)/Mux41.class \
	$(GATEDIR)/Nand2.class \
	$(GATEDIR)/Nand3.class \
	$(GATEDIR)/Nand4.class \
	$(GATEDIR)/Nor2.class \
	$(GATEDIR)/Nor3.class \
	$(GATEDIR)/Nor4.class \
	$(GATEDIR)/Tri.class \
	$(GATEDIR)/WeakBuffer.class \
	$(GATEDIR)/WeakInverter.class \
	$(GATEDIR)/BitlineBuffer.class \
	$(GATEDIR)/Xor2.class \
	$(GATEDIR)/Xor2Vertical.class \
	$(GATEDIR)/Xnor2.class \
	$(GATEDIR)/NandMetastable2.class \
	$(GATEDIR)/NandMetastable3.class \
	\
	$(GATEDIR)/And4G.class \
#$(GATEDIR)/Nand4G.class \
#$(GATEDIR)/Nor4G.class \
#$(GATEDIR)/Or4G.class \


GATESWITHDINSYMBOLS =\
	$(GATTERDIR)/And2.class \
	$(GATTERDIR)/And3.class \
	$(GATTERDIR)/And4.class \
	$(GATTERDIR)/And4Neg2.class \
	$(GATTERDIR)/Demux14.class \
	$(GATTERDIR)/Buffer.class \
	$(GATTERDIR)/Inv.class \
	$(GATTERDIR)/InvVertical.class \
	$(GATTERDIR)/Mux21.class \
	$(GATTERDIR)/Mux41.class \
	$(GATTERDIR)/Mux41DIN.class \
	$(GATTERDIR)/Nand2.class \
	$(GATTERDIR)/Nand3.class \
	$(GATTERDIR)/Nand4.class \
	$(GATTERDIR)/Nor2.class \
	$(GATTERDIR)/Nor3.class \
	$(GATTERDIR)/Nor4.class \
	$(GATTERDIR)/Or2.class \
	$(GATTERDIR)/Or3.class \
	$(GATTERDIR)/Or4.class \
	$(GATTERDIR)/Or6.class \
	$(GATTERDIR)/Tri.class \
	$(GATTERDIR)/Xor2.class \
	$(GATTERDIR)/Xnor2.class \

DELAYNODES =\
	$(GATEDELAYDIR)/DelayNode.class \
	$(GATEDELAYDIR)/DelayNode_LR.class \
	$(GATEDELAYDIR)/DelayNode_TB.class \

COMPLEXGATES =\
	$(CGATEDIR)/GenericCGate.class \
	$(CGATEDIR)/AOI21.class \
	$(CGATEDIR)/AOI22.class \
	$(CGATEDIR)/AOI31.class \
	$(CGATEDIR)/AOI32.class \
	$(CGATEDIR)/AOI33.class \
	$(CGATEDIR)/OAI21.class \
	$(CGATEDIR)/OAI22.class \
	$(CGATEDIR)/OAI31.class \
	$(CGATEDIR)/OAI32.class \
	$(CGATEDIR)/OAI33.class 

FLIPFLOPS = \
	$(FLIPFLOPDIR)/GenericFlipflop.class \
	$(FLIPFLOPDIR)/Dff.class \
	$(FLIPFLOPDIR)/DffMetastable.class \
	$(FLIPFLOPDIR)/Dffr.class \
	$(FLIPFLOPDIR)/DffrMetastable.class \
	$(FLIPFLOPDIR)/Dffe.class \
	$(FLIPFLOPDIR)/Dffre.class \
	$(FLIPFLOPDIR)/Dffrs.class \
	$(FLIPFLOPDIR)/Jkff.class \
	$(FLIPFLOPDIR)/JkffMetastable.class \
	$(FLIPFLOPDIR)/Latch.class \
	$(FLIPFLOPDIR)/LatchMetastable.class \
	$(FLIPFLOPDIR)/Latchr.class \
	$(FLIPFLOPDIR)/DffRtlib.class \
	$(FLIPFLOPDIR)/DffreRtlib.class \
	$(FLIPFLOPDIR)/Srff.class \
	$(FLIPFLOPDIR)/SrffRtlib.class \

TTLS = \
	$(TTLDIR)/SN7449.class       \
	$(TTLDIR)/SN7449_pinout.class \
	$(TTLDIR)/SN7400.class \
	$(TTLDIR)/SN7400_pinout.class \
	$(TTLDIR)/SN7405.class \
	$(TTLDIR)/SN7405_pinout.class \
	$(TTLDIR)/SN7408_pinout.class \
	$(TTLDIR)/SN7432_pinout.class \
	$(TTLDIR)/SN7486_pinout.class \
	$(TTLDIR)/SN74189.class \
	$(TTLDIR)/SN74219.class 

MEMORY = \
	$(MEMORYDIR)/MemoryListener.class \
	$(MEMORYDIR)/Memory.class \
	$(MEMORYDIR)/InstructionDecoder.class \

RTLS = \
	$(RTLDIR)/ROM_1Kx8.class \
	$(RTLDIR)/ROM_256x8.class \
	$(RTLDIR)/ROM_64x8.class \
	$(RTLDIR)/ROM_8Kx8.class \
	$(RTLDIR)/ROM_64Kx8.class \
	$(RTLDIR)/RAM_256x8.class \
	$(RTLDIR)/IDT6116.class \
	$(RTLDIR)/IDT6164.class \

REGS = \
	$(REGDIR)/Register.class \
	$(REGDIR)/RegisterR.class \
	$(REGDIR)/RegisterRE.class \
	$(REGDIR)/ShiftRegister.class \
	$(REGDIR)/LFSRGenerator.class \
	$(REGDIR)/LFSRGenerator8.class \
	$(REGDIR)/LFSRGenerator16.class \
	$(REGDIR)/LFSRGenerator24.class \
	$(REGDIR)/LFSRGenerator32.class \
	$(REGDIR)/LFSRAnalyzer.class \
	$(REGDIR)/LFSRAnalyzer8.class \
	$(REGDIR)/LFSRAnalyzer16.class \
	$(REGDIR)/LFSRAnalyzer24.class \
	$(REGDIR)/LFSRAnalyzer32.class \
	$(REGDIR)/CounterRE.class \
	$(REGDIR)/CounterRE8.class \
	$(REGDIR)/CounterRE16.class \

FSMS = \
	$(FSMDIR)/Statuszeile.class \
	$(FSMDIR)/Zustand.class \
	$(FSMDIR)/Signal.class \
	$(FSMDIR)/Transition.class \
	$(FSMDIR)/Kommentar.class \
	$(FSMDIR)/BadExpressionException.class \
	$(FSMDIR)/Parser.class \
	$(FSMDIR)/Tester.class \
	$(FSMDIR)/FSMtester.class \
	$(FSMDIR)/About.class \
	$(FSMDIR)/Panel3D.class \
	$(FSMDIR)/ExportFSM.class \
	$(FSMDIR)/SignalDialog.class \
	$(FSMDIR)/EditCanvas.class \
	$(FSMDIR)/EditFrame.class \
	$(FSMDIR)/NameDialog.class \
	$(FSMDIR)/Simulation.class \
	$(FSMDIR)/FSM.class \
	$(FSMDIR)/FsmRenderer.class \
	$(FSMDIR)/FsmWrapper.class 

SPECIAL = \
	$(SPECIALDIR)/Counter.class \
	$(SPECIALDIR)/ValueTrigger.class \
	$(SPECIALDIR)/EdgeTrigger.class \
	$(SPECIALDIR)/HazardTrigger.class \
	$(SPECIALDIR)/VT52Canvas.class \
	$(SPECIALDIR)/ParallelTerminal.class \
	$(SPECIALDIR)/SerialTerminal.class \
	$(SPECIALDIR)/MidiReceiver.class \
	$(SPECIALDIR)/TextLCDCanvas.class \
	$(SPECIALDIR)/TextLCD.class \
	$(SPECIALDIR)/GraphicsLCDCanvas.class \
	$(SPECIALDIR)/GraphicsLCD.class \
	$(SPECIALDIR)/GraphicsLCDCanvasuniv.class \
	$(SPECIALDIR)/GraphicsLCDnfb.class \

DCF77S = \
	$(DCF77DIR)/Dcf77Sender.class \
	$(DCF77DIR)/Dcf77Clock.class \

PIC16C84	= \
	$(PICDIR)/MemoryView.class \
	$(PICDIR)/ShowDisassemblerCanvas.class \
	$(PICDIR)/MemoryDisassemblerView.class \
	$(PICDIR)/HexMemoryCanvas.class \
	$(PICDIR)/PicAlu.class \
	$(PICDIR)/PicBitReg.class \
	$(PICDIR)/PicByteReg.class \
	$(PICDIR)/PicCalc.class \
	$(PICDIR)/PicCalcADDWF.class \
	$(PICDIR)/PicCalcANDWF.class \
	$(PICDIR)/PicCalcCLR.class \
	$(PICDIR)/PicCalcCOMF.class \
	$(PICDIR)/PicCalcDECF.class \
	$(PICDIR)/PicCalcDECFSZ.class \
	$(PICDIR)/PicCalcINCF.class \
	$(PICDIR)/PicCalcINCFSZ.class \
	$(PICDIR)/PicCalcIORWF.class \
	$(PICDIR)/PicCalcMOVF.class \
	$(PICDIR)/PicCalcMOVWF.class \
	$(PICDIR)/PicCalcNOP.class \
	$(PICDIR)/PicCalcRLF.class \
	$(PICDIR)/PicCalcRRF.class \
	$(PICDIR)/PicCalcSUBWF.class \
	$(PICDIR)/PicCalcSWAPF.class \
	$(PICDIR)/PicCalcXORWF.class \
	$(PICDIR)/PicClocking.class \
	$(PICDIR)/PicDecode.class \
	$(PICDIR)/PicEprom.class \
	$(PICDIR)/PicEeprom.class \
	$(PICDIR)/PicIndfReg.class \
	$(PICDIR)/PicIntConReg.class \
	$(PICDIR)/PicMemory.class \
	$(PICDIR)/PicNoReg.class \
	$(PICDIR)/PicPcReg.class \
	$(PICDIR)/PicPortReg.class \
	$(PICDIR)/PicReg.class \
	$(PICDIR)/PicRegBank.class \
	$(PICDIR)/PicStack.class \
	$(PICDIR)/PicTimerReg.class \
	$(PICDIR)/PicWdt.class \
	$(PICDIR)/PicWordReg.class \
	\
	$(PICDIR)/PicExec.class \
	$(PICDIR)/ShowPic2.class \
	$(PICDIR)/ShowSignals.class \
	$(PICDIR)/SignalElement.class \
	$(PICDIR)/TestPic.class \
	$(PICDIR)/WordButton.class \
	$(PICDIR)/Pic16C84.class \
	$(PICDIR)/PicRegBank16F84.class \
	$(PICDIR)/PicExec16F84.class \
	$(PICDIR)/Pic16F84.class \
	$(PICDIR)/FastPic16F84.class \
	$(PICDIR)/SmartPic16F84.class \
	$(PICDIR)/Pic16C84Debug.class \
	$(PICDIR)/PicDisassembler.class \
	$(PICDIR)/PicAssembler.class \
	\
	$(PICDIR)/TurboPicCore.class \
	$(PICDIR)/TurboPicGUI.class \
	$(PICDIR)/TurboPic16C84.class \
	

MCORE = \
	$(MCOREDIR)/McoreALU.class \
	$(MCOREDIR)/TestMcore.class \
	$(MCOREDIR)/McoreMillionCycles.class \
	$(MCOREDIR)/DcoreDecoder.class \
	$(MCOREDIR)/DcoreDisassemblerOrHexCanvas.class \
	$(MCOREDIR)/DcoreDisassemblerEditorFrame.class \
	$(MCOREDIR)/DcoreRAM.class \
	$(MCOREDIR)/DcoreROM.class \





META = \
	$(METADIR)/ActionButton.class \
	$(METADIR)/AudioPlayer.class \
	$(METADIR)/JythonScriptWrapper.class \
	$(METADIR)/Label.class \
	$(METADIR)/Highlighter.class \
	$(METADIR)/TTS.class \


I8048 = \
	$(I8048DIR)/OpcodeTable.class \
	$(I8048DIR)/I8048.class \
	$(I8048DIR)/I8048GUI.class \

IMAGING = \
	$(IMAGINGDIR)/ImageSignal.class \
	$(IMAGINGDIR)/ImageFileFilter.class \
	$(IMAGINGDIR)/ImageViewer.class \
	$(IMAGINGDIR)/ImageWriter.class \
	$(IMAGINGDIR)/ImageSource.class \
	$(IMAGINGDIR)/SimpleFilter.class \
	$(IMAGINGDIR)/ParametrizedFilter.class \
	\
	$(IMAGINGDIR)/RedFilter.class \
	$(IMAGINGDIR)/GreenFilter.class \
	$(IMAGINGDIR)/BlueFilter.class \
	$(IMAGINGDIR)/GrayFilter.class \
	$(IMAGINGDIR)/OpaqueFilter.class \
	$(IMAGINGDIR)/InvertFilter.class \
	$(IMAGINGDIR)/MirrorXFilter.class \
	$(IMAGINGDIR)/MirrorYFilter.class \
	$(IMAGINGDIR)/PurpleDetectionFilter.class \
	$(IMAGINGDIR)/GammaFilter.class \
	$(IMAGINGDIR)/SaturationFilter.class \
	$(IMAGINGDIR)/GaussFilter.class \
	$(IMAGINGDIR)/DifferenceFilter.class \
	\
	$(IMAGINGDIR)/TwoInputFilter.class \
	$(IMAGINGDIR)/ANDFilter.class \
	$(IMAGINGDIR)/ORFilter.class \
	$(IMAGINGDIR)/MaxFilter.class \
	$(IMAGINGDIR)/MinFilter.class \
	$(IMAGINGDIR)/AddFilter.class \
	$(IMAGINGDIR)/SubFilter.class \
	$(IMAGINGDIR)/AbsSubFilter.class \
	$(IMAGINGDIR)/MultFilter.class \
	$(IMAGINGDIR)/EqualsFilter.class \
	$(IMAGINGDIR)/EqualsWithinFilter.class \
	$(IMAGINGDIR)/S40StripeReductionFilter.class \
	\
	$(IMAGINGDIR)/ResizeFilter.class \
	$(IMAGINGDIR)/RotationFilter.class \
	$(IMAGINGDIR)/ShearFilter.class \
	$(IMAGINGDIR)/AffineTransformationFilter.class \
	$(IMAGINGDIR)/PerspectiveTransformationFilter.class \
	$(IMAGINGDIR)/CropFilter.class \
	\
	$(IMAGINGDIR)/ConvolutionFilter.class \
	$(IMAGINGDIR)/Gauss3Filter.class \
	$(IMAGINGDIR)/Gauss5Filter.class \
	$(IMAGINGDIR)/Smooth5Filter.class \
	$(IMAGINGDIR)/Smooth20Filter.class \
	$(IMAGINGDIR)/Smooth50Filter.class \
	$(IMAGINGDIR)/EdgeXFilter.class \
	$(IMAGINGDIR)/EdgeYFilter.class \
	$(IMAGINGDIR)/EdgeNEFilter.class \
	$(IMAGINGDIR)/EdgeNWFilter.class \
	$(IMAGINGDIR)/SobelXFilter.class \
	$(IMAGINGDIR)/SobelYFilter.class \
	$(IMAGINGDIR)/Laplace3Filter.class \
	\
	$(IMAGINGDIR)/LookupFilter.class \
	$(IMAGINGDIR)/InvertLookupFilter.class \
	$(IMAGINGDIR)/OffsetFilter.class \
	$(IMAGINGDIR)/ThresholdFilter.class \
	$(IMAGINGDIR)/InsideRangeFilter.class \
	$(IMAGINGDIR)/SelectRegionFilter.class \
	\
	$(IMAGINGDIR)/ReplaceRegionFilter.class \
	$(IMAGINGDIR)/CatHFilter.class \
	$(IMAGINGDIR)/CatVFilter.class \
	$(IMAGINGDIR)/RandomFilter.class \
	$(IMAGINGDIR)/ConstantColorFilter.class \
	$(IMAGINGDIR)/GradientColorFilter.class \
	$(IMAGINGDIR)/GridFilter.class \
	\
	$(IMAGINGDIR)/ImageMux21.class \
	$(IMAGINGDIR)/TriggeredFilter.class \


STRING =\
	$(STRINGDIR)/StringSignal.class \
	$(STRINGDIR)/PortString.class \
	$(STRINGDIR)/StringDisplay.class \
	$(STRINGDIR)/StringDisplay2.class \

RUGE =\
	$(RUGEDIR)/IntegerSignal.class \
	$(RUGEDIR)/Constant.class \
	$(RUGEDIR)/Register.class \
	$(RUGEDIR)/Latch.class \
	$(RUGEDIR)/Mux.class \
	$(RUGEDIR)/Adder.class \
	$(RUGEDIR)/Alu.class \
	$(RUGEDIR)/Incr.class \
	$(RUGEDIR)/TriBuf.class \
	$(RUGEDIR)/DelayNode.class \
	$(RUGEDIR)/RAM_64K.class \
#	$(RUGEDIR)/RegisterBank.class \

HAGEN =\
	$(HAGENDIR)/SimpleShiftRegister.class \
	$(HAGENDIR)/ROM_8x8.class \


MCS4	=\
	$(MCS4DIR)/AbstractIntel4000.class \
	$(MCS4DIR)/AddressStack.class \
	$(MCS4DIR)/AluRegion.class \
	$(MCS4DIR)/ContentObject.class \
	$(MCS4DIR)/ContentPanel.class \
	$(MCS4DIR)/ContentSender.class \
	$(MCS4DIR)/ExecutionUnit.class \
	$(MCS4DIR)/Instruction.class \
	$(MCS4DIR)/InstructionSet.class \
	$(MCS4DIR)/InternalState.class \
	$(MCS4DIR)/MCS4Assembler.class \
	$(MCS4DIR)/MemoryWrapper.class \
	$(MCS4DIR)/ScratchPad.class \
	$(MCS4DIR)/ValueChangeListener.class \
	$(MCS4DIR)/i4001.class \
	$(MCS4DIR)/i4001BeanInfo.class \
	$(MCS4DIR)/i4001Decoder.class \
	$(MCS4DIR)/i4001EditorFrame.class \
	$(MCS4DIR)/i4001MemoryCanvas.class \
	$(MCS4DIR)/i4001PortTypePropertyEditor.class \
	$(MCS4DIR)/i4002.class \
	$(MCS4DIR)/i4002BeanInfo.class \
	$(MCS4DIR)/i4002ChipTypePropertyEditor.class \
	$(MCS4DIR)/i4002EditorFrame.class \
	$(MCS4DIR)/i4003.class \
	$(MCS4DIR)/i4004.class \
	$(MCS4DIR)/i4004EditorFrame.class \
	$(MCS4DIR)/i4004InternalReg.class \


SWITCHED =\
	$(SWITCHEDDIR)/Switch.class \
	$(SWITCHEDDIR)/ISwitch.class \
	$(SWITCHEDDIR)/ISwitch2.class \
	$(SWITCHEDDIR)/NTRAN.class \
	$(SWITCHEDDIR)/NTRANh.class \
	$(SWITCHEDDIR)/PTRAN.class \
	$(SWITCHEDDIR)/TGATE.class \
	$(SWITCHEDDIR)/AnimatedTgate.class \
	$(SWITCHEDDIR)/Relay1.class \
	$(SWITCHEDDIR)/Relay2.class \
	$(SWITCHEDDIR)/Relay4.class \
	$(SWITCHEDDIR)/Bulb.class \
	$(SWITCHEDDIR)/BulbBig.class \

DSP =\
	$(DSPDIR)/GenericDspOperator.class \
	$(DSPDIR)/StdLogicVectorToDouble.class \
	$(DSPDIR)/DoubleToStdLogicVector.class \
	$(DSPDIR)/DoubleToStdLogic1164.class \
	$(DSPDIR)/DoubleToInteger.class \
	$(DSPDIR)/IntegerToDouble.class \
	$(DSPDIR)/Printf.class \
	$(DSPDIR)/LevelTrigger.class \
	\
	$(DSPDIR)/Register.class \
	$(DSPDIR)/Counter.class \
	$(DSPDIR)/CounterR.class \
	$(DSPDIR)/CounterWrapAround.class \
	$(DSPDIR)/SimTime.class \
	$(DSPDIR)/Random.class \
	$(DSPDIR)/Scale.class \
	$(DSPDIR)/Clip.class \
	$(DSPDIR)/parser/AXP.class \
	$(DSPDIR)/Function.class \
	$(DSPDIR)/Delay.class \
	$(DSPDIR)/Oscilloscope.class \
	\
	$(DSPDIR)/Add.class \
	$(DSPDIR)/Sub.class \
	$(DSPDIR)/Mult.class \
	$(DSPDIR)/Div.class \
	$(DSPDIR)/Constant.class \
	$(DSPDIR)/Reciprocal.class \
	$(DSPDIR)/Neg.class \
	\
	$(DSPDIR)/Max.class \
	$(DSPDIR)/Max3.class \
	$(DSPDIR)/Min.class \
	$(DSPDIR)/Min3.class \
	$(DSPDIR)/Mux21.class \
	$(DSPDIR)/Mux41.class \
	\
	$(DSPDIR)/Sin.class \
	$(DSPDIR)/Cos.class \
	$(DSPDIR)/Tan.class \
	$(DSPDIR)/Asin.class \
	$(DSPDIR)/Acos.class \
	$(DSPDIR)/Atan.class \
	$(DSPDIR)/Exp.class \
	$(DSPDIR)/Log.class \
	$(DSPDIR)/Log2.class \
	$(DSPDIR)/Log10.class \



RTLIB =\
	$(RTLIBDIR)/GenericRtlibObject.class \
	\
	$(RTLIB_IO_DIR)/IpinVector.class \
	$(RTLIB_IO_DIR)/OpinVector.class \
	$(RTLIB_IO_DIR)/IpinVectorLarge.class \
	$(RTLIB_IO_DIR)/OpinVectorLarge.class \
	$(RTLIB_IO_DIR)/Constant.class \
	$(RTLIB_IO_DIR)/SmallConstant.class \
	$(RTLIB_IO_DIR)/Merge.class \
	$(RTLIB_IO_DIR)/Merge3.class \
	$(RTLIB_IO_DIR)/Subset.class \
	$(RTLIB_IO_DIR)/SubsetFlip.class \
	$(RTLIB_IO_DIR)/BusTapRight.class \
	$(RTLIB_IO_DIR)/BusTapBottom.class \
	$(RTLIB_IO_DIR)/SelectBit.class \
	$(RTLIB_IO_DIR)/Expander.class \
	$(RTLIB_IO_DIR)/ExpanderVertical.class \
	$(RTLIB_IO_DIR)/MergeBits.class \
	$(RTLIB_IO_DIR)/ExpandBit.class \
	\
	$(RTLIB_ARITH_DIR)/Incr.class \
	$(RTLIB_ARITH_DIR)/Incr2.class \
	$(RTLIB_ARITH_DIR)/Decr.class \
	$(RTLIB_ARITH_DIR)/TwosComplement.class \
	$(RTLIB_ARITH_DIR)/Add.class \
	$(RTLIB_ARITH_DIR)/Sub.class \
	$(RTLIB_ARITH_DIR)/Addc.class \
	$(RTLIB_ARITH_DIR)/GenericShifter.class \
	$(RTLIB_ARITH_DIR)/ShiftLeft.class \
	$(RTLIB_ARITH_DIR)/ShiftRightArith.class \
	$(RTLIB_ARITH_DIR)/ShiftRightLogic.class \
	$(RTLIB_ARITH_DIR)/RotateLeft.class \
	$(RTLIB_ARITH_DIR)/RotateRight.class \
	$(RTLIB_ARITH_DIR)/UserDefinedALU.class \
	$(RTLIB_ARITH_DIR)/DcoreALU.class \
	$(RTLIB_ARITH_DIR)/DcoreALU2.class \
	\
	$(RTLIB_COMPARE_DIR)/CompareEqual.class \
	$(RTLIB_COMPARE_DIR)/CompareNotEqual.class \
	$(RTLIB_COMPARE_DIR)/CompareGreater.class \
	$(RTLIB_COMPARE_DIR)/CompareLess.class \
	$(RTLIB_COMPARE_DIR)/CompareAll.class \
	\
	$(RTLIB_LOGIC_DIR)/BitwiseAnd.class \
	$(RTLIB_LOGIC_DIR)/BitwiseNot.class \
	$(RTLIB_LOGIC_DIR)/BitwiseOr.class \
	$(RTLIB_LOGIC_DIR)/BitwiseXor.class \
	$(RTLIB_LOGIC_DIR)/N1And.class \
	$(RTLIB_LOGIC_DIR)/N1Or.class \
	\
	$(RTLIB_LOGIC_DIR)/GenericOnebitLogicObject.class \
	$(RTLIB_LOGIC_DIR)/And.class \
	$(RTLIB_LOGIC_DIR)/Nand.class \
	$(RTLIB_LOGIC_DIR)/Nor.class \
	$(RTLIB_LOGIC_DIR)/Or.class \
	$(RTLIB_LOGIC_DIR)/Xor.class \
	$(RTLIB_LOGIC_DIR)/Xnor.class \
	\
	$(RTLIB_MUXES_DIR)/Mux21.class \
	$(RTLIB_MUXES_DIR)/Mux41.class \
	$(RTLIB_MUXES_DIR)/TriBuf.class \
	$(RTLIB_MUXES_DIR)/TriBufBig.class \
	$(RTLIB_MUXES_DIR)/Decoder.class \
	$(RTLIB_MUXES_DIR)/BitDecoder.class \
	\
	$(RTLIB_REGISTER_DIR)/Reg.class \
	$(RTLIB_REGISTER_DIR)/RegE.class \
	$(RTLIB_REGISTER_DIR)/RegR.class \
	$(RTLIB_REGISTER_DIR)/RegRE.class \
	$(RTLIB_REGISTER_DIR)/Latch.class \
	$(RTLIB_REGISTER_DIR)/LatchR.class \
	$(RTLIB_REGISTER_DIR)/ShiftRegR.class \
	$(RTLIB_REGISTER_DIR)/CounterRE.class \
	$(RTLIB_REGISTER_DIR)/LFSR.class \
	$(RTLIB_REGISTER_DIR)/RegWithInitialValue.class \
	\
	$(RTLIB_MEMORY_DIR)/GenericMemory.class \
	$(RTLIB_MEMORY_DIR)/ROM.class \
	$(RTLIB_MEMORY_DIR)/ROMcs.class \
	$(RTLIB_MEMORY_DIR)/ROMoe.class \
	$(RTLIB_MEMORY_DIR)/RAM.class \
	$(RTLIB_MEMORY_DIR)/RAMoe.class \
	$(RTLIB_MEMORY_DIR)/DPRAM.class \
	$(RTLIB_MEMORY_DIR)/RegBank.class \
	$(RTLIB_MEMORY_DIR)/MipsRegBank.class \
	$(RTLIB_MEMORY_DIR)/MicroROM.class \
	$(RTLIB_MEMORY_DIR)/MR.class \
	$(RTLIB_MEMORY_DIR)/MR20.class \
	$(RTLIB_MEMORY_DIR)/MRCanvas.class \
	$(RTLIB_MEMORY_DIR)/MRLabelCanvas.class \
	$(RTLIB_MEMORY_DIR)/MREditorFrame.class \
	$(RTLIB_MEMORY_DIR)/AddressDecoder4.class \
	\
	$(RTLIB_MEMORY_DIR)/RealTimeClock.class \
#$(RTLIB_MEMORY_DIR)/RegBank.class \
	\
	$(RTLIBDIR)/Incr.class \
	$(RTLIBDIR)/Adder.class \


MICROJAVA =\
	$(MICROJAVADIR)/ALU.class \
	$(MICROJAVADIR)/BuffReg.class \
	$(MICROJAVADIR)/DFF.class \
	$(MICROJAVADIR)/DFFE.class \
	$(MICROJAVADIR)/IFU.class \
	$(MICROJAVADIR)/MROM.class \
	$(MICROJAVADIR)/MRR.class \
	$(MICROJAVADIR)/PcReg.class \
	$(MICROJAVADIR)/RAMoe.class \
	$(MICROJAVADIR)/ROMoe.class \
	$(MICROJAVADIR)/RegR.class 


GUI =\
	$(GUIDIR)/StatusPanel.class \
	$(GUIDIR)/AWTStatusPanel.class \
	$(GUIDIR)/WindowCloser.class \
	$(GUIDIR)/Trafo2D.class \
	$(GUIDIR)/ObjectCanvas.class \
	$(GUIDIR)/AWTObjectCanvas.class \
	$(GUIDIR)/SyncRedrawTimer.class \
	$(GUIDIR)/StringDialog.class \
	$(GUIDIR)/AWTStringDialog.class \
	$(GUIDIR)/ImageCanvas.class \
	$(GUIDIR)/ImageButton.class \
	$(GUIDIR)/CloseableFrame.class \
	$(GUIDIR)/DidYouKnowFrame.class \
	$(GUIDIR)/LayerTable.class \
	$(GUIDIR)/EditorMenuInteraction.class \
	$(GUIDIR)/EditFrame.class \
	$(GUIDIR)/UndoStack.class \
	$(GUIDIR)/Command.class \
	$(GUIDIR)/MoveCommand.class \
	$(GUIDIR)/CopyCommand.class \
	$(GUIDIR)/EditCommand.class \
	$(GUIDIR)/CreateCommand.class \
	$(GUIDIR)/ColibriCreateCommand.class \
	$(GUIDIR)/CreateSubdesignCommand.class \
	$(GUIDIR)/ColibriCreateSubdesignCommand.class \
	$(GUIDIR)/CreateByNameCommand.class \
	$(GUIDIR)/DeleteCommand.class \
	$(GUIDIR)/DeleteComponentCommand.class \
	$(GUIDIR)/DeleteSignalCommand.class \
	$(GUIDIR)/DeleteAllCommand.class \
	$(GUIDIR)/ZoomRegionCommand.class \
	$(GUIDIR)/CreateSignalCommand.class \
	$(GUIDIR)/AddSegmentToSignalCommand.class \
	$(GUIDIR)/InsertVertexIntoSignalCommand.class \
	$(GUIDIR)/DeleteSegmentFromSignalCommand.class \
	$(GUIDIR)/AddProbeToSignalCommand.class \
	$(GUIDIR)/DeleteProbeFromSignalCommand.class \
	$(GUIDIR)/SignalMovePointCommand.class \
	$(GUIDIR)/SignalSetValueCommand.class \
	$(GUIDIR)/ChangeNameCommand.class \
	$(GUIDIR)/ChangeSignalNameCommand.class \
	$(GUIDIR)/SetDesignNameCommand.class \
	$(GUIDIR)/OpenDesignCommand.class \
	$(GUIDIR)/MoveToPositiveQuadrantCommand.class \
	$(GUIDIR)/AutoconnectCommand.class \
	$(GUIDIR)/DisconnectCommand.class \
	$(GUIDIR)/DisconnectPortCommand.class \
	$(GUIDIR)/MirrorXCommand.class \
	$(GUIDIR)/MirrorYCommand.class \
	$(GUIDIR)/SelectObjectCommand.class \
	$(GUIDIR)/SelectRegionCommand.class \
	$(GUIDIR)/SelectAllCommand.class \
	$(GUIDIR)/MoveSelectionCommand.class \
	$(GUIDIR)/DeleteSelectionCommand.class \
	$(GUIDIR)/DeselectAllCommand.class \
	$(GUIDIR)/TrafficLight.class \
	$(GUIDIR)/MultiLineLabel.class \
	$(GUIDIR)/SimControlPanel.class \
	$(GUIDIR)/AWTSimControlPanel.class \
	$(GUIDIR)/PropertySheet.class \
	$(GUIDIR)/AWTPropertySheet.class \
	$(GUIDIR)/KeyHandler.class \
	$(GUIDIR)/ConfirmDialog.class \
	$(GUIDIR)/SaveChangesDialog.class \
	$(GUIDIR)/OKtoQuit.class \
	$(GUIDIR)/SelectFileOrURLDialog.class \
	$(GUIDIR)/AboutDialog.class \
	$(GUIDIR)/ExportOptionsDialog.class \
	$(GUIDIR)/AWTExportOptionsDialog.class \
	$(GUIDIR)/SelectURLDialog.class \
	$(GUIDIR)/AWTSelectURLDialog.class \
	$(GUIDIR)/GUIFactory.class \
	$(GUIDIR)/AWTFactory.class \
	$(GUIDIR)/SwingFactory.class \
	$(GUIDIR)/Editor.class \
	$(GUIDIR)/EditorInApplet.class \
	$(GUIDIR)/HexTextField.class \
	$(GUIDIR)/MemoryHexEditorField.class \
	$(GUIDIR)/MemoryEditorFrame.class \
	$(GUIDIR)/CanvasScroller.class \
	$(GUIDIR)/StimuliEditorCanvas.class \
	$(GUIDIR)/StimuliEditor.class \
	$(GUIDIR)/PropertiesViewer.class \
	$(GUIDIR)/Log.class \
	$(GUIDIR)/LogManager.class \
	\
	$(GUIDIR)/JConsole.class \
	$(GUIDIR)/JConfirmDialog.class \
	$(GUIDIR)/JStringDialog.class \
	$(GUIDIR)/JSelectURLDialog.class \
	$(GUIDIR)/JAboutDialog.class \
	$(GUIDIR)/JStatusPanel.class \
	$(GUIDIR)/JPropertySheet.class \
	$(GUIDIR)/JObjectCanvas.class \
	$(GUIDIR)/JMultiLineToolTip.class \
	$(GUIDIR)/JCanvasScroller.class \
	$(GUIDIR)/JTrafficLight.class \
	$(GUIDIR)/JImageButton.class \
	$(GUIDIR)/JSimControlPanel.class \
	$(GUIDIR)/JPropertiesViewer.class \
	$(GUIDIR)/JEditFrame.class \
	$(GUIDIR)/JExportOptionsAdapter.class \
	\
	$(GUIDIR)/T1Editor.class \
	$(GUIDIR)/JythonConsole.class \
#	$(GUIDIR)/JPShell.class \
#	$(GUIDIR)/AWTExportOptionsAdapter.class \
	

STYX =\
	$(STYXDIR)/TimeFormatter.class \
	$(STYXDIR)/TimePanel.class \
	$(STYXDIR)/Transformation.class \
	$(STYXDIR)/Xscroller.class \
	$(STYXDIR)/Yscroller.class \
	$(STYXDIR)/Waveform.class \
	$(STYXDIR)/WaveStdLogic1164.class \
	$(STYXDIR)/WaveStdLogicVector.class \
	$(STYXDIR)/WaveInteger.class \
	$(STYXDIR)/WaveDouble.class \
	$(STYXDIR)/WaveString.class \
	$(STYXDIR)/WaveCanvas.class \
	$(STYXDIR)/NameCanvas.class \
	$(STYXDIR)/WaveformViewer.class \

MANAGER =\
	$(MANAGERDIR)/SimObjectNotFoundException.class \
	$(MANAGERDIR)/SimObjectVersionNotFoundException.class \
	$(MANAGERDIR)/DesignManager.class \
	$(MANAGERDIR)/ExtensionFileFilter.class \
	$(MANAGERDIR)/CreateThumbnail.class \
	$(MANAGERDIR)/Browser.class \
	$(MANAGERDIR)/ComponentInfo.class \
	$(MANAGERDIR)/ComponentInfoDialog.class \
	$(MANAGERDIR)/CreateComponentInfo.class \
	\
	$(MANAGERDIR)/tree/SortedTreeNode.class \
	$(MANAGERDIR)/tree/RootTreeNode.class \
	$(MANAGERDIR)/tree/ResourceRootTreeNode.class \
	$(MANAGERDIR)/tree/ZipRootTreeNode.class \
	$(MANAGERDIR)/tree/FileRootTreeNode.class \
	$(MANAGERDIR)/tree/DirectoryTreeNode.class \
	$(MANAGERDIR)/tree/SimObjectTreeNode.class \
	$(MANAGERDIR)/tree/DesignFileTreeNode.class \
	$(MANAGERDIR)/tree/TextFileTreeNode.class \
	$(MANAGERDIR)/tree/AssemblerFileTreeNode.class \
	$(MANAGERDIR)/tree/PythonFileTreeNode.class \
	$(MANAGERDIR)/tree/ReadmeFileTreeNode.class \
	\
	$(MANAGERDIR)/HadesTreeCellRenderer.class \
	$(MANAGERDIR)/TreeManager.class \
	$(MANAGERDIR)/TreePopupMenu.class \
	$(MANAGERDIR)/InfoPanel.class \
	$(MANAGERDIR)/Colibri.class \

#	$(MANAGERDIR)/TSL.class \

UTILS =\
	$(UTILSDIR)/JavaVersionCheck.class \
	$(UTILSDIR)/NameListener.class \
	$(UTILSDIR)/Parser.class \
	$(UTILSDIR)/StringTokenizer.class \
	$(UTILSDIR)/ValidName.class \
	$(UTILSDIR)/DesignHierarchyNavigator.class \
	$(UTILSDIR)/NameMangler.class \
	$(UTILSDIR)/ShellSort.class \
	$(UTILSDIR)/TimeFormatter.class \
	$(UTILSDIR)/IntegerFormatter.class \
	$(UTILSDIR)/Flatten.class \
	$(UTILSDIR)/SignalEnumerator.class \
	$(UTILSDIR)/EndsWithFilter.class \
	$(UTILSDIR)/FigWriter.class \
	$(UTILSDIR)/Selection.class \
	$(UTILSDIR)/DecimalFormat.class \
	$(UTILSDIR)/HexFormat.class \
	$(UTILSDIR)/ContextToolTip.class \
	$(UTILSDIR)/ToolTipManager.class \
	$(UTILSDIR)/IntelHexFile.class \
	$(UTILSDIR)/LFSR32.class \
	$(UTILSDIR)/MemoryDec2HexConverter.class \
	$(UTILSDIR)/MemoryMultiple2SingleConverter.class \
	$(UTILSDIR)/JviewJythonWrapper.class \
	$(UTILSDIR)/ISCAS89Converter.class \
	$(UTILSDIR)/AudioPlayer.class \
	$(UTILSDIR)/AudioFileLoader.class \
	$(UTILSDIR)/FreeTTSWrapper.class \
	$(UTILSDIR)/MakeJarFromClassList.class \
	$(UTILSDIR)/MakeAppletClassList.class \
	$(UTILSDIR)/TestLoadAllDesigns.class \
	$(UTILSDIR)/RedrawStressTest.class \
	$(UTILSDIR)/MatlabAdapter.class \
	\
	$(VHDLDIR)/VHDLExportable.class \
	$(VHDLDIR)/VHDLNameMangler.class \
	$(VHDLDIR)/VHDLWriter.class \
	$(VHDLDIR)/VHDLModelFactory.class \
	\
	$(UTILSDIR)/BatchMode.class \
	$(UTILSDIR)/RunHadesDemo.class \
	$(UTILSDIR)/TestStdLogicVectorOverflow.class \
	$(UTILSDIR)/LogPlaybackManager.class \

JPSHELL =\
	$(JPSHELLDIR)/History.class \
	$(JPSHELLDIR)/MyPythonInterpreter.class \
	$(JPSHELLDIR)/JPWrapper.class \
	$(JPSHELLDIR)/JPShell.class \
	$(JPSHELLDIR)/JPEditor.class \

STIMULI =\
	$(STIMULIDIR)/StimuliParser.class \
	$(STIMULIDIR)/StimuliGenerator.class \

UNUSED =\
	$(IODIR)/Trigger.class \
	$(GUIDIR)/MemoryHexEditorFieldWithPopup.class \
	$(MCOREDIR)/DcoreDisassemblerCanvas.class \
	$(MANAGERDIR)/TreeDemo.class \
	$(MANAGERDIR)/Gabi.class \


all: $(OBJ) $(SIMOBJ) $(MODELOBJ) $(SYMBOLOBJ) $(GATES) \
	$(MEMORY) \
	$(COMPLEXGATES) $(FLIPFLOPS) $(TTLS) $(RTLS) $(DCF77S) $(META) \
	$(I8048) $(REGS) $(FSMS) $(UTILS) $(GUI) $(MANAGER) \
	$(SPECIAL) $(IMAGING) $(STRING) $(RUGE) $(DELAYNODES) \
	$(GATESWITHDINSYMBOLS) \
	$(RTLIB) \
	$(MICROJAVA) \
	$(STYX) \
	$(PIC16C84) \
	$(MCORE) \
	$(JPSHELL) \
	$(MIPS) \
	$(MCS4) \
	$(HAGEN) \
	$(SWITCHED) \
	$(DSP) \
	$(STIMULI) \
#	$(WAVES) \

MIPS:
	(cd $(MIPSDIR); make; ) 


clean:	
	rm -f *.class 
	rm -f */*.class
	rm -f */*/*.class
	rm -f models/*/*.class
	rm -f models/*/*/*.class


zuluzip:
	@echo "creating /tmp/hades-applet.jar (simple mode)"
	- cd ..; pwd; jar cvmf hades/gui/Manifest /tmp/hades-applet.jar \
		hades/simulator/*.class \
		hades/signals/*.class \
		hades/symbols/*.class \
		hades/styx/*.class \
		hades/utils/*.class \
		hades/manager/*.class \
		hades/gui/*.class \
		hades/gui/*Popup*txt \
		hades/gui/images/iconEditor.gif \
		hades/gui/images/hades.gif \
		hades/gui/images/hades.gif \
		hades/gui/images/lcd-matrix.gif \
		hades/gui/images/simcontrol.gif \
		hades/gui/images/terminal-big.gif \
		hades/gui/images/wavebuttons.gif \
		hades/models/*.class hades/models/*.sym \
		hades/models/io/*.class \
                hades/models/io/*.sym \
                hades/models/io/*.fig \
		hades/models/gates/*.class \
                hades/models/gates/*.sym \
                hades/models/complexgates/*.class \
                hades/models/complexgates/*.sym \
                hades/models/complexgates/*.fig \
                hades/models/gatter/*.class \
                hades/models/gatter/*.sym \
                hades/models/flipflops/*.class \
                hades/models/flipflops/*.sym \
                hades/models/register/*.class \
                hades/models/register/*.sym \
                hades/models/special/*.class \
                hades/models/special/*.sym \
                hades/models/ttl74/*.class \
                hades/models/ttl74/*.sym \
                hades/models/ttl74/*.hds \
                hades/models/ttl74/*.fig \
		jfig/canvas/*.class \
		jfig/objects/*.class \
		jfig/gui/*.class \
		jfig/java2d/*.class \
		jfig/utils/*.class \
		jfig/commands/FigCommand.class 
	mv /tmp/hades-applet.jar zulu.jar



appletzipXXX:
	@echo creating /tmp/hades-applet.jar applet JAR from classlist2.txt
	- cd ..; java hades.utils.MakeJarFromClassList /tmp/hades-applet.jar hades/classlist2.txt -magic
	cp /tmp/hades-applet.jar webdemos/classes/


#
# The 'base' hades-applet.jar includes all signals, simulator, symbol, 
# utilities, and design-manager classes.
# We also include all basic simulation models, all basic and complex gates,
# the DIN-style gates, all flipflops, all I/O components, and the
# counter and trigger models.
#

appletzip:
	@echo creating default /tmp/hades-applet.jar applet JAR 
	- cd ..; jar cvMf /tmp/hades-applet.jar \
		hades/.hadesrc \
		hades/.clblist.txt \
		hades/gui/*.class \
		hades/gui/images/hades.gif \
		hades/gui/images/iconEditor.gif \
		hades/gui/images/lcd-matrix.gif \
		hades/gui/images/simcontrol.gif \
		hades/gui/images/terminal-big.gif \
		hades/gui/images/wavebuttons.gif \
		hades/gui/*Popup*txt \
		hades/doc/help \
		hades/manager/*.class \
		hades/manager/icons/*.gif \
		hades/manager/tree/*.class \
		hades/signals/*.class \
		hades/simulator/*.class \
		hades/styx/*.class \
		hades/symbols/*.class \
		hades/utils/*.class \
		\
		hades/models/*.class \
		hades/models/*.fig \
		\
		hades/models/complexgates/*.class \
		hades/models/complexgates/*.clb \
		hades/models/complexgates/*.fig \
		hades/models/complexgates/*.sym \
		\
		hades/models/flipflops/*.class \
		hades/models/flipflops/*.clb \
		hades/models/flipflops/*.sym \
		\
		hades/models/gates/*.class \
		hades/models/gates/*.clb \
		hades/models/gates/*.sym \
		\
		hades/models/gatter/*.class \
		hades/models/gatter/*.clb \
		hades/models/gatter/*.sym \
		\
		hades/models/io/*.class \
		hades/models/io/*.clb \
		hades/models/io/*.fig\
		hades/models/io/*.sym \
		\
		hades/models/special/Counter*class \
		hades/models/special/Counter.clb \
		hades/models/special/Counter.sym \
		hades/models/special/*Trigger*class \
		hades/models/special/*Trigger.clb\
		hades/models/special/*Trigger.sym \
		\
		hades/models/meta/Label*.class \
		hades/models/meta/Highlighter*.class \
		hades/models/meta/Highlighter*.sym \
		hades/models/meta/TTS*.class \
		hades/models/meta/TTS*.sym \
		\
		hades/models/memory/*.class \
		hades/models/string/*.class \
		\
		jfig/canvas/*.class \
		\
		jfig/commands/Command.class \
		jfig/commands/FigBasicEditor.class \
		jfig/commands/EditObjectCommand.class \
		jfig/commands/JEditObjectCommand.class \
		\
		jfig/gui/JFigViewerBean*class \
		jfig/gui/JAboutDialog*class \
		jfig/gui/JAttribsControlsFactory*class \
		jfig/gui/JConsole*class \
		jfig/gui/J*Button*class \
		jfig/gui/JEditBaseobjectDialog*class \
		jfig/gui/JEditTextDialog*class \
		jfig/gui/JExportOptionsDialog*class \
		jfig/gui/JPropertiesViewer*class \
		jfig/gui/JStatusCanvas*class \
		jfig/gui/JTextViewer*class \
		jfig/gui/JWindowCloser.class \
		\
		jfig/gui/ConsoleMessage.class \
		jfig/gui/ColorCache.class \
		jfig/gui/EditObjectBaseDialog.class \
		jfig/gui/EditTextDialog.class \
		jfig/gui/FontCache*class \
		jfig/gui/ImageHelper.class \
		jfig/gui/InvertGrayFilter.class \
		jfig/gui/SimpleTextViewer*class \
		jfig/gui/StatusMessage.class \
		\
		jfig/images/buttons.gif \
		jfig/images/fillpatterns.gif \
		jfig/images/fontmenu.gif \
		jfig/images/icon.gif \
		jfig/images/manhattan.gif \
		\
		jfig/java2d/*.class \
		jfig/objects/*.class \
		\
		jfig/utils/AntiDeadlock.class \
		jfig/utils/BoundingBoxCalculator.class \
		jfig/utils/ExceptionTracer.class \
		jfig/utils/FilteredFigWriter.class \
		jfig/utils/Format.class \
		jfig/utils/JRecentFileManager.class \
		jfig/utils/LP2*class \
		jfig/utils/MouseMapper.class \
		jfig/utils/PPMReader.class \
		jfig/utils/PPMWriter.class \
		jfig/utils/Pathname.class \
		jfig/utils/RecentFileManager.class \
		jfig/utils/RegistrationKeyManager.class \
		jfig/utils/SetupManager.class \
		jfig/utils/ShellSort.class \
		jfig/utils/TmpFile.class \
		jfig/utils/Xspline*class \
		\
		jfig/jfig.cnf \
		jfig/doc/README \
		jfig/doc/LICENSE
	cp /tmp/hades-applet.jar webdemos/classes/
	#
	- cd ..; jar cvMf /tmp/hades-models-rtl.jar \
		hades/models/memory/*.class \
		hades/models/rtl/*.class \
		hades/models/rtl/*.clb \
		hades/models/rtl/*.rom \
		hades/models/rtl/*.sym 
	cp /tmp/hades-models-rtl.jar webdemos/classes/
	#
	- cd ..; jar cvMf /tmp/hades-models-fsm.jar \
		hades/models/fsm/*.class \
		hades/models/fsm/*.clb \
		hades/models/fsm/*.gif \
		hades/models/fsm/default.fsm \
		hades/models/string/*.class
	cp /tmp/hades-models-fsm.jar webdemos/classes/
	#
	- cd ..; jar cvMf /tmp/hades-models-dcore.jar \
		hades/models/mcore/*.class \
		hades/models/mcore/*.clb \
		hades/models/mcore/*.gif \
		hades/models/mcore/*.sym 
	cp /tmp/hades-models-dcore.jar webdemos/classes/
	#
	- cd ..; jar cvMf /tmp/hades-models-ttl.jar \
		hades/models/rtl/empty.rom \
		hades/models/ttl74/*.class \
		hades/models/ttl74/*.clb \
		hades/models/ttl74/*.sym \
		hades/models/ttl74/*.hds \
		hades/models/ttl74/figs/*.*
	cp /tmp/hades-models-ttl.jar webdemos/classes/
	#
	- cd ..; jar cvMf /tmp/hades-models-register.jar \
		hades/models/register/*.class \
		hades/models/register/*.clb \
		hades/models/register/*.sym \
		hades/utils/LFSR32.class 
	cp /tmp/hades-models-register.jar webdemos/classes/
	#
	- cd ..; jar cvMf /tmp/hades-models-pic.jar \
		hades/models/pic/*.class \
		hades/models/pic/*.clb \
		hades/models/pic/*.sym \
		hades/models/pic/help/*.txt \
		hades/utils/IntelHexFile.class 
	cp /tmp/hades-models-pic.jar webdemos/classes/
	#
	- cd ..; jar cvMf /tmp/hades-models-rtlib.jar \
		hades/*/*StdLogicVector*class \
		hades/gui/HexTextField*class \
		hades/gui/MemoryHexEditorField*class \
		hades/gui/MemoryEditorFrame*class \
		hades/gui/CloseableFrame*class \
		hades/utils/ToolTipManager*class \
		hades/gui/MultiLineLabel*class \
		hades/models/memory/*.class \
		hades/models/flipflops/Dffe.class \
		hades/models/flipflops/Dffe.sym\
		hades/models/rtlib/GenericRtlibObject*class \
		hades/models/rtlib/*/*.class \
		hades/models/rtlib/*/*.sym \
		hades/models/string/*.class \
		hades/symbols/BusPortSymbol.class \
		hades/symbols/FatInstanceLabel.class \
		hades/gui/MicroRomEditorCanvas*class \
		jfig/gui/SimpleTextViewer*class 
	cp /tmp/hades-models-rtlib.jar webdemos/classes/
	#
	- cd ..; jar cvMf /tmp/hades-models-microjava.jar \
		hades/models/microjava/*.class \
		hades/models/microjava/*.clb \
		hades/models/microjava/*.hds \
		hades/models/microjava/*.sym \
		hades/models/microjava/*.rom
	cp /tmp/hades-models-microjava.jar webdemos/classes/
	#
	- cd ..; jar cvMf /tmp/hades-models-special.jar \
		hades/models/special/*.class \
		hades/models/special/*.clb \
		hades/models/special/*.fig \
		hades/models/special/*.sym \
		hades/models/special/demo.sti \
		\
		hades/modes/meta/*.class \
		hades/modes/meta/*.clb \
		hades/modes/meta/*.sym  \
		\
		hades/models/dcf77/*.class \
		hades/models/dcf77/*.clb \
		hades/models/dcf77/*.sym
	cp /tmp/hades-models-special.jar webdemos/classes/
	#
	- cd ..; jar cvMf /tmp/hades-models-stimuli.jar \
		hades/models/StdLogicVector*class \
		hades/utils/DesignHierarchyNavigator*class \
		hades/models/stimuli/*.class \
		hades/models/stimuli/*.sym \
		hades/models/stimuli/demo.sti 
	cp /tmp/hades-models-stimuli.jar webdemos/classes/
	#
	- cd ..; jar cvMf /tmp/hades-models-switched.jar \
		hades/models/switched/*.class \
		hades/models/switched/*.clb \
		hades/models/switched/*.sym 
	cp /tmp/hades-models-switched.jar webdemos/classes/
	#
	- cd ..; jar cvMf /tmp/hades-models-mips.jar \
		hades/models/mips/*/*class \
		hades/models/mips/mipsmemory/*.clb \
		hades/models/mips/mipsmemory/*.sym \
		hades/models/mips/examples/prim/*
	cp /tmp/hades-models-mips.jar webdemos/classes/
	#
	- cd ..; jar cvMf /tmp/hades-models-mcs4.jar \
		hades/models/mcs4/*class \
		hades/models/mcs4/*sym  \
		hades/*/*StdLogicVector*class \
		hades/models/io/SevenSegmentMultiplexed*class \
		hades/models/special/ValueTrigger*class \
		hades/models/memory/*.class \
		hades/models/rtlib/memory/GenericMemory*class \
		hades/models/rtlib/memory/RAM*class \
		hades/models/rtlib/memory/ROM*class \
		hades/models/mcore/DcoreDecoder*.class \
		hades/models/mcore/DcoreDisassembler*.class \
		hades/utils/HexFormat.class \
		hades/gui/MemoryHexEditorField*class \
		hades/gui/MemoryEditorFrame*class \
		hades/gui/HexTextField*class 
	cp /tmp/hades-models-mcs4.jar webdemos/classes/
	#
	- cd ..; jar cvMf /tmp/hades-models-imaging.jar \
		hades/models/imaging/*class \
		hades/models/imaging/*sym \
		hades/models/imaging/256_*.jpg
	cp /tmp/hades-models-imaging.jar webdemos/classes/
	#
	- cd ..; jar cvMf /tmp/hades-models-dsp.jar \
		hades/models/rtlib/GenericRtlibObject*class \
		hades/models/dsp/*.class \
		hades/models/dsp/*.clb \
		hades/models/dsp/*.sym 
	cp /tmp/hades-models-dsp.jar webdemos/classes/
	#
	# Prof. Ferreira demos
	- cd ..; jar cvMf /tmp/hades-models-dpi.jar \
		dpi/*/*.class dpi/*/*/*.class \
		dpi/*/*.clb dpi/*/*/*.clb \
		dpi/*/*.sym dpi/*/*/*.sym \
                dpi/grafico/org/nfunk/jep/*.class \
                dpi/grafico/org/nfunk/jep/type/*.class \
                dpi/grafico/org/nfunk/jep/function/*.class 
	cp /tmp/hades-models-dpi.jar webdemos/classes/
	# Prof. Ferreira Femtojava stuff
	- cd ~/hades-ferreira2; jar cvMf /tmp/hades-models-femtojava.jar \
		dpi \
		caco \
		saito 
	cp /tmp/hades-models-femtojava.jar webdemos/classes/ 
	@echo ok.

#
# prepare the webdemos/classes/ directory to use the 'monolithic' applet 
# approach: hades.jar as hades-applet.jar, dummy files for the split JARs
#
dummyappletzip:
	@echo creating the monolithic applet JARs
	cp archive/hades.jar webdemos/classes/hades-applet.jar
	- cd ..; jar cvMf /tmp/dummy.jar \
		hades/webdemos/placeholder.txt
	cp /tmp/dummy.jar webdemos/classes/hades-models-dcore.jar
	cp /tmp/dummy.jar webdemos/classes/hades-models-fsm.jar
	cp /tmp/dummy.jar webdemos/classes/hades-models-imaging.jar
	cp /tmp/dummy.jar webdemos/classes/hades-models-mcs4.jar
	cp /tmp/dummy.jar webdemos/classes/hades-models-microjava.jar
	cp /tmp/dummy.jar webdemos/classes/hades-models-mips.jar
	cp /tmp/dummy.jar webdemos/classes/hades-models-pic.jar
	cp /tmp/dummy.jar webdemos/classes/hades-models-register.jar
	cp /tmp/dummy.jar webdemos/classes/hades-models-rtl.jar
	cp /tmp/dummy.jar webdemos/classes/hades-models-rtlib.jar
	cp /tmp/dummy.jar webdemos/classes/hades-models-special.jar
	cp /tmp/dummy.jar webdemos/classes/hades-models-stimuli.jar
	cp /tmp/dummy.jar webdemos/classes/hades-models-ttl.jar
	@echo ok.

website:
	@echo "creating /tmp/jetty website (using LANG=de_DE)"
	cp archive/hades.jar webdemos/classes/hades.jar;
	cp archive/hades-signed.jar webdemos/classes/hades-signed.jar;
	cd webdemos; make;
	@echo ok.



classdoczip:
	@echo javadoc...
	cd ..; javadoc -package -breakiterator -d $(HADESDIR)/classdoc -J-mx128M \
	hades.jpshell \
	hades.gui \
	hades.manager \
	hades.manager.tree \
	hades.models \
	hades.models.complexgates \
	hades.models.dcf77 \
	hades.models.flipflops \
	hades.models.fsm \
	hades.models.gates \
	hades.models.gatter \
	hades.models.imaging \
	hades.models.io \
	hades.models.mcore \
	hades.models.memory \
	hades.models.meta \
	hades.models.mcs4 \
	\
	hades.models.mips.core \
	hades.models.mips.gui \
	hades.models.mips.instr \
	hades.models.mips.memory \
	hades.models.mips.mipsmemory \
	hades.models.mips.tools \
	\
	hades.models.pic \
	hades.models.register \
	hades.models.rtl \
	hades.models.rtlib \
	hades.models.rtlib.arith \
	hades.models.rtlib.compare \
	hades.models.rtlib.io \
	hades.models.rtlib.logic \
	hades.models.rtlib.memory \
	hades.models.rtlib.muxes \
	hades.models.rtlib.register \
	hades.models.ruge \
	hades.models.special \
	hades.models.stimuli \
	hades.models.string \
	hades.models.ttl74 \
	hades.signals \
	hades.simulator \
	hades.styx \
	hades.symbols \
	hades.utils \
	hades.utils.vhdl \
	jfig.canvas \
	jfig.commands \
	jfig.gui \
	jfig.objects \
	jfig.utils 
	@echo packaing class documentation...
	cd ..; $(JAR) -cMvf hades-classdoc.jar \
		hades/doc/README hades/doc/INSTALL hades/doc/CHANGES hades/doc/FAQ \
		hades/classdoc 
	mv ../hades-classdoc.jar $(ARCHIVEDIR)/hades-classdoc.zip


tar:
	@echo HADES tar.gz archive with everything inside
	cd ..; tar -cvhf hades.tar hades jfig GIFEncoder; gzip hades.tar 
	@echo you should now move the hades.tar file to somewhere safe


classjar:
	@echo signed HADES and jfig class jar archive
	exit -1
	mv ../hades.jar $(ARCHIVEDIR)/hades.jar
	@echo ...signing the class archive...
	cd $(ARCHIVEDIR); $(JAVAKEY) -gs Sign_directive_Hendrich hades.jar
	rm $(ARCHIVEDIR)/hades.jar



megazip:
	@echo HADES/jfig class archive, some examples
	cd ..; $(JAR) -cvMf hades-mega.zip \
		hades/doc/README hades/doc/INSTALL hades/doc/CHANGES hades/doc/FAQ \
		hades/makefile \
		hades/.hadesrc \
		hades/gui/images hades/gui/*.html \
		hades/gui/PopupMenu.txt \
		hades/gui/ViewModePopupMenu.txt \
		hades/*/*.class hades/*/*/*.class hades/*/*/*/*.class \
		hades/simulator/*.sym \
		hades/manager \
		hades/models/*.sym hades/models/*/*.sym hades/models/*/*/*.sym \
		hades/models/*.rom hades/models/*/*.rom hades/models/*/*/*.rom \
		hades/models/*.fsm hades/models/*/*.fsm hades/models/*/*/*.fsm \
		hades/*/README hades/*/*/README hades/*/*/*/README \
		hades/models/ttl74/*.hds hades/models/ttl74/figs/* \
		hades/models/*.gif hades/models/*/*.gif \
		hades/models/*.fig hades/models/*/*.fig \
		hades/models/*.hds hades/models/*/*.hds \
		hades/models/*/*/*.gif \
		hades/models/pic/help \
		hades/utils/vhdl/vhdl-classmap.txt \
		hades/styx/*.gif hades/styx/shortcut-keys.txt \
		hades/examples/tutorial \
		hades/examples/simple \
		hades/examples/pic16c84 \
		hades/scripts \
		hades/jpshell \
		hades/doc/help \
		jfig/canvas/*.class \
		jfig/commands/*.class \
		jfig/objects/*.class \
		jfig/utils/*.class \
		jfig/gui/*.class \
		jfig/doc \
		jfig/gui/*.html \
		jfig/examples \
		jfig/images \
		jfig/jfig.cnf \
		GIFEncoder/*.class
	mv ../hades-mega.zip $(ARCHIVEDIR)/hades-mega.zip


gatelevelzip:
	@echo HADES/jfig gate level applet archive, minimal size
	cd ..; $(JAR) cvmf hades/gui/Manifest hades-gatelevel.zip \
	hades/doc/README hades/doc/INSTALL \
	hades/doc/FAQ \
	hades/doc/TODO \
	hades/.hadesrc \
	hades/gui/images/simcontrol.gif \
	hades/gui/images/simcontrol_gray.gif \
	hades/gui/images/hades.gif \
	hades/gui/images/sound.gif \
	hades/gui/PopupMenu.txt \
	hades/gui/ViewModePopupMenu.txt \
	\
	hades/gui/*.class \
	\
	hades/manager/DesignManager.class \
	hades/manager/SimObjectNotFoundException.class \
	hades/manager/SimObjectVersionNotFoundException.class \
	hades/simulator/*.class \
	hades/symbols/*.class \
	hades/signals/*.class \
	\
	hades/styx/README \
	hades/styx/shortcut-keys.txt \
	hades/styx/*.class \
	hades/gui/images/wavebuttons.gif \
	\
	hades/utils/AudioFileLoader.class \
	hades/utils/AudioPlayer.class \
	hades/utils/ContextToolTip.class \
	hades/utils/DecimalFormat.class \
	hades/utils/EndsWithFilter.class \
	hades/utils/FigWriter.class \
	hades/utils/HexFormat.class \
	hades/utils/JviewJythonWrapper.class \
	hades/utils/LFSR32.class \
	hades/utils/NameListener.class \
	hades/utils/Parser.class \
	hades/utils/Selection.class \
	hades/utils/ShellSort.class \
	hades/utils/SignalEnumerator.class \
	hades/utils/StringTokenizer.class \
	hades/utils/TimeFormatter.class \
	hades/utils/ToolTipManager$1.class \
	hades/utils/ToolTipManager.class \
	hades/utils/NameMangler.class \
	\
	hades/models/*.class \
	hades/models/*.sym \
	hades/models/gates/*.class \
	hades/models/gates/*.sym \
	hades/models/io/*.class \
	hades/models/io/*.sym \
	hades/models/flipflops/*.class \
	hades/models/flipflops/*.sym \
	\
        jfig/canvas/FigCanvas*class \
        jfig/canvas/FigDrawable*class \
        jfig/canvas/FigSwingCanvas*class \
        jfig/canvas/FigTrafo*class \
        jfig/canvas/FullRedraw.class \
        jfig/canvas/ObjectPainter.class \
        jfig/canvas/SyncPainter.class \
        jfig/canvas/ZoomListener.class \
	\
	jfig/commands/Command.class \
	jfig/commands/FigBasicEditor.class \
	\
	jfig/gui/JStatusCanvas*class \
	jfig/gui/JTextViewer*.class \
	jfig/gui/About*.class \
	jfig/gui/ConfirmDialog.class \
	jfig/gui/Console*.class \
	jfig/gui/ColorCache.class \
	jfig/gui/Export*.class \
	jfig/gui/FontCache*class \
	jfig/gui/ImageHelper.class \
	jfig/gui/InsetsPanel.class \
	jfig/gui/InvertGrayFilter.class \
	jfig/gui/SimpleTextViewer*.class \
	jfig/gui/StatusCanvas.class \
	jfig/gui/StatusMessage.class \
	\
	jfig/objects/*.class \
	jfig/java2d/*.class \
	\
	jfig/utils/JRecentFileManager*class \
	jfig/utils/AntiDeadlock.class \
	jfig/utils/BoundingBoxCalculator.class \
	jfig/utils/ExceptionTracer.class \
	jfig/utils/FilteredFigWriter.class \
	jfig/utils/LP2*class \
	jfig/utils/Format.class \
	jfig/utils/MouseMapper.class \
	jfig/utils/Pathname.class \
	jfig/utils/SetupManager.class \
	\
	jfig/jfig.cnf 
	mv ../hades-gatelevel.zip $(ARCHIVEDIR)/hades-gatelevel.zip


# NOTE: The following are important classes that we don't include into
#       hades-ws2004.jar (yet):
#
	# hades/doc/CHANGES \
	# hades/gui/HexTextField*class
	# hades/gui/MemoryEditorFrame*class
	# hades/gui/MemoryHexEditorField.class
 	# 
hades-ws2004:
	@echo HADES/jfig gate level applet archive, minimal size
	cd ..; $(JAR) cmf hades/gui/Manifest.WS2004 hades-ws2004.jar \
	hades/doc/README hades/doc/INSTALL hades/doc/FAQ hades/doc/TODO \
	hades/.hadesrc \
	\
	hades/.hadesrc.ws2004 \
	hades/gui/PopupMenuWS2004.txt \
	hades/gui/T1Editor*class \
	\
	hades/gui/images/simcontrol.gif \
	hades/gui/images/simcontrol_gray.gif \
	hades/gui/images/hades.gif \
	hades/gui/images/sound.gif \
	hades/gui/PopupMenu.txt \
	hades/gui/*Command*class \
	hades/gui/CanvasScroller*class \
	hades/gui/Console*class \
	hades/gui/Editor*class \
	hades/gui/GUIFactory.class \
	hades/gui/AWTFactory.class \
	hades/gui/SelectURLDialog*class \
	hades/gui/PropertySheet*class \
	hades/gui/StringDialog*class \
	hades/gui/ExportOptionsDialog*class \
	hades/gui/SimControlPanel*class \
	hades/gui/StatusPanel*class \
	hades/gui/ObjectCanvas*class \
	\
	hades/gui/ConfirmDialog*class \
	hades/gui/SaveChangesDialog*class \
	\
	hades/gui/JAboutDialog.class \
	hades/gui/JCanvasScroller*class \
	hades/gui/JConfirmDialog.class \
	hades/gui/JConsole*class \
	hades/gui/JEditFrame.class \
	hades/gui/JExportOptionsAdapter.class \
	hades/gui/JImageButton.class \
	hades/gui/JMultiLineToolTip.class \
	hades/gui/JObjectCanvas*class \
	hades/gui/JPropertiesViewer.class \
	hades/gui/JPropertySheet.class \
	hades/gui/JSelectURLDialog*class \
	hades/gui/JSimControlPanel*class \
	hades/gui/JStatusPanel.class \
	hades/gui/JStringDialog.class \
	hades/gui/JTrafficLight.class \
	hades/gui/KeyHandler.class \
	hades/gui/LayerTable.class \
	hades/gui/Log.class \
	hades/gui/LogManager.class \
	hades/gui/OKtoQuit.class \
	hades/gui/SwingFactory.class \
	hades/gui/SyncRedrawTimer.class \
	hades/gui/Trafo2D.class \
	hades/gui/UndoStack.class \
	hades/gui/WindowCloser.class \
	\
	hades/manager/DesignManager*class \
	hades/manager/ExtensionFileFilter.class \
	hades/manager/SimObjectNotFoundException.class \
	hades/manager/SimObjectVersionNotFoundException.class \
	\
	hades/simulator/*.class \
	hades/symbols/*.class \
	hades/signals/*.class \
	\
	hades/styx/README hades/styx/shortcut-keys.txt \
	hades/styx/*.class \
	\
	hades/utils/AudioFileLoader.class \
	hades/utils/AudioPlayer.class \
	hades/utils/ContextToolTip.class \
	hades/utils/DecimalFormat.class \
	hades/utils/EndsWithFilter.class \
	hades/utils/FigWriter.class \
	hades/utils/HexFormat.class \
	hades/utils/JviewJythonWrapper.class \
	hades/utils/LFSR32.class \
	hades/utils/NameListener.class \
	hades/utils/Parser.class \
	hades/utils/Selection.class \
	hades/utils/ShellSort.class \
	hades/utils/SignalEnumerator.class \
	hades/utils/StringTokenizer.class \
	hades/utils/TimeFormatter.class \
	hades/utils/ToolTipManager.class \
	hades/utils/NameMangler.class \
	\
	hades/models/Const1164.class \
	hades/models/Design.class \
	hades/models/FigObject.class \
	hades/models/InputConnector.class \
	hades/models/OutputConnector.class \
	hades/models/PortStdLogic1164.class \
	hades/models/PortStdLogicVector.class \
	hades/models/StdLogic1164.class \
	hades/models/StdLogicVector.class \
	hades/models/FigObject.sym \
	\
	hades/models/gates/*.class \
	hades/models/gates/*.sym \
	\
	hades/models/gatter/*.class \
	hades/models/gatter/*.sym \
	\
	hades/models/io/ClockGen*class \
	hades/models/io/ClockGen*sym \
	hades/models/io/Constant*class \
	hades/models/io/Constant*sym \
	hades/models/io/HexDisplay*class \
	hades/models/io/HexDisplay*sym \
	hades/models/io/HexSwitch.class \
	hades/models/io/HexSwitch.fig \
	hades/models/io/HexSwitch.sym \
	hades/models/io/Ipin*class \
	hades/models/io/Ipin*sym \
	hades/models/io/PulseSwitch.class \
	hades/models/io/PulseSwitch.sym \
	hades/models/io/Opin*class \
	hades/models/io/Opin*sym \
	hades/models/io/LED.class \
	hades/models/io/PowerOnReset.class \
	hades/models/io/PowerOnReset.sym \
	hades/models/io/Pullup.class \
	hades/models/io/Gnd.class \
	hades/models/io/Vcc.class \
	hades/models/io/SevenSegment.class \
	hades/models/io/SevenSegment.sym \
	\
	hades/models/flipflops/Dff.class \
	hades/models/flipflops/DffMetastable.class \
	hades/models/flipflops/Dffe.class \
	hades/models/flipflops/Dffr.class \
	hades/models/flipflops/Dffrs.class \
	hades/models/flipflops/GenericFlipflop.class \
	hades/models/flipflops/Jkff.class \
	hades/models/flipflops/Latch.class \
	hades/models/flipflops/LatchMetastable.class \
	hades/models/flipflops/Latchr.class \
	hades/models/flipflops/Dff.sym \
	hades/models/flipflops/DffMetastable.sym \
	hades/models/flipflops/Dffe.sym \
	hades/models/flipflops/Dffr.sym \
	hades/models/flipflops/Dffrs.sym \
	hades/models/flipflops/Jkff.sym \
	hades/models/flipflops/Latch.sym \
	hades/models/flipflops/LatchMetastable.sym \
	hades/models/flipflops/Latchr.sym \
	\
	hades/models/meta/Label*class \
	\
	hades/models/special/Counter*class \
	hades/models/special/Counter.sym \
	\
	hades/models/ttl74/SN7400*class \
	hades/models/ttl74/SN7400_pinout.sym \
	hades/models/ttl74/figs/SN7400_pinout.fig \
	\
        jfig/canvas/FigCanvas*class \
        jfig/canvas/FigDrawable*class \
        jfig/canvas/FigSwingCanvas*class \
        jfig/canvas/FigTrafo*class \
        jfig/canvas/FullRedraw.class \
        jfig/canvas/ObjectPainter.class \
        jfig/canvas/SyncPainter.class \
        jfig/canvas/ZoomListener.class \
	\
	jfig/commands/Command.class \
	jfig/commands/FigBasicEditor.class \
	\
	jfig/gui/JStatusCanvas.class \
	jfig/gui/JTextViewer*class \
	jfig/gui/JAboutDialog*class \
	jfig/gui/JWindowCloser.class \
	jfig/gui/JPropertiesViewer*class \
	jfig/gui/JExportOptionsDialog*class \
	jfig/gui/JEditTextDialog*class \
	jfig/gui/EditTextDialog*class \
	jfig/gui/EditObjectBaseDialog*class \
	jfig/gui/JEditBaseobjectDialog*class \
	jfig/gui/JStateButton*class \
	jfig/gui/JConsole*class \
	jfig/gui/ConfirmDialog.class \
	jfig/gui/Console*class \
	jfig/gui/ColorCache.class \
	jfig/gui/ExportOptionsDialog*class \
	jfig/gui/FontCache*class \
	jfig/gui/ImageHelper.class \
	jfig/gui/InsetsPanel.class \
	jfig/gui/InvertGrayFilter.class \
	jfig/gui/SimpleTextViewer*class \
	jfig/gui/StatusCanvas.class \
	jfig/gui/StatusMessage.class \
	\
	jfig/objects/FigArc.class \
	jfig/objects/FigArrow.class \
	jfig/objects/FigArrowParams.class \
	jfig/objects/FigAttribs.class \
	jfig/objects/FigBaseobject.class \
	jfig/objects/FigBbox.class \
	jfig/objects/FigBezier*class \
	jfig/objects/FigBezierXSpline.class \
	jfig/objects/FigCompound.class \
	jfig/objects/FigEllipse.class \
	jfig/objects/FigGeneralXSpline.class \
	jfig/objects/FigGlobalAttributes.class \
	jfig/objects/FigImage.class \
	jfig/objects/FigNormalXSpline.class \
	jfig/objects/FigObject.class \
	jfig/objects/FigObjectFactory*class \
	jfig/objects/FigObjectList*class \
	jfig/objects/FigParser.class \
	jfig/objects/FigPolyline.class \
	jfig/objects/FigPrintWriter.class \
	jfig/objects/FigRectangle.class \
	jfig/objects/FigRenderer.class \
	jfig/objects/FigSpline.class \
	jfig/objects/FigText.class \
	jfig/objects/FigTrigger.class \
	jfig/objects/FigWriter.class \
	jfig/objects/FigXSpline.class \
	jfig/objects/FillPatterns*class \
	jfig/objects/FillWrapper.class \
	jfig/objects/LineWrapper.class \
	jfig/objects/ListNode.class \
	\
	jfig/java2d/*.class \
	\
	jfig/utils/JRecentFileManager.class \
	jfig/utils/AntiDeadlock.class \
	jfig/utils/BoundingBoxCalculator.class \
	jfig/utils/ExceptionTracer.class \
	jfig/utils/FilteredFigWriter.class \
	jfig/utils/LP2.class \
	jfig/utils/ShellSort.class \
	jfig/utils/Format.class \
	jfig/utils/MouseMapper.class \
	jfig/utils/Pathname.class \
	jfig/utils/SetupManager.class \
	jfig/jfig.cnf 
	mv ../hades-ws2004.jar $(ARCHIVEDIR)/hades-ws2004.jar
	jarsigner -keystore ~/java/jfig/jfig-selfsigned-keystore archive/hades-ws2004.jar fnh



# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


classzip:
	@echo HADES/jfig class archive, few examples - but all .sym
	- cd ..; $(JAR) cvmf hades/gui/Manifest hades.jar \
		hades/doc/README \
		hades/doc/INSTALL \
		hades/doc/CHANGES \
		hades/doc/FAQ \
		hades/doc/TODO \
		hades/makefile \
		hades/.hadesrc \
		hades/.clblist.txt \
		\
		hades/gui/images/didyouknow.gif \
		hades/gui/images/hades.gif \
		hades/gui/images/iconEditor.gif \
		hades/gui/images/lcd-matrix.gif \
		hades/gui/images/python.gif \
		hades/gui/images/simcontrol.gif \
		hades/gui/images/terminal-big.gif \
		hades/gui/images/wavebuttons.gif \
		hades/gui/PopupMenu.txt \
		hades/gui/PopupMenuWS2004.txt \
		hades/gui/ViewModePopupMenu.txt \
		\
		hades/*/*.class hades/*/*/*.class hades/*/*/*/*.class \
		hades/simulator/*.sym \
		hades/manager/*.class \
		hades/manager/tree/*.class \
		hades/manager/icons/*.gif \
		\
		hades/models/*.sym hades/models/*/*.sym hades/models/*/*/*.sym \
		hades/models/*.clb hades/models/*/*.clb hades/models/*/*/*.clb \
		hades/models/*.rom hades/models/*/*.rom hades/models/*/*/*.rom \
		hades/models/*.fsm hades/models/*/*.fsm hades/models/*/*/*.fsm \
		hades/*/README hades/*/*/README hades/*/*/*/README \
		hades/models/ttl74/*.hds hades/models/ttl74/figs/* \
		hades/models/*.fig hades/models/*/*.fig \
		hades/models/*.gif hades/models/*/*.gif \
		hades/models/*.hds hades/models/*/*.hds \
		hades/models/*/*/*.gif \
		hades/models/pic/help \
		hades/models/io/Stimulus.hst \
		hades/models/meta/AudioPlayer.wav \
		\
		hades/models/imaging/256_*.jpg\
		hades/utils/vhdl/vhdl-classmap.txt \
		hades/styx/*.gif \
		hades/styx/shortcut-keys.txt \
		hades/jpshell \
		hades/doc/help \
		hades/examples/appetizers \
		\
                jfig/canvas/*.class \
                jfig/commands/*.class \
                jfig/gui/*.class \
                jfig/java2d/*.class \
                jfig/objects/*.class \
                jfig/utils/*.class \
		\
                jfig/images/icon.gif \
                jfig/images/buttons.gif \
                jfig/images/fontmenu.gif \
                jfig/images/fillpatterns.gif \
                jfig/images/updatebutton.gif \
                \
                jfig/jfig.cnf 
	mv ../hades.jar $(ARCHIVEDIR)/hades.jar
	cp $(ARCHIVEDIR)/hades.jar $(ARCHIVEDIR)/hades.zip


#hades/examples/tutorial \
#hades/examples/simple \
#hades/examples/pic16c84 \
#hades/testsuite \
#hades/scripts \
#jfig/examples \
#jfig/gui/*.html \
#jfig/gui/UserEditor.java \
#jfig/gui/ExportOptionsDialog.java \
#jfig/utils/MakePieChart.java 
#jfig/fonts/*.ttf \


src2zip:
	@echo HADES/jfig source archive, few examples - but all .sym
	cd ..; $(JAR) -cvMf hades-src-small.zip \
		hades/doc/README hades/doc/INSTALL hades/doc/CHANGES hades/doc/FAQ \
		hades/doc/TODO \
		hades/makefile \
		hades/.hadesrc \
 		hades/gui/images \
		hades/gui/PopupMenu.txt \
		hades/gui/ViewModePopupMenu.txt \
		hades/*.java \
		hades/gui/*.java hades/jpshell/*.java hades/manager/*.java \
		hades/models/*.java hades/signals/*.java hades/simulator/*.java \
		hades/styx/*.java hades/symbols/*.java hades/utils/*.java \
		hades/*/*/*.java hades/*/*/*/*.java \
		hades/*/README hades/*/*/README hades/*/*/*/README \
		hades/manager \
		hades/models/*.hds hades/models/*/*.hds hades/models/*/*/*.hds \
		hades/models/*.fig hades/models/*/*.fig hades/models/*/*/*.fig \
		hades/models/*.gif hades/models/*/*.gif hades/models/*/*/*.gif \
		hades/models/*.sym hades/models/*/*.sym hades/models/*/*/*.sym \
		hades/models/*.clb hades/models/*/*.clb hades/models/*/*/*.clb \
		hades/models/*.rom hades/models/*/*.rom hades/models/*/*/*.rom \
		hades/models/*.fsm hades/models/*/*.fsm hades/models/*/*/*.fsm \
		hades/*/*.sav hades/models/*/*.sav hades/models/*/*/*.sav \
		hades/models/io/Stimulust.hst \
		hades/models/meta/AudioPlayer.wav \
		hades/styx/*.gif hades/styx/shortcut-keys.txt \
		hades/models/pic/examples hades/models/pic/help \
		hades/models/pic/programmer \
		hades/models/mips/examples hades/models/mips/bin \
		hades/models/mips/makefile \
		hades/utils/vhdl/vhdl-classmap.txt \
		hades/examples/tutorial \
		hades/scripts \
		hades/testsuite \
		hades/jpshell \
		hades/doc/help \
		hades/gui/Manifest



signedclasszip:
	@echo signing the hades.jar file:
	cp archive/hades.jar archive/hades-signed.jar
	jarsigner -keystore ~/java/jfig/jfig-selfsigned-keystore archive/hades-signed.jar fnh
	# jarsigner -keystore ~/java/jfig3/jfig/jfig-selfsigned-keystore archive/hades-signed.jar fnh

signedfreettszip:
	@echo signing the freetts-repacked.jar archive:
	cp webdemos/classes/freetts-repacked.jar webdemos/classes/freetts-repacked-signed.jar
	jarsigner -keystore ~/java/jfig/jfig-selfsigned-keystore webdemos/classes/freetts-repacked-signed.jar fnh

	

srczip:
	@echo HADES/jfig source archive, few examples - but all .sym
	- cd ..; $(JAR) -cvMf hades-src.zip \
		hades/doc/README hades/doc/INSTALL hades/doc/CHANGES hades/doc/FAQ \
		hades/doc/TODO \
		hades/makefile \
		hades/.hadesrc* \
		hades/.clblist.txt \
 		hades/gui/images \
		hades/gui/*PopupMenu*.txt \
		hades/*.java \
		hades/*/*.java hades/*/*/*.java hades/*/*/*/*.java \
		hades/*/README hades/*/*/README hades/*/*/*/README \
		hades/manager \
		hades/models/*.hds hades/models/*/*.hds hades/models/*/*/*.hds \
		hades/models/*.fig hades/models/*/*.fig hades/models/*/*/*.fig \
		hades/models/*.gif hades/models/*/*.gif hades/models/*/*/*.gif \
		hades/models/*.sym hades/models/*/*.sym hades/models/*/*/*.sym \
		hades/models/*.clb hades/models/*/*.clb hades/models/*/*/*.clb \
		hades/models/*.rom hades/models/*/*.rom hades/models/*/*/*.rom \
		hades/models/*.fsm hades/models/*/*.fsm hades/models/*/*/*.fsm \
		hades/models/*.jj  hades/models/*/*.jj  hades/models/*/*/*.jj  \
		hades/*/*.sav hades/models/*/*.sav hades/models/*/*/*.sav \
		hades/models/io/Stimulust.hst \
		hades/models/meta/AudioPlayer.wav \
		hades/styx/*.gif hades/styx/shortcut-keys.txt \
		hades/models/pic/examples hades/models/pic/help \
		hades/models/pic/programmer \
		hades/models/mips/examples hades/models/mips/bin \
		hades/models/mips/makefile \
		hades/utils/vhdl/vhdl-classmap.txt \
		hades/examples/tutorial \
		hades/examples/appetizers \
		hades/scripts \
		hades/testsuite \
		hades/jpshell \
		hades/gui/Manifest* \
		hades/utils/JavaPolicyEditor.Manifest* \
		hades/doc/help 
	mv ../hades-src.zip $(ARCHIVEDIR)/hades-src.zip
	cp $(ARCHIVEDIR)/hades-src.zip $(ARCHIVEDIR)/hades-src-`date +%Y%m%d`.zip


examplezip:
	@echo HADES examples archive
	cd ..; $(JAR) -cvMf hades-examples.jar hades/examples 
	mv ../hades-examples.jar $(ARCHIVEDIR)/hades-examples.zip
	@echo HADES examples-unihh archive
	cd ..; $(JAR) -cvMf hades-examples-unihh.jar \
		hades/examples-unihh \
		hades/examples-midi \
		hades/examples-tmp \
		hades/phraser 
	mv ../hades-examples-unihh.jar $(ARCHIVEDIR)/hades-examples-unihh.zip


doczip:
	@echo HADES documentation jar archive
	cd ..; $(JAR) -cMvf hades-doc.jar \
		hades/doc/README hades/doc/INSTALL hades/doc/CHANGES hades/doc/FAQ \
		hades/doc/tutorial/tutorial.ps \
		hades/doc/html
	mv ../hades-doc.jar $(ARCHIVEDIR)/hades-doc.zip

docsrcjar:
	@echo "HADES documentation source (TeX stuff, etc.) jar archive"
	cd ..; $(JAR) -cMvf hades-doc-src.jar \
		hades/doc
	mv ../hades-doc-src.jar $(ARCHIVEDIR)/hades-doc-src.jar

classdocjar:
	@echo HADES class documentation jar archive
	cd ..; $(JAR) -cMvf hades-classdoc.jar \
		hades/doc/README hades/doc/INSTALL hades/doc/CHANGES hades/doc/FAQ \
		hades/classdoc 
	mv ../hades-classdoc.jar $(ARCHIVEDIR)/hades-classdoc.jar


webdemoszip:
	@echo Hades webdemos source directory archive
	jar cvf archive/webdemos.zip webdemos
	@echo ok.


examplejar:
	@echo HADES examples jar archive
	cd ..; $(JAR) -cMvf hades-examples.jar \
		hades/examples 
	mv ../hades-examples.jar $(ARCHIVEDIR)/hades-examples.jar



signedjar: 
	@echo signed HADES jar archive
	make jar;
	cd ..; $(JAVAKEY) -gs hades/Sign_directive_Hendrich hades.jar
	@echo signed HADES jar archive ok.


wwwinstall: 
	@echo ...installing HADES to $(WWWSERVER):$(WWWDIR)
	ssh $(WWWSERVER) "cp -f $(ARCHIVEDIR)/hades.zip $(WWWARDIR)/hades.zip"
	ssh $(WWWSERVER) "cp -f $(ARCHIVEDIR)/hades-classes.zip $(WWWARDIR)/hades-classes.zip"
	ssh $(WWWSERVER) "cp -f $(JAVAFIGARCHIVEDIR)/jfig-classes.zip $(WWWARDIR)/jfig-classes.zip"
	ssh $(WWWSERVER) "cp -f $(ARCHIVEDIR)/hades-doc.zip $(WWWARDIR)/hades-doc.zip"
	ssh $(WWWSERVER) "cp -f $(ARCHIVEDIR)/hades-classdoc.zip \
                                       $(WWWARDIR)/hades-classdoc.zip"
	ssh $(WWWSERVER) "cp -f $(ARCHIVEDIR)/hades-examples.zip \
                                       $(WWWARDIR)/hades-examples.zip"
	ssh $(WWWSERVER) "cp -f $(HADESDIR)/doc/README $(WWWDIR)"
	ssh $(WWWSERVER) "cp -f $(HADESDIR)/doc/README $(WWWARDIR)"
	ssh $(WWWSERVER) "cp -f $(HADESDIR)/doc/CHANGES $(WWWARDIR)"
	ssh $(WWWSERVER) "cp -f $(HADESDIR)/doc/INSTALL $(WWWARDIR)"
	ssh $(WWWSERVER) "cp -f $(HADESDIR)/doc/FAQ $(WWWARDIR)"
	ssh $(WWWSERVER) "cp -f $(HADESDIR)/doc/qrc/referenzkarte.pdf $(WWWARDIR)"
	ssh $(WWWSERVER) "chmod a+r $(WWWDIR)/*.html $(WWWDIR)/archive/*"
	ssh $(WWWSERVER) "touch $(HADESDIR)/index.html"
	ssh $(WWWSERVER) "chmod a-r $(WWWDIR)/archive/hades-src.zip"


t3zip:
	@echo Creating the T3 template designs and master solution...
	jar -cMvf archive/t3-hades.zip t3
	jar -cMvf archive/t3-master.zip t3-master

t3install:
	@echo Installing the T3 template designs...
	scp archive/t3-hades.zip $(WWWSERVER):$(WWWDOCDIR)/t3-hades.zip
	scp archive/hades.zip $(WWWSERVER):$(WWWDOCDIR)/hades.zip

optinstall-old:
	@echo Installing to $INSTALLDIR...
	cp $(ARCHIVEDIR)/hades.jar.sig $(INSTALLDIR)/hades.jar
	cd $(INSTALLDIR); jar xvf $(ARCHIVEDIR)/hades-examples.jar
	cd $(INSTALLDIR); jar xvf $(ARCHIVEDIR)/hades-doc.jar
	#cd $(INSTALLDIR); chmod a-rwx examples/b-tutorial
	cp scripts/runhades scripts/runjfig $(INSTALLDIR)

optinstall:
	@echo Installing to $INSTALLDIR...
	cp $(ARCHIVEDIR)/hades.zip $(INSTALLDIR)/classes/
	chmod a+r $(INSTALLDIR)/classes/hades.zip
	



echo:
	@echo $(OBJ)


help:
	@echo Use on of the following targets:
	@echo classzip srczip megazip webdemoszip wwwinstall optinstall		
	@echo signedclasszip 
	@echo appletzip \(experimental\)
	@echo dummyappletzip \(hades.jar as hades-applet.jar\)
	@echo website   \(experimental\)
	@echo policyjar \(experimental\)


policyjar:
	@echo building the JavaPolicyEditor tool
	cd utils; $(JAVAC) JavaPolicyEditor.java
	cd utils; $(JAR) cvmf JavaPolicyEditor.Manifest ../JavaPolicyEditor.jar JavaPolicyEditor.class JavaPolicyEditor.java
	jarsigner -keystore ~/java/jfig/jfig-selfsigned-keystore JavaPolicyEditor.jar fnh
	cp JavaPolicyEditor.jar webdemos/classes/JavaPolicyEditor.jar
	mv JavaPolicyEditor.jar webdemos/classes/JavaPolicyEditor.zip



allarchives:
	make classzip srczip megazip classdoczip wwwinstall optinstall

